---
title: "Incident Response Runbook"
version: "1.0"
category: "27-devops-deployment"
tags:
  - incident-response
  - runbook
  - on-call
  - post-mortem
  - sre
author: "garri333"
description: "Incident response procedures with severity classification, escalation paths, communication templates, and post-mortem generation"
language: "en"
created: "2026-02-22"
---

# Incident Response Runbook

## Objective

Create a **comprehensive incident response framework** covering severity classification (P0–P4), escalation procedures, communication templates for stakeholders, root cause analysis (RCA) methodology, and structured post-mortem generation — enabling teams to respond to incidents consistently, quickly, and transparently.

---

## Context

Every production system will have incidents. The difference between chaos and controlled response is preparation. A well-structured runbook ensures that on-call engineers know exactly what to do at 3 AM, stakeholders receive timely updates, and the organization learns from every incident through blameless post-mortems. This framework draws from SRE best practices at Google, PagerDuty, and Atlassian.

---

## Prompt

You are a **Senior Site Reliability Engineer (SRE)** establishing an incident response program for a mid-sized engineering organization. Generate a complete incident response runbook covering the following areas:

### 1. Severity Classification (P0–P4)

| Severity | Name         | Impact                                           | Response Time | Update Frequency | Examples                                    |
|----------|--------------|--------------------------------------------------|---------------|------------------|---------------------------------------------|
| **P0**   | Critical     | Complete service outage, data loss/breach         | ≤ 5 minutes   | Every 15 minutes | Database down, security breach, data loss   |
| **P1**   | Major        | Major feature unavailable, significant user impact| ≤ 15 minutes  | Every 30 minutes | Auth broken, payments failing, API down     |
| **P2**   | Moderate     | Partial degradation, workaround available         | ≤ 1 hour      | Every 2 hours    | Slow queries, partial feature failure       |
| **P3**   | Minor        | Minor issue, low user impact                      | ≤ 4 hours     | Daily            | UI glitch, non-critical job failure         |
| **P4**   | Informational| No immediate impact, improvement opportunity      | Next sprint   | As needed        | Technical debt, monitoring gap              |

#### Severity Decision Tree

```
Is the service completely unavailable?
├── YES → Are users unable to perform core actions?
│         ├── YES → P0 (Critical)
│         └── NO → P1 (Major)
└── NO → Is there measurable degradation?
          ├── YES → Is there a workaround?
          │         ├── YES → P2 (Moderate)
          │         └── NO → P1 (Major)
          └── NO → Is it user-facing?
                    ├── YES → P3 (Minor)
                    └── NO → P4 (Informational)
```

#### Auto-Classification Triggers
```yaml
# PagerDuty / Alerting rules
auto_classify:
  P0:
    - error_rate > 50% for 5 minutes
    - uptime_check failed for 3 consecutive checks
    - database connection pool exhausted
    - security alert: unauthorized access detected
  P1:
    - error_rate > 20% for 10 minutes
    - response_time p95 > 10s for 10 minutes
    - authentication service degraded
    - payment processing failure rate > 5%
  P2:
    - error_rate > 5% for 15 minutes
    - response_time p95 > 5s for 15 minutes
    - background job failure rate > 10%
    - disk usage > 85%
  P3:
    - error_rate > 1% for 30 minutes
    - non-critical service degradation
    - cache hit rate < 50%
```

### 2. Escalation Procedures

#### Escalation Matrix

```
Level 1 — On-call Engineer (0-15 min)
  ├── Acknowledge alert
  ├── Assess severity
  ├── Begin investigation
  └── Escalate if not resolved in 15 min or if P0/P1

Level 2 — Team Lead / Senior Engineer (15-30 min)
  ├── Join incident channel
  ├── Coordinate investigation
  ├── Make architectural decisions
  └── Escalate if cross-team impact

Level 3 — Engineering Manager + VP Engineering (30-60 min)
  ├── Coordinate cross-team response
  ├── Stakeholder communication
  ├── Resource allocation decisions
  └── Executive briefing if P0

Level 4 — CTO / Executive Team (60+ min for P0 only)
  ├── External communication approval
  ├── Customer notification decisions
  └── Business continuity decisions
```

#### On-Call Rotation Structure
```yaml
on_call:
  primary:
    rotation: weekly
    schedule: Mon 09:00 → Mon 09:00
    handoff: 30-min sync meeting
    
  secondary:
    rotation: weekly
    offset: 1 week ahead of primary
    activation: primary unreachable for 10 min
    
  escalation_chain:
    - primary_engineer (0 min)
    - secondary_engineer (10 min)
    - team_lead (20 min)
    - engineering_manager (30 min)
    
  expectations:
    response_time: 5 minutes (P0/P1), 30 minutes (P2+)
    tools_required: laptop, phone, VPN access
    compensation: on-call stipend + incident bonus
```

### 3. Communication Templates

#### Initial Incident Notification (Internal — Slack/Teams)

