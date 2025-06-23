import socket

def scan_ports(target, ports=range(1, 101)):  
    open_ports = []
    print(f"\n[+] Scanning ports on {target}...\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is OPEN")
            sock.close()
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")
    
    return open_ports
