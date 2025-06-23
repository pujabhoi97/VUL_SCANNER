import datetime
from scan_modules.port_scan import scan_ports
from scan_modules.header_scan import check_security_headers
from scan_modules.cve_check import check_cve_banners
from scan_modules.dir_check import check_directory_listing

def generate_html_report(target, open_ports, missing_headers, cve_findings, directory_listing):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <html>
    <head>
        <title>Vulnerability Scan Report for {target}</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            h1 {{ color: #2c3e50; }}
            ul {{ list-style: none; padding-left: 0; }}
            li {{ margin-bottom: 5px; }}
            .section {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>Scan Report for {target}</h1>
        <p><strong>Scanned on:</strong> {timestamp}</p>

        <div class="section">
            <h2>Open Ports</h2>
            <ul>
                {"".join(f"<li>Port {port} is OPEN</li>" for port in open_ports) if open_ports else "<li>No open ports found.</li>"}
            </ul>
        </div>

        <div class="section">
            <h2>Missing Security Headers</h2>
            <ul>
                {"".join(f"<li>{header}</li>" for header in missing_headers) if missing_headers else "<li>All recommended headers are present.</li>"}
            </ul>
        </div>

        <div class="section">
            <h2>Potential Vulnerabilities (CVE)</h2>
            <ul>
                {"".join(f"<li>{banner} → {cve}</li>" for banner, cve in cve_findings) if cve_findings else "<li>No known CVEs detected.</li>"}
            </ul>
        </div>

        <div class="section">
            <h2>Directory Listing</h2>
            <ul>
                <li>{"✅ Enabled — may expose sensitive files!" if directory_listing else "❌ Not enabled — good."}</li>
            </ul>
        </div>
    </body>
    </html>
    """

    with open("scan_report.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("\n✅ Report saved as scan_report.html")


if __name__ == "__main__":
    target = input("Enter the target URL or IP (e.g., http://example.com): ").strip()

    # Extract hostname for port scanning
    hostname = target.replace("http://", "").replace("https://", "").split("/")[0]

    print("\n🔍 Starting scan...\n")

    open_ports = scan_ports(hostname, range(20, 1025))
    missing_headers = check_security_headers(target)
    cve_findings = check_cve_banners(target)
    directory_listing = check_directory_listing(target)

    generate_html_report(target, open_ports, missing_headers, cve_findings, directory_listing)
