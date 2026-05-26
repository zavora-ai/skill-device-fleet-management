# Device Fleet Cross-MCP Workflows

## Devices + Identity: Access Based on Posture
```
DEVICES: get_security_posture(device_id) → {compliant: false, issues: ["encryption_off"]}
IDENTITY: request_access(user_id, resource: "production") → BLOCKED
→ "Access denied: device not compliant (encryption disabled)"
```

## Devices + ITSM: Auto-Create Ticket for Hardware Issues
```
DEVICES: run_health_check(device_id) → {disk: "95% full", battery: "degraded"}
ITSM: create_ticket(type: "request", subject: "Hardware issue: disk full + battery degraded", assignee: "it-support")
NOTIFICATIONS: send_notification(recipient: user, title: "IT ticket created for your device")
```

## Devices + Slack: Fleet Compliance Report
```
DEVICES: [for all devices] get_security_posture() → {compliant: 45, non_compliant: 3}
SLACK: send_message(channel: "#it-ops", text: "📊 Fleet compliance: 93.8% (45/48). 3 devices non-compliant. Action needed.")
```
