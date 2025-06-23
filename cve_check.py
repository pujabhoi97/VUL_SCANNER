# scan_modules/cve_check.py

import requests
import re

# Very basic banner → CVE mapping 
CVE_DB = {
    "Apache/2.4.49": "CVE-2021-41773 (Path Traversal)",
    "Apache/2.4.50": "CVE-2021-42013 (Remote Code Execution)",
    "PHP/5.4.0": "CVE-2015-8607 (Memory corruption in EXIF)",
    "nginx/1.3.9": "CVE-2013-2028 (Buffer Overflow)"
}

def check_cve_banners(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        findings = []

        # Check "Server" and "X-Powered-By" headers
        for key in ["Server", "X-Powered-By"]:
            if key in headers:
                banner = headers[key]
                for vulnerable in CVE_DB:
                    if vulnerable in banner:
                        findings.append((banner, CVE_DB[vulnerable]))
        
        return findings

    except requests.RequestException as e:
        print(f"[!] Failed to connect to {url}: {e}")
        return None
