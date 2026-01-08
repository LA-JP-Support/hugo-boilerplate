+++
title = "Entorno Variables (Secretos): El Fondo"
translationKey = "environment-variables-secrets"
description = "Aprenda sobre variables de entorno (secretos) para una configuración segura de aplicaciones. Separe datos sensibles como claves API y contraseñas del código, asegurando seguridad y flexibilidad."
keywords = [
  "variables de entorno",
  "gestión de secretos",
  "claves API",
  "seguridad de aplicaciones",
  "gestión de configuración"
]
category = "General"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Environment-Variables--Secrets-/"

+++
## ¿Qué son las Variables de Entorno (Secretos)?

Las variables de entorno son pares clave-valor con nombre, definidos externamente, que proveen configuración en tiempo de ejecución a las aplicaciones. Cuando se utilizan para secretos, almacenan datos sensibles—claves API, contraseñas, cadenas de conexión, tokens—fuera del código, interfaces de usuario o registros. Esta separación garantiza que los secretos nunca estén codificados en el código fuente ni se suban al control de versiones.

- **Analogía:**El valor de una variable de entorno actúa como un marcador de posición en su código. Por ejemplo, en lugar de escribir `API_KEY = "secret123"`, referencia `API_KEY`, que solo se define en tiempo de ejecución en el entorno de ejecución.
- **Contexto de Seguridad:**Almacenar secretos en variables de entorno minimiza el riesgo de exposición accidental a través de filtraciones de código, acceso a repositorios Git o registros. Los valores sensibles se inyectan en tiempo de ejecución y no se almacenan en interfaces visuales ni archivos de configuración a menos que sea necesario.
- **Tipos de Secretos:**Contraseñas de bases de datos, tokens API, credenciales OAuth, claves criptográficas, [feature flags](/es/glossary/feature-flags/), y más.

