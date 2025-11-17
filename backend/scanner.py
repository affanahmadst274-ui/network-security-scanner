import nmap

def run_scan(target: str, scan_type: str):
    nm = nmap.PortScanner()

    if scan_type == "syn":
        args = "-sS"
    elif scan_type == "udp":
        args = "-sU"
    else:
        args = "-sT"

    nm.scan(target, arguments=args)
    results = []

    for proto in nm[target].all_protocols():
        ports = nm[target][proto].keys()
        for port in ports:
            results.append({
                "port": port,
                "service": nm[target][proto][port]["name"],
                "state": nm[target][proto][port]["state"]
            })

    return results

