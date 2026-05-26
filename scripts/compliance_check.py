#!/usr/bin/env python3
"""Check device compliance against security policy."""
import json, sys

REQUIRED = {
    "encryption": True,
    "firewall": True,
    "os_up_to_date": True,
    "antivirus": True,
    "screen_lock": True,
}

def check(device):
    posture = device.get("posture", {})
    violations = []
    for req, expected in REQUIRED.items():
        actual = posture.get(req, False)
        if actual != expected:
            violations.append({"requirement": req, "expected": expected, "actual": actual})
    
    return {
        "device_id": device.get("id"),
        "compliant": len(violations) == 0,
        "violations": violations,
        "risk_level": "critical" if len(violations) > 2 else "high" if violations else "none",
        "action": "restrict_access" if len(violations) > 2 else "notify_user" if violations else "none",
    }

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
