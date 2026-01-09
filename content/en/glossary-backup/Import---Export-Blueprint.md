---
title: "Import / Export Blueprint"
translationKey: "import-export-blueprint"
description: "Import / Export Blueprint saves automation/chatbot logic as a file (JSON/YAML) for sharing, backup, migration, and version control across platforms and environments."
keywords: ["automation blueprint", "chatbot blueprint", "JSON", "YAML", "workflow migration"]
category: "AI Chatbot & Automation"
type: "glossary"
date: 2025-12-05
lastmod: 2025-12-05
draft: false
---
## Definition

<strong>Import / Export Blueprint</strong>is the process of saving the entire logic, configuration, and structure of an automation scenario or chatbot (including all settings, modules, flows, and logic) as a standardized file—commonly in JSON or YAML format. This enables users to share, back up, migrate, or move these blueprints between different accounts, environments, or platforms.

- <strong>Sharing:</strong>Distribute sophisticated automations or chatbot flows to other users, teams, or the community.
- <strong>Backup:</strong>Securely save the logic and configuration of critical automations to prevent data loss.
- <strong>Migration:</strong>Move automations or chatbots between environments (such as development, staging, and production) or across accounts.
- <strong>Version Control:</strong>Track changes to automation flows over time and revert to previous versions as necessary.
- <strong>Collaboration:</strong>Easily collaborate on process design, review, and deployment by exchanging blueprints.

Blueprint import/export preserves core logic, configuration, and metadata (when supported), and reinstates them in compatible environments with minimal manual effort.

## 1. What is Import / Export Blueprint?

Import / Export Blueprint is a core feature of many automation and AI chatbot platforms. It allows users to save the entire definition of a workflow, scenario, or bot—including all settings, modules, and logic—into a blueprint file. This file, typically in JSON or YAML, is a portable, structured representation of the automation logic.

### Utility

- <strong>Collaboration</strong>: Teams develop, review, and deploy automation collaboratively by exchanging blueprints.
- <strong>Versioning</strong>: Store blueprints in source control systems (like Git) for change tracking.
- <strong>Risk Mitigation</strong>: Regular blueprint exports serve as backups and disaster recovery points.
- <strong>Migration</strong>: Move automations between environments with consistent configuration.

### Industry Examples

