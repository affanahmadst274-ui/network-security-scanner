from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scanner import run_scan
from firewall import apply_rules
from models import ScanRequest, FirewallRule, Traffic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

firewall_rules = []

@app.post("/scan")
async def scan_network(req: ScanRequest):
    results = run_scan(req.target, req.scan_type)
    return {"ip": req.target, "results": results}

@app.post("/firewall/add")
async def add_rule(rule: FirewallRule):
    firewall_rules.append(rule)
    return {"status": "rule added", "total_rules": len(firewall_rules)}

@app.post("/firewall/check")
async def check_traffic(traffic: Traffic):
    action = apply_rules(firewall_rules, traffic)
    return {"decision": action}

@app.get("/firewall/rules")
async def get_rules():
    return firewall_rules

