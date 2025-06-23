from scan_modules.header_scan import check_security_headers

url = "http://scanme.nmap.org"  # Or try your own localhost site

missing = check_security_headers(url)

if missing is not None:
    if missing:
        print(f"\n[!] Missing security headers on {url}:")
        for h in missing:
            print(f"  - {h}")
    else:
        print(f"\n[✔] All recommended security headers are present on {url}")