- [Make.com: Export and Import Blueprints (YouTube tutorial)](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- [Microsoft Azure: Import and Export Blueprints with PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- [Blueprint Help Center: Migrate - Import/Export (RPA platforms)](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)

## 2. How is Import / Export Blueprint Used?

### 2.1 Exporting a Blueprint

Exporting a blueprint saves the current state of a workflow, bot, or automation as a file. Methods include:

- <strong>User Interface (UI):</strong>Most platforms provide an "Export" button or menu item.
- <strong>Command-Line Interface (CLI):</strong>Advanced users can use CLI tools or scripts, e.g., PowerShell on Azure.

<strong>File Formats:</strong>- <strong>JSON:</strong>Most common, readable, and widely supported.
- <strong>YAML:</strong>Used in some environments for its readability, especially in configuration-heavy setups.

#### Example: Make.com

1. Open the scenario editor.
2. Click the three dots in the toolbar.
3. Select "Export Blueprint" to download a `.json` file.

#### Example: Azure Blueprints (PowerShell)

```powershell
$bpDefinition = Get-AzBlueprint -SubscriptionId '{subId}' -Name 'MyBlueprint' -Version '1.1'
Export-AzBlueprintWithArtifact -Blueprint $bpDefinition -OutputPath 'C:\Blueprints'
```

#### Example: RPA Platforms (Blueprint, UiPath, Blue Prism, Automation Anywhere)

Instance administrators can configure export settings for each platform, enabling or disabling export features as needed. For specific instructions, see [Blueprint Help Center: Migrate - Import/Export](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export).

### 2.2 Importing a Blueprint

Importing a blueprint recreates a workflow, automation, or bot in a new environment or account by uploading the blueprint file.

- <strong>UI-based Import:</strong>Most platforms provide an "Import Blueprint" option for uploading JSON/YAML files.
- <strong>CLI-based Import:</strong>Advanced users can use CLI tools, specifying the file path and target environment.

#### Example: Make.com

1. Open the scenario editor.
2. Click the three dots in the toolbar.
3. Select "Import Blueprint," choose the `.json` file, and click "Save."
4. Update integrations or connections as prompted.

#### Example: Azure Blueprints (PowerShell)

```powershell
Import-AzBlueprintWithArtifact -Name 'MyBlueprint' -ManagementGroupId 'DevMG' -InputPath 'C:\Blueprints\MyBlueprint'
```

#### Example: RPA Platforms

Enable or disable import options per platform (e.g., Automation Anywhere, Blue Prism, UiPath) through the instance administration panel ([detailed guide](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)).

<strong>Post-import actions:</strong>- Reconnect integrations or accounts (e.g., APIs, SaaS connectors).
- Update environment-specific variables, endpoints, or credentials.

## 3. Blueprint File Structure and Format

### 3.1 General Structure

Blueprint files encapsulate:

- <strong>Metadata:</strong>Name, description, version, author, and creation date.
- <strong>Modules/Steps:</strong>Sequence of actions or nodes (e.g., triggers, conditions, API calls).
- <strong>Variables/Parameters:</strong>Inputs, outputs, environment variables, mapped fields.
- <strong>Connections:</strong>Integration points (API keys, credentials—usually not exported for security).
- <strong>Artifacts:</strong>Azure Blueprints may reference additional artifact files in an `artifacts` folder.

### 3.2 Folder/File Hierarchy (Azure Blueprints Example)

```
MyBlueprint/
  blueprint.json           # Main blueprint definition
  artifacts/               # Folder for all artifact files
    artifact1.json
    artifact2.json
```
See: [Azure Official Docs: Import and Export Blueprints](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)

### 3.3 Format Requirements

- <strong>JSON/YAML Syntax:</strong>Must be valid and well-formed.
- <strong>Naming Conventions:</strong>Main file often named `blueprint.json`, artifacts in `artifacts/`.
- <strong>Sensitive Data:</strong>Credentials are rarely included; reconnect after import.

### 3.4 Version Compatibility

- Ensure exported blueprints are compatible with the platform version.
- Some platforms allow backward compatibility, but deprecated features may not work.
- [Azure Blueprints Deprecation](https://learn.microsoft.com/en-us/azure/governance/blueprints/deprecated) notice—migrate to Template Specs and Deployment Stacks.

## 4. Use Cases and Examples

### 4.1 Sharing Automation Templates

Teams export blueprints to share proven flows, accelerating onboarding and standardizing processes.  
<strong>Example:</strong>A solutions architect exports a data processing blueprint for other departments to customize.

### 4.2 Migrating Between Environments

Move automations from development to staging or production by exporting/importing blueprints.  
<strong>Example:</strong>A validated chatbot is exported from dev and imported into production for reliable deployment.

### 4.3 Backing Up Mission-Critical Automations

Regular blueprint exports serve as backups, allowing rapid restoration in case of issues.  
<strong>Example:</strong>Before major updates, administrators export blueprints to roll back if necessary.

### 4.4 Version Control and CI/CD

Treating blueprints as code enables version control, collaborative development, code review, automated testing, and CI/CD pipelines.  
<strong>Example:</strong>DevOps teams store blueprint JSON files in Git, using pull requests and automated tests before deployment.

### 4.5 Vendor or Platform Changes

Blueprint files facilitate migration between platforms, when the target supports the format or provides import tools.  
<strong>Example:</strong>Exporting bots from UiPath and importing into an upgraded environment via built-in settings.

For a comprehensive migration guide:  
[Switching Automation Platforms: Complete Data Export and Import Guide | Autonoly](https://www.autonoly.com/blog/68a2aa89d4fe118dae2a444b/switching-automation-platforms-complete-data-export-and-import-guide)

## 5. Managing Blueprints: Best Practices

- <strong>Validate Before Import:</strong>Use JSON/YAML linters to ensure files are valid.
- <strong>Check Dependencies:</strong>Ensure referenced resources, connections, or artifacts exist in the target environment.
- <strong>Sensitive Data:</strong>Never store credentials or secrets in blueprint files.
- <strong>Track Versions:</strong>Use version info in metadata and filenames.
- <strong>Automate Backups:</strong>Schedule regular exports.
- <strong>Use Source Control:</strong>Store blueprints in Git or other VCS for collaboration and auditability.
- <strong>Stay Current:</strong>Review platform documentation for updates, deprecations, and changes in import/export features.

## 6. Common Errors and Troubleshooting

### 6.1 Import Failures

- <strong>Invalid File Format:</strong>Use a linter to check syntax.
- <strong>Missing Dependencies:</strong>All modules/resources must be available.
- <strong>Version Incompatibility:</strong>Ensure file matches platform version requirements.
- <strong>Locked Blueprints:</strong>Some platforms prevent overwriting checked-out blueprints.
- <strong>Browser Support:</strong>Some browsers may not support import/export features.

<strong>Troubleshooting Steps:</strong>1. Validate file syntax.
2. Review documentation for format/version requirements.
3. Ensure all referenced resources exist.
4. Avoid importing into locked or checked-out blueprints.
5. Use recommended browsers or CLI tools.

### 6.2 Post-Import Issues

- <strong>Disconnected Integrations:</strong>Reconnect all external accounts/APIs.
- <strong>Environment-Specific Settings:</strong>Update variables and configuration as needed.
- <strong>Design Errors:</strong>Address missing resources or errors flagged by the platform.

## 7. Platforms Supporting Import / Export Blueprint

### 7.1 Make.com

- <strong>Format:</strong>JSON
- <strong>Import/Export:</strong>Via scenario editor toolbar
- <strong>Tutorial:</strong>[YouTube: Export and Import Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- <strong>Community:</strong>[Make Community: Importing JSON Blueprint](https://community.make.com/t/importing-json-blueprint/88348)

### 7.2 Azure Blueprints

- <strong>Format:</strong>JSON with artifact subfolders
- <strong>Import/Export:</strong>PowerShell (`Export-AzBlueprintWithArtifact`, `Import-AzBlueprintWithArtifact`)
- <strong>Docs:</strong>[Import/Export Blueprints with PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- <strong>Deprecation:</strong>Migrate to [Template Specs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/template-specs) and [Deployment Stacks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks).

### 7.3 BMC Cloud Lifecycle Management

- <strong>Format:</strong>JSON
- <strong>Import/Export:</strong>Service Designer workspace
- <strong>Docs:</strong>[Exporting or importing a blueprint](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)

### 7.4 RPA Platforms

- <strong>Blueprint, Automation Anywhere, Blue Prism, UiPath</strong>- <strong>Format:</strong>Platform-specific (often JSON or proprietary)
- <strong>Import/Export:</strong>Managed by instance administrators, with configurable settings ([Blueprint Help Center: Migrate - Import/Export](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export))

## 8. Related Terminology

| Keyword               | Description                                  |
|-----------------------|----------------------------------------------|
| Export blueprint      | The process or command to save a blueprint file. |
| Import blueprint      | The process or command to load a blueprint into a platform. |
| Export import         | General term for transferring files between systems. |
| Exporting importing   | Performing both export and import operations. |
| Managing blueprint    | Practices and tools for handling blueprint files. |
| JSON file             | JavaScript Object Notation file, used for blueprint structure. |
| YAML file             | YAML Ain’t Markup Language file, sometimes used for blueprints. |

## 9. Further Resources and Next Steps

- <strong>Official Documentation:</strong>- [Microsoft Learn: Import and export blueprints with PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
  - [Exporting or importing a blueprint – BMC Documentation](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)
  - [Blueprint Help Center: Migrate - Import/Export](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)
- <strong>Tutorials and Videos:</strong>- [Make.com YouTube: Export and Import Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
  - [Make Community: Importing JSON Blueprint](https://community.make.com/t/importing-json-blueprint/88348)
- <strong>Community and Training:</strong>- [Make Academy](https://academy.make.com)
  - [Make Help Centre](https://www.make.com/en/help)
  - [BMC Communities](https://community.bmc.com/)
- <strong>Best Practices:</strong>- Store blueprint files in source control (e.g., GitHub, GitLab).
  - Integrate blueprint management into CI/CD pipelines.
  - Regularly review platform release notes for changes to import/export features.

## 10. Summary Table

| Aspect                    | Details                                                                                 |
|---------------------------|----------------------------------------------------------------------------------------|
| <strong>Purpose</strong>| Share, back up, migrate, or version-control automation/chatbot flows                   |
| <strong>File Types</strong>| JSON (primary), YAML (occasionally)                                                    |
| <strong>How to Export</strong>| UI action or CLI command                                                               |
| <strong>How to Import</strong>| UI action or CLI command                                                               |
| <strong>Common Use Cases</strong>| Team sharing, environment migration, backup, version control, platform migration       |
| <strong>Platform Examples</strong>| Make.com, Azure Blueprints, BMC CLM, RPA tools                                         |
| <strong>Troubleshooting</strong>| Check file format, dependencies, platform version compatibility                        |
| <strong>Best Practices</strong>| Validate, back up, use source control, update integrations after import                |
| <strong>Further Reading</strong>| See documentation and community links above                                            |

## 11. Frequently Asked Questions

<strong>Q: Can I use a blueprint file created in one platform on another?</strong>A: Most blueprint files are platform-specific. Some platforms may provide conversion tools or compatible formats, but always check documentation before importing across systems.

<strong>Q: Does exporting a blueprint include my API keys and passwords?</strong>A: No. Sensitive data is typically excluded. Reconnect integrations after import.

<strong>Q: What happens if I import a blueprint that already exists?</strong>A: Platform behavior varies—some create a new version, others overwrite, some require manual merge. Review import warnings and documentation.

<strong>Q: How can I automate blueprint exports for backup?</strong>A: Use CLI tools or APIs to script exports, storing files securely or in version control.

## 12. See Also

- [Infrastructure as Code (IaC)](https://learn.microsoft.com/en-us/azure/governance/blueprints/concepts/lifecycle)
- [Source Control Fundamentals](https://docs.github.com/en/get-started/quickstart/hello-world)
- [CI/CD with Automation Platforms](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-cicd)

### References & Tutorials

- [Make.com YouTube: Export and Import Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- [Blueprint Help Center: Migrate - Import/Export](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)
- [Switching Automation Platforms: Complete Data Export and Import Guide | Autonoly](https://www.autonoly.com/blog/68a2aa89d4fe118dae2a444b/switching-automation-platforms-complete-data-export-and-import-guide)
- [Azure Blueprints Documentation](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- [BMC Documentation: Exporting or importing a blueprint](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)

This glossary entry delivers a comprehensive and deeply detailed overview of Import / Export Blueprint, with authoritative references, best practices, technical file structure, and platform-specific instructions. For further learning, consult the documentation and community resources linked above.
