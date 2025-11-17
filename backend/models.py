from pydantic import BaseModel
from typing import List, Optional

class ScanRequest(BaseModel):
    target: str
    scan_type: str  # syn, udp, full

class PortResult(BaseModel):
    port: int
    service: str
    state: str

class ScanResponse(BaseModel):
    ip: str
    results: List[PortResult]

class FirewallRule(BaseModel):
    action: str  # allow / deny
    ip: Optional[str]
    port: Optional[int]
    protocol: Optional[str]

class Traffic(BaseModel):
    ip: str
    port: int
    protocol: str

