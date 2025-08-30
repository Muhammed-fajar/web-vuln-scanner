# web-vuln-scanner
“Enterprise Python Web Vulnerability Scanner”
# Web Vulnerability Scanner (WVS) — Enterprise / Extreme Edition

A production-oriented, extensible Python web vulnerability scanner for learning and authorized assessments.
Designed to be resume-ready and easy to demonstrate on GitHub.

## Features
- Domain-limited crawler with depth control and polite rate-limiting
- Form discovery and payload-based tests (SQLi, Reflected XSS)
- Param checks: open redirect, param-based SQLi/XSS
- Sensitive file discovery (.env, .git, backup files)
- Security headers/cookie flag checks, mixed-content, directory listing
- Plugin-based checks for easy extension
- Optional Selenium rendering for JS-heavy apps
- HTML, JSON and PDF reports
- Docker + docker-compose demo (with OWASP Juice Shop)
- GitHub Actions CI for linting

Legal: **Scan only systems you own or have explicit permission to test.**

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m wvs -u http://localhost:3000 -d 2 --threads 8 --rate 0.2
