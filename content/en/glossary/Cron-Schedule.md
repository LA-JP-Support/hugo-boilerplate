---
title: Cron Schedule
date: 2025-12-19
lastmod: 2026-04-02
translationKey: cron-schedule
description: A time-specification method in Unix/Linux for scheduling automatic task execution. Enables precise timing like "backup every day at 2 AM."
keywords:
- Cron schedule
- Task automation
- Crontab
- Scheduling
- Unix/Linux
category: Cloud & Infrastructure
type: glossary
draft: false
url: /en/glossary/cron-schedule/
---

## What is Cron Schedule?

**Cron schedule is a system for specifying "execute this command at this date and time" on servers and cloud systems.** It automates repetitive tasks like backups, report generation, and data synchronization without manual intervention.

> **In a nutshell:** The Linux version of Windows "Task Scheduler." It supports complex time specifications and is a foundational business automation tool.

**Key points:**

- **What it does:** Auto-execute scripts and commands at specified times
- **Why it's needed:** Address labor shortages, eliminate human error, enable 24/7 automated operation
- **Format:** Five numbers (minute, hour, day, month, day-of-week) plus a command

## Why it matters

Daily 2 AM backups, weekly Monday sales reports, monthly first-day invoicing—all routine work can be fully automated, freeing people for other tasks. Compared to manual work, human error like "I forgot" or "wrong time" becomes zero.

In the cloud era, this is increasingly important. AWS Lambda, Google Cloud Functions, and others offer cron-compatible scheduling, making it enterprise standard.

## How it works

Cron runs a "cron daemon" in the background that checks system time every minute. When the specified time arrives, it automatically executes the command.

**Basic format:**
```
minute hour day month day-of-week command
```

Examples:
- `0 2 * * *` = Every day at 2 AM (minute: 0, hour: 2, day: all, month: all, day-of-week: all)
- `0 9 * * 1-5` = Weekdays at 9 AM (day-of-week: 1-5 is Monday-Friday)
- `*/15 * * * *` = Every 15 minutes

## Practical examples

**Backup script:**
```
0 2 * * * /home/user/backup.sh
```
Execute backup script daily at 2 AM.

**Report generation:**
```
0 8 1 * * /usr/local/bin/generate_report.sh
```
Auto-generate sales report first of month at 8 AM.

**Health check:**
```
*/5 * * * * /opt/healthcheck.sh
```
Run server health check every 5 minutes.

## How to set it up

On Linux/Mac terminal, edit the cron registration file (crontab):

```bash
crontab -e
```

A text editor opens where you write commands in the format above. Save and exit to auto-register.

```bash
crontab -l  # Show registered cron jobs
crontab -r  # Delete all
```

## Benefits and considerations

**Benefits:** Complete automation, 24/7 operation, improved staff efficiency.

**Considerations:** Failures don't auto-notify (configure email forwarding for notifications). If the server stops, tasks don't execute. Critical tasks need redundancy and monitoring.

## Related terms

- **[Task Automation](Task-Automation.md)** — General concept of automation including cron
- **[Script](Script.md)** — The program to execute
- **[Backup](Backup.md)** — Often auto-executed with cron
- **[Job Scheduler](Job-Scheduler.md)** — Multi-step task management
- **[DevOps](DevOps.md)** — System automation with cron is foundational

## Frequently asked questions

**Q: What are the exact ranges for the five numbers?**
A: Minute (0-59), Hour (0-23), Day (1-31), Month (1-12), Day-of-week (0-6, Sunday=0).

**Q: How do I get notified of failures?**
A: Crontab results are logged by default only. Configure email sending for failure notifications, or use external cron monitoring tools like Cronitor.

**Q: Does it work with cloud services?**
A: AWS Lambda, Google Cloud Functions, Azure Functions all support cron-compatible trigger settings.

**System Maintenance:** Backups, log rotation, removing temp files, updating software.  
**Reporting:** Automated generation and delivery of daily/weekly/monthly reports.  
**Monitoring:** Scheduled health checks, disk usage alerts, alerting on system anomalies.  
**AI & Automation:** Triggering model retraining, data pipeline execution, automated chatbots, or API polling.  
**Cloud & DevOps:** Deploying builds, syncing microservices, running serverless functions, refreshing data in cloud platforms.

### Common Environments Supporting Cron Schedules

**Traditional Systems:** Unix/Linux servers, BSD, macOS, WSL on Windows.  
**Cloud Providers:** AWS Lambda scheduled events, Google Cloud Scheduler, Azure Logic Apps, Cloudflare Workers.  
**SaaS Automation:** Cloudflare Workers, RobilityAI, Zapier, GitHub Actions.  
**CI/CD & Orchestration:** Jenkins, GitLab CI, Argo Workflows, RobilityAI.

## Cron Schedule Syntax: The Building Blocks

Cron schedules are defined using cron expressions—strings of fields separated by spaces, each representing a time unit.

### Standard (5-field) Cron Syntax

