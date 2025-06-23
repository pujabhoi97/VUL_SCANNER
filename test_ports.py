from scan_modules.port_scan import scan_ports

target = "scanme.nmap.org"
ports = range(20, 100)  

open_ports = scan_ports(target, ports)

print(f"\n[✔] Open ports on {target}: {open_ports}")
