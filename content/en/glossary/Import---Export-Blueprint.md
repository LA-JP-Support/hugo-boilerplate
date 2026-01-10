---
title: "Import / Export Blueprint"
translationKey: "import-export-blueprint"
description: "A file format that saves your automation or chatbot setup so you can back it up, share it with others, or move it between different systems."
keywords: ["automation blueprint", "chatbot blueprint", "JSON", "YAML", "workflow migration"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-18
lastmod: 2025-12-18
draft: false
---

## What is Import / Export Blueprint?

Import / Export Blueprint is the process of saving the entire logic, configuration, and structure of an automation scenario or chatbot (including all settings, modules, flows, and logic) as a standardized file—commonly in JSON or YAML format. This enables users to share, back up, migrate, or move these blueprints between different accounts, environments, or platforms.

**Key Uses:**-**Sharing**– Distribute sophisticated automations or chatbot flows to other users, teams, or community
- **Backup**– Securely save logic and configuration of critical automations to prevent data loss
- **Migration**– Move automations or chatbots between environments (development, staging, production) or accounts
- **Version Control**– Track changes to automation flows over time and revert to previous versions
- **Collaboration**– Easily collaborate on process design, review, and deployment by exchanging blueprints

Blueprint import/export preserves core logic, configuration, and metadata, reinstating them in compatible environments with minimal manual effort.

## How It Works

### Exporting a Blueprint

Exporting saves current state of workflow, bot, or automation as file. Methods include:

**User Interface (UI):**Most platforms provide "Export" button or menu item.**Command-Line Interface (CLI):**Advanced users can use CLI tools or scripts.**File Formats:**-**JSON**– Most common, readable, widely supported
- **YAML**– Used in some environments for readability

### Importing a Blueprint

Importing recreates workflow, automation, or bot in new environment or account by uploading blueprint file.

**UI-based Import:**Most platforms provide "Import Blueprint" option for uploading JSON/YAML files.**CLI-based Import:**Advanced users can use CLI tools, specifying file path and target environment.**Post-import Actions:**- Reconnect integrations or accounts (APIs, SaaS connectors)
- Update environment-specific variables, endpoints, or credentials

## Platform Examples

### Make.com

**Export:**1. Open scenario editor
2. Click three dots in toolbar
3. Select "Export Blueprint" to download `.json` file

**Import:**1. Open scenario editor
2. Click three dots in toolbar
3. Select "Import Blueprint," choose `.json` file, click "Save"
4. Update integrations or connections as prompted

### Azure Blueprints

**Export (PowerShell):**```powershell
$bpDefinition = Get-AzBlueprint -SubscriptionId '{subId}' -Name 'MyBlueprint' -Version '1.1'
Export-AzBlueprintWithArtifact -Blueprint $bpDefinition -OutputPath 'C:\Blueprints'
```**Import (PowerShell):**```powershell
Import-AzBlueprintWithArtifact -Name 'MyBlueprint' -ManagementGroupId 'DevMG' -InputPath 'C:\Blueprints\MyBlueprint'
```**Note:**Azure Blueprints deprecated; migrate to Template Specs and Deployment Stacks.

### RPA Platforms

**Blueprint, Automation Anywhere, Blue Prism, UiPath:**Enable or disable import/export options per platform through instance administration panel.

## Blueprint File Structure

### General Structure

Blueprint files encapsulate:

- **Metadata**– Name, description, version, author, creation date
- **Modules/Steps**– Sequence of actions or nodes
- **Variables/Parameters**– Inputs, outputs, environment variables, mapped fields
- **Connections**– Integration points (API keys, credentials—usually not exported for security)
- **Artifacts**– Additional artifact files (Azure Blueprints)

### Folder Hierarchy (Azure Example)

```
MyBlueprint/
  blueprint.json           # Main blueprint definition
  artifacts/               # Folder for all artifact files
    artifact1.json
    artifact2.json
```

### Format Requirements

- **JSON/YAML Syntax**– Must be valid and well-formed
- **Naming Conventions**– Main file often named `blueprint.json`, artifacts in `artifacts/`
- **Sensitive Data**– Credentials rarely included; reconnect after import
- **Version Compatibility**– Ensure exported blueprints compatible with platform version

## Use Cases

**Sharing Automation Templates:**Teams export blueprints to share proven flows, accelerating onboarding and standardizing processes.**Migrating Between Environments:**Move automations from development to staging or production by exporting/importing blueprints.**Backing Up Mission-Critical Automations:**Regular blueprint exports serve as backups, allowing rapid restoration in case of issues.**Version Control and CI/CD:**Treating blueprints as code enables version control, collaborative development, code review, automated testing, and CI/CD pipelines.**Vendor or Platform Changes:**Blueprint files facilitate migration between platforms when target supports format or provides import tools.

## Best Practices

**Validate Before Import:**Use JSON/YAML linters to ensure files are valid.**Check Dependencies:**Ensure referenced resources, connections, or artifacts exist in target environment.**Sensitive Data:**Never store credentials or secrets in blueprint files.**Track Versions:**Use version info in metadata and filenames.**Automate Backups:**Schedule regular exports.**Use Source Control:**Store blueprints in Git or other VCS for collaboration and auditability.**Stay Current:**Review platform documentation for updates, deprecations, and changes.

## Common Errors and Troubleshooting

**Import Failures:**-**Invalid File Format**– Use linter to check syntax
- **Missing Dependencies**– All modules/resources must be available
- **Version Incompatibility**– Ensure file matches platform version requirements
- **Locked Blueprints**– Some platforms prevent overwriting checked-out blueprints
- **Browser Support**– Some browsers may not support import/export features**Post-Import Issues:**-**Disconnected Integrations**– Reconnect all external accounts/APIs
- **Environment-Specific Settings**– Update variables and configuration as needed
- **Design Errors**– Address missing resources or errors flagged by platform

## Platforms Supporting Import / Export

**Make.com:**- Format: JSON
- Import/Export: Via scenario editor toolbar

**Azure Blueprints:**- Format: JSON with artifact subfolders
- Import/Export: PowerShell
- Deprecation: Migrate to Template Specs and Deployment Stacks

**BMC Cloud Lifecycle Management:**- Format: JSON
- Import/Export: Service Designer workspace

**RPA Platforms:**- Blueprint, Automation Anywhere, Blue Prism, UiPath
- Format: Platform-specific (often JSON or proprietary)
- Import/Export: Managed by instance administrators

## Related Terminology

| Keyword | Description |
|---------|-------------|
| Export blueprint | Process or command to save blueprint file |
| Import blueprint | Process or command to load blueprint into platform |
| Export import | General term for transferring files between systems |
| Managing blueprint | Practices and tools for handling blueprint files |
| JSON file | JavaScript Object Notation file, used for blueprint structure |
| YAML file | YAML Ain't Markup Language file, sometimes used for blueprints |

## Frequently Asked Questions

**Q: Can I use a blueprint file created in one platform on another?**A: Most blueprint files are platform-specific. Some platforms may provide conversion tools or compatible formats, but always check documentation.**Q: Does exporting a blueprint include my API keys and passwords?**A: No. Sensitive data is typically excluded. Reconnect integrations after import.**Q: What happens if I import a blueprint that already exists?**A: Platform behavior varies—some create new version, others overwrite, some require manual merge. Review import warnings and documentation.**Q: How can I automate blueprint exports for backup?**A: Use CLI tools or APIs to script exports, storing files securely or in version control.

## References


1. Make.com. (n.d.). Export and Import Blueprints. YouTube.

2. Make Community. (n.d.). Importing JSON Blueprint. Make Community Forum.

3. Make Academy. Online Learning Platform. URL: https://academy.make.com

4. Make Help Centre. Support Resource. URL: https://www.make.com/en/help

5. Microsoft. (n.d.). Import and Export Blueprints with PowerShell. Microsoft Learn.

6. Microsoft. (n.d.). Azure Blueprints Deprecated. Microsoft Learn.

7. Microsoft. (n.d.). Template Specs. Microsoft Learn.

8. Microsoft. (n.d.). Deployment Stacks. Microsoft Learn.

9. Microsoft. (n.d.). Azure Blueprints Lifecycle. Microsoft Learn.

10. BMC. (n.d.). Exporting or Importing a Blueprint. BMC Documentation.

11. Blueprint Help Center. (n.d.). Migrate - Import/Export. Blueprint Help Docs.

12. Autonoly. (n.d.). Switching Automation Platforms Guide. Autonoly Blog.

13. BMC Communities. Online Community Platform. URL: https://community.bmc.com/

14. GitHub. (n.d.). Source Control Fundamentals. GitHub Docs.

15. Microsoft. (n.d.). CI/CD with Azure DevOps. Microsoft Learn.