```
* * * * *  <command or script>
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, Sunday=0 or 7)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Example Table

| Cron Schedule | Meaning |
|---------------|---------|
| `0 9 * * 1` | At 9:00 AM every Monday |
| `*/15 9-17 * * 1-5` | Every 15 mins, 9AM–5PM, Monday–Friday |
| `0 0 * * *` | Every day at midnight |
| `0 0 1 * *` | 1st of every month at midnight |
| `* * * * *` | Every minute |

### Extended Cron Syntax

Some platforms (Quartz, Cloudflare Workers, RobilityAI) support extended cron syntax, including seconds and year fields.

| Field | Position | Allowed Values | Special Characters |
|-------|----------|----------------|-------------------|
| Seconds | 1 | 0–59 | `* , - /` |
| Minutes | 2 | 0–59 | `* , - /` |
| Hours | 3 | 0–23 | `* , - /` |
| Day of Month | 4 | 1–31 | `* , - / ? L W` |
| Month | 5 | 1–12 or JAN–DEC | `* , - /` |
| Day of Week | 6 | 0–6 or SUN–SAT | `* , - / ? L #` |
| Year (optional) | 7 | 1970–2099 | `* , - /` |

## Special Characters and Operators in Cron Expressions

| Character | Example | Meaning |
|-----------|---------|---------|
| `*` | `* * * * *` | Every value |
| `,` | `0 9,17 * * *` | List (9 AM and 5 PM) |
| `-` | `0 9-17 * * *` | Range (9 AM to 5 PM) |
| `/` | `*/15 * * * *` | Step (every 15 minutes) |
| `?` | `0 0 1 ? * *` | No specific value (DOW/DOM) |
| `L` | `0 0 L * *` | Last day of period |
| `W` | `0 0 15W * *` | Nearest weekday to 15th |
| `#` | `0 0 * * 1#2` | Nth weekday (second Monday) |

## Common Cron Schedule Examples

| Expression | Meaning |
|------------|---------|
| `0 0 * * *` | Every day at midnight |
| `0 12 * * MON-FRI` | Every weekday at noon |
| `*/10 * * * *` | Every 10 minutes |
| `0 6,18 * * *` | At 6 AM and 6 PM daily |
| `0 8 1 */3 *` | 8 AM on the 1st, every 3rd month (quarterly) |
| `0 0 1 1 *` | At midnight on January 1st |
| `@hourly` | Every hour (special string) |
| `@daily`/`@midnight` | Every day at midnight |
| `@weekly` | Every week at midnight on Sunday |
| `@monthly` | First day of the month at midnight |
| `@yearly`/`@annually` | Once a year, midnight, January 1st |
| `@reboot` | At system startup |
| `0 15 10 ? * 2#1` | 10:15 AM, first Monday of every month (Quartz) |
| `0 0 8 15W * ?` | 8 AM on nearest weekday to the 15th |
| `0 0 23 L * ?` | 11 PM on the last day of every month |
| `0 0/5 9-17 * * MON-FRI` | Every 5 minutes, 9 AM–5 PM, Monday–Friday |

## How Cron Schedules Work (Under the Hood)

The cron daemon (`crond`) runs continuously in the background, checking all loaded crontabs every minute.

**Execution Process:**

1. The daemon parses each crontab entry and its associated schedule
2. At the start of each minute, it checks whether any entry matches the current time
3. If a match is found, the associated command is executed as the user who owns the crontab
4. Advanced implementations (like Vixie cron) optimize this with event lists and next-run computation

## Cron Schedule Use Cases

### System Administration
**Nightly Backups:** `0 2 * * *`  
**Weekly Log Rotation:** `0 0 * * 0`  
**Daily Temp Cleanup:** `0 3 * * *`

### AI & Automation
**Retrain ML Models:** `0 1 * * 0`  
**Scheduled API Polling:** `*/30 * * * *`  
**Automated Chatbot Processing:** Custom schedules for user engagement flows.

### DevOps & Cloud
**Nightly Deployments:** `0 0 * * *`  
**Data Synchronization:** `0 */6 * * *`  
**Serverless Functions:** Cloudflare Cron Triggers Example:

```toml
[triggers]
crons = ["*/15 * * * *"]
```

### Monitoring & Alerting
**Health Checks:** `*/5 * * * *`  
**Daily Reports:** `0 7 * * *`  
**Resource Alerts:** Custom schedules for system thresholds.

### Business Operations
**Email Reports:** `0 8 * * 1`  
**Marketing Campaigns:** `0 10 * * 5`  
**Billing Reminders:** Monthly or weekly schedules.

## Setting Up and Managing Cron Schedules

### 1. Editing the Crontab

To create or edit a cron schedule, use:

```bash
crontab -e
```

This opens your user's crontab in your default editor (often nano or vim).

### 2. Adding a Cron Job

Example: Run a backup script every day at 2 AM

```
0 2 * * * /home/user/scripts/backup.sh
```

**Pro Tip:** Always use absolute paths to avoid path resolution errors.

### 3. Listing Existing Cron Jobs

```bash
crontab -l
```

### 4. Removing All Cron Jobs

```bash
crontab -r
```

Or safer, with confirmation:

```bash
crontab -i
```