```markdown
🔴 **INCIDENT DECLARED — [P0/P1/P2]**

**Title:** [Brief description of the issue]
**Severity:** P[0-4]
**Started:** [Time UTC]
**Impact:** [What users/services are affected]
**Incident Commander:** @[name]
**War Room:** #incident-[YYYY-MM-DD]-[short-name]

**Current Status:**
- [What we know so far]
- [What is being investigated]

**Next Update:** [Time — in 15/30/60 minutes]
```

#### Status Update Template (Internal)

```markdown
📊 **INCIDENT UPDATE — [P0/P1/P2] — Update #[N]**

**Title:** [Brief description]
**Duration:** [X hours Y minutes]
**Status:** Investigating / Identified / Mitigating / Resolved

**What changed since last update:**
- [Action taken and result]
- [New findings]

**Current hypothesis:**
- [What we think is causing the issue]

**Next steps:**
- [ ] [Action item — @owner — ETA]
- [ ] [Action item — @owner — ETA]

**Next Update:** [Time]
```

#### Customer-Facing Status Page Update

```markdown
**[Service Name] — [Investigating/Identified/Monitoring/Resolved]**

We are currently experiencing [brief, non-technical description of impact].

**Impact:** [What customers may notice]
**Workaround:** [If available]
**Started:** [Time with timezone]

We are actively investigating and will provide updates every [N] minutes.

[Posted by: Incident Commander]
```

#### Escalation Request Template

```markdown
🆘 **ESCALATION REQUEST**

**Incident:** #incident-[YYYY-MM-DD]-[name]
**Current Severity:** P[N]
**Requesting:** [What help is needed]
**Reason for Escalation:**
- [Why current responders cannot resolve]
- [What expertise/access is needed]
**Requested From:** @[team/person]
**Urgency:** [Immediate / Within 30 min / Within 1 hour]
```

#### Post-Resolution Customer Communication

```markdown
**[Service Name] — Resolved**

The issue affecting [service/feature] has been resolved as of [time].

**Duration:** [X hours Y minutes]
**Root Cause:** [Brief, non-technical explanation]
**Resolution:** [What was done to fix it]
**Prevention:** [What we're doing to prevent recurrence]

We apologize for the disruption and appreciate your patience.
A detailed post-mortem will be published within [48/72] hours.
```

### 4. Root Cause Analysis (RCA) Methodology

#### The "5 Whys" Framework

```
Problem: API response time increased to 30 seconds

Why 1: The database queries were taking too long
Why 2: The query planner was doing full table scans
Why 3: An index was dropped during a migration
Why 4: The migration script had a bug that dropped the wrong index
Why 5: The migration was not tested against production-scale data

Root Cause: Insufficient testing of database migrations
Contributing Factor: No automated index verification in CI pipeline
```

#### RCA Investigation Checklist

```markdown
## Timeline Reconstruction
- [ ] Gather all alert timestamps
- [ ] Collect relevant log entries (30 min before to 30 min after)
- [ ] Identify all deployments in the last 24 hours
- [ ] Note all configuration changes in the last 24 hours
- [ ] Document manual actions taken during response

## Technical Analysis
- [ ] Identify the failing component(s)
- [ ] Determine the triggering event
- [ ] Assess blast radius (affected services, users, data)
- [ ] Review monitoring gaps (what should have caught this earlier?)
- [ ] Evaluate detection time vs. desired detection time

## Contributing Factors
- [ ] Process failures (missing runbook, unclear ownership)
- [ ] Technical debt (known fragile component)
- [ ] Testing gaps (missing test coverage for this scenario)
- [ ] Monitoring blind spots (missing alerts or dashboards)
- [ ] Communication failures (delayed escalation, unclear updates)
```

#### Severity-Specific RCA Requirements

| Severity | RCA Required | Deadline    | Review By           | Action Items Due |
|----------|-------------|-------------|---------------------|-----------------|
| P0       | Yes         | 48 hours    | VP Engineering      | 1 week          |
| P1       | Yes         | 1 week      | Engineering Manager | 2 weeks         |
| P2       | Optional    | 2 weeks     | Team Lead           | Next sprint     |
| P3       | No          | —           | —                   | Backlog         |
| P4       | No          | —           | —                   | Backlog         |

### 5. Post-Mortem Generation

#### Post-Mortem Template

