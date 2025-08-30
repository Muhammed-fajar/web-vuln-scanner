import requests, threading, queue
from .utils import RateLimiter, normalize_url, same_domain
from .payloads import SQLI_PAYLOADS, XSS_PAYLOADS
from .plugins import check_sensitive_files
from .reporting import save_reports
from .selenium_helper import SeleniumHelper

class Scanner:
    def __init__(self, config):
        self.config = config
        self.visited = set()
        self.to_visit = queue.Queue()
        self.results = {"meta":{"target": config['target']}, "findings":[]}
        self.session = requests.Session()
        self.rate_limiter = RateLimiter(config.get("rate_limit", 0.2))
        self.use_selenium = config.get("use_selenium", False)
        self.selenium = SeleniumHelper(wait=config['selenium']['render_wait']) if self.use_selenium else None

    def crawl(self):
        self.to_visit.put((self.config['target'], 0))
        threads = []
        for _ in range(self.config.get("threads",5)):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        if self.config.get("plugins_enabled", True):
            self.results["findings"] += check_sensitive_files(self.session, self.config['target'])
        if self.selenium:
            self.selenium.close()
        return save_reports(self.results)

    def worker(self):
        while not self.to_visit.empty():
            try:
                url, depth = self.to_visit.get_nowait()
            except:
                break
            if url in self.visited or depth > self.config.get("max_depth",2):
                continue
            self.visited.add(url)
            self.rate_limiter.wait()
            try:
                content = self.get_content(url)
                self.test_payloads(url, content)
            except:
                continue

    def get_content(self, url):
        if self.use_selenium:
            return self.selenium.get_page(url)
        else:
            r = self.session.get(url, timeout=10)
            return r.text

    def test_payloads(self, url, content):
        for payload in SQLI_PAYLOADS + XSS_PAYLOADS:
            if payload in content:
                self.results["findings"].append({
                    "title": "Payload detected",
                    "url": url,
                    "severity": "medium",
                    "description": "Potential vulnerability detected",
                    "evidence": payload
                })
