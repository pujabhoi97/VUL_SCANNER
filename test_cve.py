from scan_modules.cve_check import check_cve_banners

url = "http://scanme.nmap.org"

cves = check_cve_banners(url)

if cves:
    print(f"\n[!] Possible vulnerable banners found on {url}:")
    for banner, cve in cves:
        print(f"  - {banner} → {cve}")
else:
    print(f"\n[✔] No known vulnerable banners found on {url}")