```markdown
# Post-Mortem: [Incident Title]

**Date:** [YYYY-MM-DD]
**Authors:** [Names of responders]
**Severity:** P[0-4]
**Duration:** [X hours Y minutes]
**Impact:** [Number of users affected, revenue impact, SLA breach]

---

## Executive Summary

[2-3 sentences: what happened, impact, resolution, key takeaways]

---

## Timeline (UTC)

| Time  | Event                                          | Actor         |
|-------|------------------------------------------------|---------------|
| 14:00 | Deployment v2.3.1 rolled out                  | CI/CD         |
| 14:05 | Error rate alert triggered                     | PagerDuty     |
| 14:07 | On-call engineer acknowledged                  | @engineer_a   |
| 14:10 | Incident declared as P1                        | @engineer_a   |
| 14:15 | War room opened, investigation started         | @engineer_a   |
| 14:25 | Root cause identified: missing DB index        | @engineer_b   |
| 14:30 | Hotfix deployed: index recreated               | @engineer_a   |
| 14:35 | Error rate returned to normal                  | Monitoring    |
| 14:45 | Incident resolved, monitoring continues        | @engineer_a   |
| 15:00 | All-clear communicated to stakeholders         | @eng_manager  |

---

## Root Cause

[Detailed technical explanation of what caused the incident]

### Contributing Factors

1. [Factor 1: e.g., migration testing only used small datasets]
2. [Factor 2: e.g., no automated index verification in CI]
3. [Factor 3: e.g., alerting threshold too high, delayed detection]

---

## Impact Assessment

| Metric                    | Value                          |
|---------------------------|--------------------------------|
| Duration                  | 45 minutes                     |
| Users affected            | ~2,500 (15% of DAU)           |
| Failed requests           | 12,340                         |
| Revenue impact            | $X,XXX estimated               |
| SLA breach                | Yes/No (99.9% target: X.XX%)  |
| Data loss                 | None                           |

---

## What Went Well

- [Alert fired within 5 minutes of issue starting]
- [On-call responded within 2 minutes]
- [Root cause identified quickly — good observability]
- [Clear communication throughout]

## What Went Poorly

- [Detection was slower than desired (5 min vs 1 min target)]
- [Runbook did not cover this specific scenario]
- [Rollback was not attempted — could have been faster]
- [Status page update was delayed by 10 minutes]

## Where We Got Lucky

- [The issue happened during business hours, not at 3 AM]
- [A senior engineer was available to help debug]

---

## Action Items

| Priority | Action                                          | Owner         | Due Date   | Status   |
|----------|-------------------------------------------------|---------------|------------|----------|
| P0       | Add automated index verification to CI          | @engineer_b   | 2026-03-01 | TODO     |
| P1       | Test all migrations against prod-scale data     | @engineer_a   | 2026-03-08 | TODO     |
| P1       | Reduce error rate alert threshold to 5%         | @sre_team     | 2026-02-28 | TODO     |
| P2       | Add rollback step to deployment runbook         | @team_lead    | 2026-03-15 | TODO     |
| P2       | Create runbook for database performance issues  | @engineer_b   | 2026-03-15 | TODO     |
| P3       | Improve status page update automation           | @platform     | 2026-03-30 | TODO     |

---

## Lessons Learned

1. **[Key lesson]:** [Explanation and how it changes our practices]
2. **[Key lesson]:** [Explanation and how it changes our practices]

---

## Review & Sign-off

- [ ] Reviewed by Team Lead: @[name] — [date]
- [ ] Reviewed by Engineering Manager: @[name] — [date]
- [ ] Action items tracked in [Jira/Linear/GitHub Issues]
- [ ] Shared with engineering team: [date]
```

#### Post-Mortem Best Practices

1. **Blameless culture** — Focus on systems, not individuals. Use "the deploy" not "John's deploy"
2. **Complete within deadline** — P0: 48h, P1: 1 week
3. **Review meeting** — Schedule 30-60 min review with all responders + stakeholders
4. **Action item tracking** — Every action item gets an owner and a due date
5. **Share broadly** — Post-mortems are shared with the entire engineering org
6. **Follow up** — Track action item completion in weekly SRE review
7. **Metric trends** — Track incident frequency, MTTR, MTTD over time

### 6. Incident Response Tools Checklist

| Category          | Tool                        | Purpose                           |
|-------------------|-----------------------------|-----------------------------------|
| Alerting          | PagerDuty / Opsgenie        | On-call rotation, escalation      |
| Communication     | Slack (dedicated channel)   | Real-time coordination            |
| Status Page       | Statuspage.io / Cachet      | Customer-facing status            |
| Video             | Zoom / Google Meet          | War room for P0/P1                |
| Documentation     | Notion / Confluence         | Post-mortem storage               |
| Monitoring        | Grafana / Datadog           | Dashboards, metrics               |
| Logging           | ELK / Loki / CloudWatch     | Log aggregation & search          |
| Runbooks          | GitHub Wiki / Notion        | Step-by-step procedures           |
| Ticketing         | Jira / Linear / GitHub      | Action item tracking              |

---

## Output Format

Provide:
1. Complete severity classification guide with decision tree
2. Escalation matrix with contact templates
3. All communication templates (copy-paste ready)
4. RCA investigation checklist
5. Post-mortem template (Markdown, ready to use)
6. Incident commander checklist

---

## Tags

`incident-response` · `runbook` · `on-call` · `post-mortem` · `rca` · `sre` · `severity` · `escalation` · `communication` · `blameless`
