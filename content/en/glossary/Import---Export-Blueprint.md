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

<strong>Key Uses:</strong>- <strong>Sharing</strong>– Distribute sophisticated automations or chatbot flows to other users, teams, or community
- <strong>Backup</strong>– Securely save logic and configuration of critical automations to prevent data loss
- <strong>Migration</strong>– Move automations or chatbots between environments (development, staging, production) or accounts
- <strong>Version Control</strong>– Track changes to automation flows over time and revert to previous versions
- <strong>Collaboration</strong>– Easily collaborate on process design, review, and deployment by exchanging blueprints

Blueprint import/export preserves core logic, configuration, and metadata, reinstating them in compatible environments with minimal manual effort.

## How It Works

### Exporting a Blueprint

Exporting saves current state of workflow, bot, or automation as file. Methods include:

<strong>User Interface (UI):</strong>Most platforms provide "Export" button or menu item.

<strong>Command-Line Interface (CLI):</strong>Advanced users can use CLI tools or scripts.

<strong>File Formats:</strong>- <strong>JSON</strong>– Most common, readable, widely supported
- <strong>YAML</strong>– Used in some environments for readability

### Importing a Blueprint

Importing recreates workflow, automation, or bot in new environment or account by uploading blueprint file.

<strong>UI-based Import:</strong>Most platforms provide "Import Blueprint" option for uploading JSON/YAML files.

<strong>CLI-based Import:</strong>Advanced users can use CLI tools, specifying file path and target environment.

<strong>Post-import Actions:</strong>- Reconnect integrations or accounts (APIs, SaaS connectors)
- Update environment-specific variables, endpoints, or credentials

## Platform Examples

### Make.com

<strong>Export:</strong>1. Open scenario editor
2. Click three dots in toolbar
3. Select "Export Blueprint" to download `.json` file

<strong>Import:</strong>1. Open scenario editor
2. Click three dots in toolbar
3. Select "Import Blueprint," choose `.json` file, click "Save"
4. Update integrations or connections as prompted

### Azure Blueprints

<strong>Export (PowerShell):</strong>```powershell
$bpDefinition = Get-AzBlueprint -SubscriptionId '{subId}' -Name 'MyBlueprint' -Version '1.1'
Export-AzBlueprintWithArtifact -Blueprint $bpDefinition -OutputPath 'C:\Blueprints'
```

**Import (PowerShell):**```powershell
Import-AzBlueprintWithArtifact -Name 'MyBlueprint' -ManagementGroupId 'DevMG' -InputPath 'C:\Blueprints\MyBlueprint'
```

<strong>Note:</strong>Azure Blueprints deprecated; migrate to Template Specs and Deployment Stacks.

### RPA Platforms

<strong>Blueprint, Automation Anywhere, Blue Prism, UiPath:</strong>Enable or disable import/export options per platform through instance administration panel.

## Blueprint File Structure

### General Structure

Blueprint files encapsulate:

- <strong>Metadata</strong>– Name, description, version, author, creation date
- <strong>Modules/Steps</strong>– Sequence of actions or nodes
- <strong>Variables/Parameters</strong>– Inputs, outputs, environment variables, mapped fields
- <strong>Connections</strong>– Integration points (API keys, credentials—usually not exported for security)
- <strong>Artifacts</strong>– Additional artifact files (Azure Blueprints)

### Folder Hierarchy (Azure Example)

```
MyBlueprint/
  blueprint.json           # Main blueprint definition
  artifacts/               # Folder for all artifact files
    artifact1.json
    artifact2.json
```

### Format Requirements

- <strong>JSON/YAML Syntax</strong>– Must be valid and well-formed
- <strong>Naming Conventions</strong>– Main file often named `blueprint.json`, artifacts in `artifacts/`
- <strong>Sensitive Data</strong>– Credentials rarely included; reconnect after import
- <strong>Version Compatibility</strong>– Ensure exported blueprints compatible with platform version

## Use Cases

<strong>Sharing Automation Templates:</strong>Teams export blueprints to share proven flows, accelerating onboarding and standardizing processes.

<strong>Migrating Between Environments:</strong>Move automations from development to staging or production by exporting/importing blueprints.

<strong>Backing Up Mission-Critical Automations:</strong>Regular blueprint exports serve as backups, allowing rapid restoration in case of issues.

<strong>Version Control and CI/CD:</strong>Treating blueprints as code enables version control, collaborative development, code review, automated testing, and CI/CD pipelines.

<strong>Vendor or Platform Changes:</strong>Blueprint files facilitate migration between platforms when target supports format or provides import tools.

## Best Practices

<strong>Validate Before Import:</strong>Use JSON/YAML linters to ensure files are valid.

<strong>Check Dependencies:</strong>Ensure referenced resources, connections, or artifacts exist in target environment.

<strong>Sensitive Data:</strong>Never store credentials or secrets in blueprint files.

<strong>Track Versions:</strong>Use version info in metadata and filenames.

<strong>Automate Backups:</strong>Schedule regular exports.

<strong>Use Source Control:</strong>Store blueprints in Git or other VCS for collaboration and auditability.

<strong>Stay Current:</strong>Review platform documentation for updates, deprecations, and changes.

## Common Errors and Troubleshooting

<strong>Import Failures:</strong>- <strong>Invalid File Format</strong>– Use linter to check syntax
- <strong>Missing Dependencies</strong>– All modules/resources must be available
- <strong>Version Incompatibility</strong>– Ensure file matches platform version requirements
- <strong>Locked Blueprints</strong>– Some platforms prevent overwriting checked-out blueprints
- <strong>Browser Support</strong>– Some browsers may not support import/export features

<strong>Post-Import Issues:</strong>- <strong>Disconnected Integrations</strong>– Reconnect all external accounts/APIs
- <strong>Environment-Specific Settings</strong>– Update variables and configuration as needed
- <strong>Design Errors</strong>– Address missing resources or errors flagged by platform

## Platforms Supporting Import / Export

<strong>Make.com:</strong>- Format: JSON
- Import/Export: Via scenario editor toolbar

<strong>Azure Blueprints:</strong>- Format: JSON with artifact subfolders
- Import/Export: PowerShell
- Deprecation: Migrate to Template Specs and Deployment Stacks

<strong>BMC Cloud Lifecycle Management:</strong>- Format: JSON
- Import/Export: Service Designer workspace

<strong>RPA Platforms:</strong>- Blueprint, Automation Anywhere, Blue Prism, UiPath
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

<strong>Q: Can I use a blueprint file created in one platform on another?</strong>A: Most blueprint files are platform-specific. Some platforms may provide conversion tools or compatible formats, but always check documentation.

<strong>Q: Does exporting a blueprint include my API keys and passwords?</strong>A: No. Sensitive data is typically excluded. Reconnect integrations after import.

<strong>Q: What happens if I import a blueprint that already exists?</strong>A: Platform behavior varies—some create new version, others overwrite, some require manual merge. Review import warnings and documentation.

<strong>Q: How can I automate blueprint exports for backup?</strong>A: Use CLI tools or APIs to script exports, storing files securely or in version control.

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
