import time, threading
from urllib.parse import urljoin, urldefrag, urlparse

class RateLimiter:
    def __init__(self, delay=0.2):
        self.delay = float(delay)
        self.lock = threading.Lock()
        self.last = 0.0

    def wait(self):
        with self.lock:
            now = time.time()
            to_wait = max(0, self.last + self.delay - now)
            if to_wait:
                time.sleep(to_wait)
            self.last = time.time()

def normalize_url(base, link):
    u = urljoin(base, link)
    u, _ = urldefrag(u)
    return u

def same_domain(a, b):
    return urlparse(a).netloc == urlparse(b).netloc
