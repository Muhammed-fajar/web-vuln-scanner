from .payloads import SENSITIVE_FILES

def check_sensitive_files(session, base_url):
    found = []
    for f in SENSITIVE_FILES:
        url = base_url.rstrip("/") + "/" + f
        try:
            r = session.get(url, timeout=5)
            if r.status_code == 200:
                found.append({"title": "Sensitive file", "url": url, "severity": "high"})
        except:
            continue
    return found