**Ver:**- [OWASP Hoja de Trucos de Gestión de Secretos—Introducción y Conceptos Generales](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#1-introduction)  
- [Kinsta: ¿Qué es una Variable de Entorno?](https://kinsta.com/blog/what-is-an-environment-variable/)

## ¿Por qué usar variables de entorno para secretos?

**Separación de Código y Configuración:**- Mantiene los datos sensibles fuera del código y el control de versiones.  
- Permite que el mismo código se ejecute en diferentes entornos (desarrollo, pruebas, producción) con diferentes credenciales.

**Seguridad:**- Reduce el riesgo de filtración de secretos al no incluirlos en el código o repositorios públicos.
- Impide que los secretos se expongan en registros, mensajes de error o interfaces.

**Flexibilidad y Mantenibilidad:**- Los secretos pueden actualizarse o rotarse sin cambiar el código.
- Permite responder rápidamente a incidentes (ej. filtraciones de credenciales) cambiando la variable de entorno y reiniciando la aplicación.

**Escalabilidad y Consistencia:**- Gestione valores específicos de entorno (dev/staging/prod) de forma centralizada.
- Pipelines de despliegue consistentes (CI/CD) que no requieren cambios de código para actualizaciones de configuración.

**Aislamiento de Procesos:**- Cada proceso tiene acceso solo a los secretos relevantes, reduciendo exposiciones accidentales o escaladas de privilegios.
## Tipos de Variables de Entorno

### 1. Variables de Entorno del Sistema
- Definidas a nivel del sistema operativo.
- Afectan a todos los procesos y usuarios en la máquina.
- Ejemplo: Agregar directorios a la variable `PATH` en Unix o Windows.

### 2. Variables de Entorno de Usuario
- Alcance a un perfil de usuario específico.
- Solo los procesos lanzados por ese usuario pueden acceder a estas variables.
- Ejemplo: Windows permite editar variables de entorno de usuario desde el Panel de Control.

### 3. Variables de Entorno de Proceso/Ejecución
- Alcance a un proceso o sesión específica.
- Definidas temporalmente para una sesión o al lanzar un proceso.

### 4. Secretos de Build vs. Runtime
- **Build-Time:**Usados durante el proceso de construcción/compilación (ej. obtención de dependencias).
- **Runtime:**Usados mientras la aplicación está en ejecución (ej. conexión a servicios en vivo).

### 5. A nivel de Aplicación/Proyecto (.env, Gestores de Secretos)
- Los archivos `.env` almacenan variables de entorno para desarrollo local.
- Gestores de secretos (ej. AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) proveen almacenamiento cifrado con auditoría, control de acceso y rotación.

### Diferencias entre Plataformas
- **Windows:**Definir vía Panel de Control, CLI (`set`), o PowerShell (`$env:VAR_NAME`).
- **Unix/Linux/macOS:**Definir vía `export VAR=valor` en shell, o agregar a `.bashrc`/`.zshrc` para persistencia.
## ¿Cómo se usan las variables de entorno?

**Flujo de Trabajo:**1. Defina secretos fuera del código (SO, archivo `.env`, gestor de secretos, dashboard de despliegue).
2. Refierálos en el código de la aplicación mediante APIs de variables de entorno.
3. Despliegue la aplicación—los secretos se inyectan en tiempo de ejecución.

**Ejemplo:**En vez de codificar `API_KEY = "abc123"`, defina el valor como variable de entorno y deje que la aplicación lo lea de forma segura en tiempo de ejecución.

**Inyección Automática de Secretos:**- En CI/CD, los secretos suelen inyectarse en build o despliegue.
- Gestores de secretos o dashboards de despliegue ofrecen interfaces/APIs para definir y rotar secretos.
## Casos de Uso Comunes y Ejemplos

- **Claves API:**Servicios externos (OpenAI, Google Cloud, Stripe).
- **Credenciales de Base de Datos:**Transmita usuario, contraseña y host de DB de forma segura.
- **Tokens Secretos:**Claves de firmado JWT, secretos OAuth, tokens de webhook.
- **Feature Flags:**Activar/desactivar funcionalidades dinámicamente.
- **Tags de Entorno:**Indicar `development`, `staging` o `production`.

**Ejemplo .env:**```
OPENAI_API_KEY=sk-abc123
DATABASE_URL=postgres://user:pass@host:5432/db
MODE=production
```

**Ejemplos de Plataforma:**- [Variables de Entorno en Netlify](https://docs.netlify.com/configure-builds/environment-variables/)
- [Variables de Entorno en Vercel](https://vercel.com/docs/concepts/projects/environment-variables)

## Definir y Acceder a Variables de Entorno

### A nivel de Sistema Operativo

#### Unix/Linux/macOS

- Definir para la sesión actual:
  ```sh
  export API_KEY="abc123"
  ```
- Definir para un solo comando:
  ```sh
  API_KEY="abc123" python app.py
  ```
- Persistente para el usuario:
  ```sh
  echo 'export API_KEY="abc123"' >> ~/.bashrc
  source ~/.bashrc
  ```

#### Windows

- Definir para la sesión actual (cmd):
  ```bat
  set API_KEY=abc123
  ```
- Persistente vía GUI:  
  Panel de Control → Sistema → Avanzado → Variables de Entorno
- PowerShell:
  ```powershell
  $env:API_KEY="abc123"
  ```

### En Código de Aplicación (.env, Gestores de Secretos, Dashboards de Plataforma)

#### Archivos .env

- Coloque un archivo `.env` en la raíz del proyecto:
  ```
  API_KEY=abc123
  DB_PASS=supersecret
  ```
- **Seguridad:**Agregue siempre `.env` a `.gitignore` para evitar commits accidentales al control de versiones.

#### Gestores de Secretos

- **AWS Secrets Manager:**[Documentación Oficial](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- **Azure Key Vault:**[Documentación Oficial](https://learn.microsoft.com/en-us/azure/key-vault/)
- **HashiCorp Vault:**[Documentación Oficial](https://www.vaultproject.io/docs)
- Los secretos están cifrados, con control de acceso y auditoría.

#### Dashboards de Plataforma

- **Render:**[Configurar Variables de Entorno](https://render.com/docs/configure-environment-variables)
- **Netlify:**[Variables de Entorno](https://docs.netlify.com/configure-builds/environment-variables/)
- **Vercel:**[Variables de Entorno](https://vercel.com/docs/concepts/projects/environment-variables)

### Ejemplos de Código: Node.js, Python, .NET

#### Node.js

- Acceder a variables de entorno:
  ```js
  // index.js
  console.log(process.env.API_KEY);
  ```
- Con dotenv:
  ```js
  require('dotenv').config();
  const apiKey = process.env.API_KEY;
  ```

#### Python

- Acceder a variables de entorno:
  ```python
  import os
  api_key = os.environ.get('API_KEY')
  ```
- Con python-dotenv:
  ```python
  from dotenv import load_dotenv
  load_dotenv()
  api_key = os.getenv('API_KEY')
  ```

#### .NET (C#)

- Acceder a variables de entorno:
  ```csharp
  var apiKey = Environment.GetEnvironmentVariable("API_KEY");
  ```
- Secretos de Usuario en ASP.NET Core:
  1. Inicializar secretos:
     ```
     dotnet user-secrets init
     ```
  2. Definir secreto:
     ```
     dotnet user-secrets set "Movies:ServiceApiKey" "12345"
     ```
  3. Acceder en el código:
     ```csharp
     var builder = WebApplication.CreateBuilder(args);
     var movieApiKey = builder.Configuration["Movies:ServiceApiKey"];
     ```
## Gestión y Rotación de Secretos

**Ciclo de Vida del Secreto:**- **Definir Múltiples Secretos:**Por lote vía archivos `.env`, dashboards de plataforma o APIs de gestores de secretos.
- **Listar Secretos:**Herramientas CLI (ej. `dotnet user-secrets list`), dashboards, APIs.
- **Actualizar/Rotar:**Cambie valores en los gestores de secretos, archivos `.env` o dashboards; redepliegue/reinicie apps si es necesario.
- **Eliminar/Expirar:**Elimine o revoque secretos cuando ya no sean necesarios. Los secretos expirados deben purgarse.

**Rotación Automática:**- Use secretos dinámicos (si es posible) que expiran tras su uso o sesión, ej. credenciales temporales de BD vía Vault.
- Configure rotación programada en gestores de secretos (AWS, Azure, HashiCorp Vault).
- Asegure que el código soporte hot-reload o re-autenticación ante cambios de secretos.

**Mapeo a Objetos de Configuración:**- .NET: Mapee secretos a POCOs para acceso estructurado.
- Node.js/Python: Use librerías de configuración o wrappers personalizados para validación y agregación.
## Buenas Prácticas de Seguridad

- **Nunca almacene secretos en el control de versiones.**- **Agregue `.env` y archivos similares a `.gitignore`.**- **Use gestores de secretos en producción, no archivos en texto plano.**- **Principio de mínimo privilegio:**Restrinja el acceso solo a quien lo necesite.
- **Rote y revoque los secretos regularmente.**- **Audite y registre todo acceso a los secretos.**- **Nunca exponga secretos de tiempo de ejecución en código cliente (ej. JavaScript en navegador).**- **Automatice el escaneo de secretos en pipelines CI/CD:**- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-security/about-secret-scanning)
    - [Azure DevOps Credential Scanner](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-secret-scanning)

- **Cifre los secretos en reposo y en tránsito.**- **Aísle los secretos por entorno y servicio.**- **Minimice la interacción humana con los secretos—use pipelines automatizados.**## Escenarios Avanzados: Múltiples Entornos, Archivos de Secretos, Grupos de Entorno

- **Múltiples Entornos:**Use archivos `.env` o sets de secretos separados para `development`, `staging` y `production`.
- **Archivos de Secretos:**Suba archivos secretos (ej. claves privadas) vía dashboards de plataforma (Render, Vercel).
- **Grupos de Entorno:**Agrupe variables para microservicios o despliegues multi-app.
- **Configuración Centralizada:**Use grupos de entorno o gestores de secretos para compartir secretos entre equipos/servicios.

**Patrones Arquitectónicos:**- **Kubernetes Sidecar:**Use un contenedor sidecar (ej. Vault Agent) para obtener secretos y montarlos en el contenedor principal ([Ejemplo OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html#example-1-kubernetes-with-a-sidecar-container)).
- **Secretos Dinámicos:**Las aplicaciones solicitan secretos al arrancar y reciben credenciales temporales y auto-expirables.

## Limitaciones y Alternativas

**Limitaciones:**- **Almacenamiento en texto plano:**Archivos `.env` y variables a nivel SO están sin cifrar en disco.
- **Configs complejas:**Estructurar configuraciones anidadas o grandes en variables de entorno es difícil.
- **Sincronización manual:**Distribuir secretos entre equipos/entornos puede ser propenso a errores sin un gestor central.

**Alternativas:**- **Gestores de Secretos:**AWS Secrets Manager, Azure Key Vault, HashiCorp Vault.
- **Archivos de configuración cifrados:**Para configs complejas (deben excluirse del control de versiones).
- **Herramientas de plataforma:**Use dashboards de despliegue (Render, Vercel, Netlify) para gestionar y agrupar secretos.
## Puntos Clave

- Las variables de entorno inyectan valores sensibles en las apps de forma segura sin exponerlos en código o interfaces.
- Separan la configuración del código, permitiendo despliegues seguros y flexibles.
- Use archivos `.env` para desarrollo local (con `.gitignore` estricto); gestores de secretos o dashboards para producción.
- Rote y audite secretos; nunca los registre ni exponga en código cliente.
- Gestione secretos por entorno y equipo para aislamiento.
- Nunca suba secretos al control de versiones; use controles de acceso y cifrado en producción.

## Referencias y Lectura Adicional

- [OWASP: Hoja de Trucos de Gestión de Secretos](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [Microsoft Learn: Mejores prácticas para proteger secretos](https://learn.microsoft.com/en-us/azure/security/fundamentals/secrets-best-practices)
- [Microsoft Docs: Almacenamiento seguro de secretos de app en ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0)
- [Kinsta: ¿Qué es una Variable de Entorno?](https://kinsta.com/blog/what-is-an-environment-variable/)
- [DreamHost: Variables de Entorno Explicadas](https://www.dreamhost.com/blog/environment-variables/)
- [Render Docs: Variables de Entorno y Secretos](https://render.com/docs/configure-environment-variables)
- [Stack Overflow: ¿Cómo almacenar y acceder a claves API y contraseñas con Gatsby?](https://stackoverflow.com/questions/62231572/how-to-store-and-access-api-keys-and-passwords-with-gatsby)
- [Documentación de HashiCorp Vault](https://www.vaultproject.io/docs)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-security/about-secret-scanning)

## Escenario de Ejemplo: Chatbot de IA en Producción

Suponga que tiene un chatbot de IA que necesita una clave API de un LLM externo. En vez de incrustar la clave en el código, usted:
1. Almacena la clave API en el dashboard de variables de entorno de la plataforma o gestor de secretos.
2. La aplicación lee `OPENAI_API_KEY` del entorno en tiempo de ejecución.
3. La clave nunca se expone a usuarios, código o registros.
4. Para rotar, actualícela en el dashboard/gestor de secretos y redepliegue—sin cambios de código.

**Ejemplo Node.js:**```js
require('dotenv').config();
const openai = require('openai');
openai.apiKey = process.env.OPENAI_API_KEY;
```
**Ejemplo Python:**```python
import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
```
**Ejemplo .NET:**```csharp
var builder = WebApplication.CreateBuilder(args);
var openAiApiKey = builder.Configuration["OPENAI_API_KEY"];
```
- [Cómo almacenar y acceder