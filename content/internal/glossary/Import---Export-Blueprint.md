+++
title = "Importación / Exportación de Blueprint"
translationKey = "import-export-blueprint"
description = "La Importación / Exportación de Blueprint guarda la lógica de automatización/chatbot como archivo (JSON/YAML) para compartir, respaldar, migrar y controlar versiones entre plataformas y entornos."
keywords = ["blueprint de automatización", "blueprint de chatbot", "JSON", "YAML", "migración de flujos de trabajo"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Import---Export-Blueprint/"

+++
## Definición

**Importación / Exportación de Blueprint**es el proceso de guardar toda la lógica, configuración y estructura de un escenario de automatización o chatbot (incluyendo todos los ajustes, módulos, flujos y lógica) como un archivo estandarizado—comúnmente en formato JSON o YAML. Esto permite a los usuarios compartir, respaldar, migrar o mover estos blueprints entre diferentes cuentas, entornos o plataformas.

- **Compartir:**Distribuya automatizaciones sofisticadas o flujos de chatbot a otros usuarios, equipos o la comunidad.
- **Respaldo:**Guarde de forma segura la lógica y configuración de automatizaciones críticas para prevenir la pérdida de datos.
- **Migración:**Mueva automatizaciones o chatbots entre entornos (como desarrollo, pruebas y producción) o entre cuentas.
- **Control de Versiones:**Haga un seguimiento de los cambios en los flujos de automatización a lo largo del tiempo y revierta a versiones anteriores según sea necesario.
- **Colaboración:**Colabore fácilmente en el diseño, revisión y despliegue de procesos intercambiando blueprints.

La importación/exportación de blueprints preserva la lógica principal, configuración y metadatos (cuando se admite), y los restablece en entornos compatibles con un esfuerzo manual mínimo.

## 1. ¿Qué es la Importación / Exportación de Blueprint?

La Importación / Exportación de Blueprint es una función clave de muchas plataformas de automatización y chatbots de IA. Permite a los usuarios guardar toda la definición de un flujo de trabajo, escenario o bot—including all settings, modules, and logic—en un archivo blueprint. Este archivo, típicamente en JSON o YAML, es una representación portátil y estructurada de la lógica de automatización.

### Utilidad

- **Colaboración**: Los equipos desarrollan, revisan y despliegan automatizaciones colaborando mediante el intercambio de blueprints.
- **Versionado**: Almacene blueprints en sistemas de control de versiones (como Git) para el seguimiento de cambios.
- **Mitigación de Riesgos**: Las exportaciones regulares de blueprints sirven como copias de seguridad y puntos de recuperación ante desastres.
- **Migración**: Mueva automatizaciones entre entornos con configuración consistente.

### Ejemplos en la Industria

- [Make.com: Exportar e Importar Blueprints (tutorial de YouTube)](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- [Microsoft Azure: Importar y Exportar Blueprints con PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- [Centro de Ayuda Blueprint: Migrar - Importar/Exportar (plataformas RPA)](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)

## 2. ¿Cómo se utiliza la Importación / Exportación de Blueprint?

### 2.1 Exportar un Blueprint

Exportar un blueprint guarda el estado actual de un flujo de trabajo, bot o automatización como un archivo. Los métodos incluyen:

- **Interfaz de Usuario (UI):**La mayoría de plataformas ofrecen un botón o elemento de menú "Exportar".
- **Interfaz de Línea de Comando (CLI):**Usuarios avanzados pueden emplear herramientas CLI o scripts, por ejemplo, PowerShell en Azure.

**Formatos de archivo:**- **JSON:**El más común, legible y ampliamente soportado.
- **YAML:**Usado en algunos entornos por su legibilidad, especialmente en configuraciones complejas.

#### Ejemplo: Make.com

1. Abra el editor de escenarios.
2. Haga clic en los tres puntos de la barra de herramientas.
3. Seleccione "Exportar Blueprint" para descargar un archivo `.json`.

#### Ejemplo: Azure Blueprints (PowerShell)

```powershell
$bpDefinition = Get-AzBlueprint -SubscriptionId '{subId}' -Name 'MyBlueprint' -Version '1.1'
Export-AzBlueprintWithArtifact -Blueprint $bpDefinition -OutputPath 'C:\Blueprints'
```

#### Ejemplo: Plataformas RPA (Blueprint, UiPath, Blue Prism, Automation Anywhere)

Los administradores de instancias pueden configurar los ajustes de exportación para cada plataforma, habilitando o deshabilitando funciones de exportación según sea necesario. Para instrucciones específicas, consulte [Centro de Ayuda Blueprint: Migrar - Importar/Exportar](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export).

### 2.2 Importar un Blueprint

Importar un blueprint recrea un flujo de trabajo, automatización o bot en un nuevo entorno o cuenta subiendo el archivo blueprint.

- **Importación basada en UI:**La mayoría de plataformas ofrecen una opción "Importar Blueprint" para subir archivos JSON/YAML.
- **Importación por CLI:**Usuarios avanzados pueden usar herramientas CLI, especificando la ruta del archivo y el entorno destino.

#### Ejemplo: Make.com

1. Abra el editor de escenarios.
2. Haga clic en los tres puntos de la barra de herramientas.
3. Seleccione "Importar Blueprint", elija el archivo `.json` y haga clic en "Guardar".
4. Actualice integraciones o conexiones según se le indique.

#### Ejemplo: Azure Blueprints (PowerShell)

```powershell
Import-AzBlueprintWithArtifact -Name 'MyBlueprint' -ManagementGroupId 'DevMG' -InputPath 'C:\Blueprints\MyBlueprint'
```

#### Ejemplo: Plataformas RPA

Active o desactive las opciones de importación por plataforma (ej. Automation Anywhere, Blue Prism, UiPath) a través del panel de administración de instancias ([guía detallada](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)).

**Acciones posteriores a la importación:**- Reconecte integraciones o cuentas (por ejemplo, APIs, conectores SaaS).
- Actualice variables, endpoints o credenciales específicas del entorno.

## 3. Estructura y Formato del Archivo Blueprint

### 3.1 Estructura General

Los archivos blueprint encapsulan:

- **Metadatos:**Nombre, descripción, versión, autor y fecha de creación.
- **Módulos/Pasos:**Secuencia de acciones o nodos (ej. disparadores, condiciones, llamadas API).
- **Variables/Parámetros:**Entradas, salidas, [variables de entorno](/en/glossary/environment-variables--secrets-/), campos mapeados.
- **Conexiones:**Puntos de integración (claves API, credenciales—normalmente no exportados por seguridad).
- **Artefactos:**Azure Blueprints puede referenciar archivos adicionales en una carpeta `artifacts`.

### 3.2 Jerarquía de Carpetas/Archivos (Ejemplo Azure Blueprints)

```
MyBlueprint/
  blueprint.json           # Definición principal del blueprint
  artifacts/               # Carpeta para todos los archivos de artefactos
    artifact1.json
    artifact2.json
```
Ver: [Documentos Oficiales de Azure: Importar y Exportar Blueprints](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)

### 3.3 Requisitos de Formato

- **Sintaxis JSON/YAML:**Debe ser válida y estar bien formada.
- **Convenciones de Nombres:**El archivo principal suele llamarse `blueprint.json`, artefactos en `artifacts/`.
- **Datos Sensibles:**Rara vez se incluyen credenciales; reconéctelas luego de la importación.

### 3.4 Compatibilidad de Versiones

- Asegúrese de que los blueprints exportados sean compatibles con la versión de la plataforma.
- Algunas plataformas tienen compatibilidad hacia atrás, pero funciones obsoletas pueden no funcionar.
- Aviso de [Deprecación de Azure Blueprints](https://learn.microsoft.com/en-us/azure/governance/blueprints/deprecated)—migre a Template Specs y Deployment Stacks.

## 4. Casos de Uso y Ejemplos

### 4.1 Compartir Plantillas de Automatización

Los equipos exportan blueprints para compartir flujos comprobados, acelerando la incorporación y estandarizando procesos.  
**Ejemplo:**Un arquitecto de soluciones exporta un blueprint de procesamiento de datos para que otros departamentos lo personalicen.

### 4.2 Migración entre Entornos

Mueva automatizaciones de desarrollo a pruebas o producción exportando/importando blueprints.  
**Ejemplo:**Un chatbot validado se exporta desde desarrollo y se importa en producción para un despliegue confiable.

### 4.3 Respaldar Automatizaciones Críticas

Las exportaciones regulares de blueprints sirven como copias de seguridad, permitiendo restaurar rápidamente en caso de problemas.  
**Ejemplo:**Antes de grandes actualizaciones, los administradores exportan blueprints para revertir si es necesario.

### 4.4 Control de Versiones y CI/CD

Tratar los blueprints como código habilita el control de versiones, desarrollo colaborativo, revisión de código, pruebas automatizadas y pipelines CI/CD.  
**Ejemplo:**Equipos DevOps almacenan archivos JSON de blueprints en Git, usando pull requests y tests automáticos antes del despliegue.

### 4.5 Cambios de Proveedor o Plataforma

Los archivos blueprint facilitan la migración entre plataformas, cuando el destino soporta el formato o provee herramientas de importación.  
**Ejemplo:**Exportar bots de UiPath e importarlos en un entorno actualizado vía configuraciones integradas.

Para una guía completa de migración:  
[Cambio de Plataformas de Automatización: Guía Completa de Exportación e Importación de Datos | Autonoly](https://www.autonoly.com/blog/68a2aa89d4fe118dae2a444b/switching-automation-platforms-complete-data-export-and-import-guide)

## 5. Gestión de Blueprints: Mejores Prácticas

- **Validar antes de importar:**Utilice linters de JSON/YAML para garantizar la validez del archivo.
- **Comprobar dependencias:**Asegúrese de que los recursos, conexiones o artefactos referenciados existan en el entorno destino.
- **Datos sensibles:**Nunca almacene credenciales o secretos en archivos blueprint.
- **Rastrear versiones:**Use información de versión en metadatos y nombres de archivo.
- **Automatizar respaldos:**Programe exportaciones regulares.
- **Usar control de versiones:**Almacene blueprints en Git u otro VCS para colaboración y auditoría.
- **Mantenerse actualizado:**Revise la documentación de la plataforma para novedades, deprecaciones y cambios en las funciones de importación/exportación.

## 6. Errores Comunes y Solución de Problemas

### 6.1 Fallos de Importación

- **Formato de archivo inválido:**Use un linter para comprobar la sintaxis.
- **Dependencias faltantes:**Todos los módulos/recursos deben estar disponibles.
- **Incompatibilidad de versiones:**Asegúrese de que el archivo cumpla los requisitos de versión de la plataforma.
- **Blueprints bloqueados:**Algunas plataformas impiden sobrescribir blueprints en uso.
- **Soporte de navegador:**Algunos navegadores pueden no soportar funciones de importación/exportación.

**Pasos para solucionar:**1. Valide la sintaxis del archivo.
2. Revise la documentación para requisitos de formato/versión.
3. Asegúrese de que existan todos los recursos referenciados.
4. Evite importar sobre blueprints bloqueados o en uso.
5. Use navegadores o herramientas CLI recomendadas.

### 6.2 Problemas Posteriores a la Importación

- **Integraciones desconectadas:**Reconecte todas las cuentas/APIs externas.
- **Ajustes específicos del entorno:**Actualice variables y configuración según sea necesario.
- **Errores de diseño:**Atienda recursos faltantes o errores señalados por la plataforma.

## 7. Plataformas que Soportan Importación / Exportación de Blueprint

### 7.1 Make.com

- **Formato:**JSON
- **Importar/Exportar:**Desde la barra de herramientas del editor de escenarios
- **Tutorial:**[YouTube: Exportar e Importar Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- **Comunidad:**[Make Community: Importar JSON Blueprint](https://community.make.com/t/importing-json-blueprint/88348)

### 7.2 Azure Blueprints

- **Formato:**JSON con subcarpetas de artefactos
- **Importar/Exportar:**PowerShell (`Export-AzBlueprintWithArtifact`, `Import-AzBlueprintWithArtifact`)
- **Docs:**[Importar/Exportar Blueprints con PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- **Deprecación:**Migrar a [Template Specs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/template-specs) y [Deployment Stacks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks).

### 7.3 BMC Cloud Lifecycle Management

- **Formato:**JSON
- **Importar/Exportar:**Espacio de trabajo Service Designer
- **Docs:**[Exportar o importar un blueprint](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)

### 7.4 Plataformas RPA

- **Blueprint, Automation Anywhere, Blue Prism, UiPath**- **Formato:**Específico de la plataforma (frecuentemente JSON o propietario)
- **Importar/Exportar:**Administrado por los administradores de instancia, con ajustes configurables ([Centro de Ayuda Blueprint: Migrar - Importar/Exportar](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export))

## 8. Terminología Relacionada

| Palabra clave           | Descripción                                     |
|-------------------------|-------------------------------------------------|
| Exportar blueprint      | El proceso o comando para guardar un archivo blueprint. |
| Importar blueprint      | El proceso o comando para cargar un blueprint en una plataforma. |
| Exportar importar       | Término general para transferir archivos entre sistemas. |
| Exportando importando   | Realizar ambas operaciones de exportación e importación. |
| Gestionar blueprint     | Prácticas y herramientas para manejar archivos blueprint. |
| Archivo JSON            | Archivo JavaScript Object Notation, usado para la estructura de blueprint. |
| Archivo YAML            | Archivo YAML Ain’t Markup Language, a veces usado para blueprints. |

## 9. Recursos Adicionales y Próximos Pasos

- **Documentación Oficial:**- [Microsoft Learn: Importar y exportar blueprints con PowerShell](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
  - [Exportar o importar un blueprint – Documentación BMC](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)
  - [Centro de Ayuda Blueprint: Migrar - Importar/Exportar](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)
- **Tutoriales y Videos:**- [Make.com YouTube: Exportar e Importar Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
  - [Make Community: Importar JSON Blueprint](https://community.make.com/t/importing-json-blueprint/88348)
- **Comunidad y Formación:**- [Make Academy](https://academy.make.com)
  - [Make Help Centre](https://www.make.com/en/help)
  - [BMC Communities](https://community.bmc.com/)
- **Mejores Prácticas:**- Almacene archivos blueprint en control de versiones (ej. GitHub, GitLab).
  - Integre la gestión de blueprints en pipelines CI/CD.
  - Revise regularmente las notas de lanzamiento de la plataforma para cambios en funciones de importación/exportación.

## 10. Tabla Resumen

| Aspecto                   | Detalles                                                                             |
|---------------------------|--------------------------------------------------------------------------------------|
| **Propósito**| Compartir, respaldar, migrar o controlar versiones de flujos de automatización/chatbot|
| **Tipos de archivo**| JSON (principal), YAML (ocasionalmente)                                              |
| **Cómo exportar**| Acción en la UI o comando CLI                                                        |
| **Cómo importar**| Acción en la UI o comando CLI                                                        |
| **Casos de uso comunes**| Compartir en equipo, migración de entornos, respaldo, control de versiones, migración de plataforma |
| **Ejemplos de plataforma**| Make.com, Azure Blueprints, BMC CLM, herramientas RPA                                |
| **Solución de problemas**| Revise formato de archivo, dependencias, compatibilidad de versión de plataforma      |
| **Mejores prácticas**| Validar, respaldar, usar control de versiones, actualizar integraciones tras la importación |
| **Lectura adicional**| Consulte la documentación y enlaces de comunidad arriba                              |

## 11. Preguntas Frecuentes

**P: ¿Puedo usar un archivo blueprint creado en una plataforma en otra?**R: La mayoría de los archivos blueprint son específicos de la plataforma. Algunos pueden ofrecer herramientas de conversión o formatos compatibles, pero siempre revise la documentación antes de importar entre sistemas.

**P: ¿Exportar un blueprint incluye mis claves API y contraseñas?**R: No. Normalmente se excluyen los datos sensibles. Reconecte las integraciones después de importar.

**P: ¿Qué pasa si importo un blueprint que ya existe?**R: El comportamiento de la plataforma varía—algunas crean una nueva versión, otras sobrescriben, algunas requieren fusión manual. Revise las advertencias de importación y la documentación.

**P: ¿Cómo puedo automatizar las exportaciones de blueprints para respaldo?**R: Use herramientas CLI o APIs para programar las exportaciones, almacenando los archivos de forma segura o en control de versiones.

## 12. Véase También

- [Infraestructura como Código (IaC)](https://learn.microsoft.com/en-us/azure/governance/blueprints/concepts/lifecycle)
- [Fundamentos de Control de Versiones](https://docs.github.com/en/get-started/quickstart/hello-world)
- [CI/CD con Plataformas de Automatización](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-cicd)

### Referencias y Tutoriales

- [Make.com YouTube: Exportar e Importar Blueprints](https://www.youtube.com/watch?v=VF4jkZ6-m-Y)
- [Centro de Ayuda Blueprint: Migrar - Importar/Exportar](https://blueprint.helpdocs.io/article/ajmht7bg69-migrate-import-export)
- [Cambio de Plataformas de Automatización: Guía Completa de Exportación e Importación de Datos | Autonoly](https://www.autonoly.com/blog/68a2aa89d4fe118dae2a444b/switching-automation-platforms-complete-data-export-and-import-guide)
- [Documentación Azure Blueprints](https://learn.microsoft.com/en-us/azure/governance/blueprints/how-to/import-export-ps)
- [Documentación BMC: Exportar o importar un blueprint](https://docs.bmc.com/xwiki/bin/view/Automation-DevSecOps/Client-Management/BMC-Cloud-Lifecycle-Management/clm46/Administering-the-product/Services/Building-service-blueprints/Exporting-or-importing-a-blueprint/)

Esta entrada de glosario ofrece una visión completa y detallada sobre la Importación / Exportación de Blueprint, con referencias autorizadas, mejores prácticas, estructura técnica de archivos e instrucciones específicas por plataforma. Para profundizar, consulte la documentación y los recursos comunitarios enlazados arriba.