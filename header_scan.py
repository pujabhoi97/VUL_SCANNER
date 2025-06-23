# scan_modules/header_scan.py

import requests

SECURITY_HEADERS = [
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "Content-Security-Policy",
    "X-XSS-Protection"
]

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=5)
        missing_headers = []

        for header in SECURITY_HEADERS:
            if header not in response.headers:
                missing_headers.append(header)

        return missing_headers

    except requests.RequestException as e:
        print(f"[!] Error connecting to {url}: {e}")
        return None
