# Device Fleet Management Skill

> Endpoint management for AI agents — device health, security posture, compliance checks, diagnostics, and remediation via mcp-device-management (Intune/Jamf/Fleet/Kandji).

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--device--management-green)](https://github.com/zavora-ai/mcp-device-management)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Security Posture | 1-2 | Compliance check against policy |
| Health Check | 2 | System stats + diagnostics |
| Remediation | 1 | Create fix task for violations |
| Fleet Report | 2-3 | Compliance % across all devices |

### Without this skill:
- Non-compliant devices access production undetected
- Hardware issues discovered only when users complain
- No fleet-wide compliance visibility

### With this skill:
- Compliance checked before granting access
- Health issues detected proactively
- Fleet compliance dashboard with action items

## Installation

```bash
git clone https://github.com/zavora-ai/skill-device-fleet-management.git \
  ~/.skills/skills/device-fleet-management
```

## Requirements

**Required:** `mcp-device-management` (10 tools)

**Cross-MCP:**
- `mcp-identity` — block access for non-compliant devices
- `mcp-itsm` — auto-create tickets for hardware issues
- `mcp-slack` — fleet compliance reports

## Folder Structure

```
device-fleet-management/
├── SKILL.md                       # Decision tree + compliance rules
├── scripts/
│   └── compliance_check.py        # Policy compliance validator
├── references/
│   ├── tool-sequences.md          # 10 tools
│   ├── cross-mcp-workflows.md     # Devices + Identity + ITSM + Slack
│   └── examples.md                # Posture check, health, fleet report
├── README.md
└── LICENSE
```

## Scripts

### `compliance_check.py`
```bash
python scripts/compliance_check.py '{"id": "dev_1", "posture": {"encryption": true, "firewall": false}}'
# → {"compliant": false, "violations": [{"requirement": "firewall"}], "action": "notify_user"}
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

## How It Works

### Compliance-First Approach

Every device interaction starts with a security posture check:
1. Check encryption, firewall, OS version, antivirus
2. Flag violations immediately
3. Block access for critically non-compliant devices
4. Create remediation tasks for fixable issues
