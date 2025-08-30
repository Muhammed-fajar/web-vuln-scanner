# web-vuln-scanner
# 🌐 Web Vulnerability Scanner (WVS) — Extreme Edition

Fully functional Python web vulnerability scanner with multi-threading, Selenium support, and advanced reporting.

## Features
- Crawls websites with depth control
- Detects SQL Injection & XSS vulnerabilities
- Sensitive file scanning
- Optional Selenium JS rendering
- HTML, JSON, PDF reports
- Plugin-based architecture for easy extension

## Quick Start

```bash
# Clone the repo
git clone https://github.com/yourusername/web-vuln-scanner.git
cd web-vuln-scanner

# Install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run scanner
python -m wvs -c config.yaml