### 5. System vs. User Crontab

**System crontab:** `/etc/crontab` (root access, includes a user field)  
**User crontab:** Per-user schedule, no user field

### 6. Cloud & SaaS Platforms

Modern cloud and SaaS platforms provide their own UIs or config files for defining cron schedules:

**Cloudflare Workers:** Use the `wrangler.toml` file's `[triggers]` section.  
**RobilityAI:** Define cron-based triggers in the project management scheduler.

## Advanced Scheduling: Edge Cases & Operators

Advanced cron features enable highly flexible schedules:

- **Nth Day of Week:** `1#2` (second Monday)
- **Last Day/Weekday:** `L`, `6L` (last Friday)
- **Nearest Weekday:** `15W` (weekday closest to 15th)
- **Step Values:** `0/10` (every 10 minutes)
- **Year Field:** Available in Quartz, Cloudflare, RobilityAI, not classic cron

**Platform Support:** Always check platform documentation for support of advanced syntax.

## Limitations and Platform Differences

**Minimum Interval:** Classic cron's minimum interval is one minute.  
**Missed Runs:** Missed jobs (system down, busy) are not auto-executed; no built-in retry.  
**Notification:** No built-in notification for failures (unless configured via log/email).  
**Environment:** Cron jobs run in a minimal environment—environment variables like `PATH` may differ from your terminal session.  
**Permissions:** Only authorized users can set/edit cron jobs. System-wide jobs require root.

## Security and Best Practices

### Security
- Run jobs with the least possible privilege
- Store scripts and crontabs securely
- Control access using `cron.allow` and `cron.deny`

### Reliability
- Always specify absolute paths for commands and files
- Test scripts manually before scheduling
- Redirect output and errors to log files for troubleshooting
- Prevent overlaps using lock files or job concurrency tools

### Monitoring
- Enable and check system logs: `/var/log/cron`, `/var/log/syslog`
- Use monitoring tools: Cronitor, Healthchecks.io, Cloudflare Cron Events
- Set up alerts for job failures or missed runs

## Troubleshooting Common Cron Schedule Issues

| Problem | Causes & Solutions |
|---------|-------------------|
| **Script runs manually, not in cron** | Missing environment variables, user permissions, not executable |
| **Path errors** | Use absolute paths for files/commands |
| **Job overlap** | Use lock files to prevent concurrency |
| **No output/errors captured** | Redirect output/errors: `... >> /path/log.txt 2>&1` |
| **Cron job not running** | Cron daemon not running, user not in allowed list, incorrect syntax |

## Frequently Asked Questions

**Q: What are the five standard fields in a cron schedule?**  
A: Minute, hour, day of month, month, day of week (in that order).

**Q: How do I schedule a job every weekday at noon?**  
A: `0 12 * * 1-5 <command>`

**Q: Can I use cron schedules in cloud/serverless environments?**  
A: Yes. Platforms like Cloudflare Workers and RobilityAI support cron triggers.

**Q: How do I prevent cron jobs from overlapping?**  
A: Use lock files or tools that manage job concurrency.

**Q: How can I monitor my cron jobs?**  
A: Use external tools (Cronitor, Healthchecks.io), enable logs, or leverage built-in cloud monitoring.

## References

- [Cronitor: Cron Jobs Guide](https://cronitor.io/guides/cron-jobs)
- [Cronitor: Cron Reference](https://cronitor.io/docs/cron-reference)
- [Cronitor: Cron Job Monitoring](https://cronitor.io/cron-job-monitoring)
- [Cronitor: Debugging Cron Jobs](https://cronitor.io/guides/cron-jobs#troubleshooting)
- [Hostinger: Cron Job Tutorial](https://www.hostinger.com/tutorials/cron-job)
- [OSTechNix: A Beginner's Guide to Cron Jobs](https://ostechnix.com/a-beginners-guide-to-cron-jobs/)
- [Splunk: What Are Cron Jobs?](https://www.splunk.com/en_us/blog/learn/cron-jobs.html)
- [Cloudflare Workers: Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/)
- [Cloudflare: Cron Trigger Syntax](https://developers.cloudflare.com/workers/configuration/cron-triggers/#syntax)
- [Cloudflare: View Past Events](https://developers.cloudflare.com/workers/configuration/cron-triggers/#view-past-events)
- [RobilityAI: Cron-based Schedulers](https://docs.robility.ai/docs/robility-manager/project-management/scheduler/cron-based-schedulers/)
- [StackOverflow: How does cron internally schedule jobs?](https://stackoverflow.com/questions/3982957/how-does-cron-internally-schedule-jobs)
- [CodeSignal: Scheduling Tasks with Cron](https://codesignal.com/learn/courses/system-automation-with-shell-scripts/lessons/scheduling-tasks-with-cron)
- [Crontab.guru: Cron Expression Editor](https://crontab.guru/)
- [Crontab Generator](https://crontab-generator.org/)
- [Quartz Scheduler: CronTriggers](https://www.quartz-scheduler.net/documentation/quartz-3.x/tutorial/crontriggers.html)
- [Healthchecks.io](https://healthchecks.io/)
