const API = "network-security-scanner-production.up.railway.app";


async function runScan() {
    const ip = document.getElementById("ip").value;
    const scanType = document.getElementById("scanType").value;

    const res = await fetch(`${API}/scan`, {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({target:ip, scan_type:scanType})
    });

    const data = await res.json();

    const table = document.getElementById("resultsTable");
    table.innerHTML = "<tr><th>Port</th><th>Service</th><th>Status</th></tr>";

    data.results.forEach(r=>{
        table.innerHTML += `<tr>
            <td>${r.port}</td>
            <td>${r.service}</td>
            <td>${r.state}</td>
        </tr>`;
    });
}

async function addRule() {
    const rule = {
        action: document.getElementById("fwAction").value,
        ip: document.getElementById("fwIP").value || "any",
        port: Number(document.getElementById("fwPort").value) || null,
        protocol: document.getElementById("fwProtocol").value || "any"
    };

    await fetch(`${API}/firewall/add`, {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(rule)
    });

    loadRules();
}

async function loadRules() {
    const res = await fetch(`${API}/firewall/rules`);
    const rules = await res.json();

    const list = document.getElementById("ruleList");
    list.innerHTML = "";
    rules.forEach(r=>{
        list.innerHTML += `<li>${r.action.toUpperCase()} - IP:${r.ip}, Port:${r.port}, Protocol:${r.protocol}</li>`;
    });
}

async function simulateTraffic() {
    const traffic = {
        ip: document.getElementById("tIP").value,
        port: Number(document.getElementById("tPort").value),
        protocol: document.getElementById("tProto").value
    };

    const res = await fetch(`${API}/firewall/check`, {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(traffic)
    });

    const data = await res.json();
    document.getElementById("trafficResult").innerText =
        "Firewall Decision: " + data.decision.toUpperCase();
}

loadRules();

