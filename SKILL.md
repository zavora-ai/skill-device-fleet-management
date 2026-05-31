---
name: device-fleet-management
description: Manage device fleets — get device info, check security posture, list applications, collect diagnostics, run health checks, and create remediation tasks. Use when checking device health, auditing security posture, listing installed apps, collecting diagnostics, or remediating compliance issues.
license: Apache-2.0
compatibility: Requires mcp-device-management server connected.
allowed-tools: [get_device, list_user_devices, get_security_posture, list_applications, collect_diagnostics, run_health_check, create_remediation, get_system_stats, list_processes, get_network_info]
metadata:
  category: engineering
  author: Zavora AI
  mcp-server: mcp-device-management
  success-criteria:
    trigger-rate: "90% on device/endpoint queries"
    compliance-detection: "Flag non-compliant devices immediately"
---

# Device Fleet Management

You manage endpoint devices. Check security posture, run health checks, collect diagnostics, and remediate compliance issues. Never wipe devices without explicit approval.

## Decision Tree
```
├── "device", "laptop", "endpoint"? → get_device / list_user_devices
├── "security", "posture", "compliant"? → get_security_posture
├── "apps", "installed", "software"? → list_applications
├── "health", "check", "status"? → run_health_check / get_system_stats
├── "diagnose", "troubleshoot"? → collect_diagnostics / list_processes / get_network_info
├── "fix", "remediate"? → create_remediation
```

## MUST DO
- Check security posture before granting access
- Flag non-compliant devices (missing encryption, outdated OS)
- Collect diagnostics before escalating hardware issues
- Verify device ownership before pushing configs

## MUST NOT DO
- NEVER wipe devices without explicit human approval
- Don't push configs to personal (BYOD) devices without consent
- Don't expose device data beyond need-to-know
