+++
title = "Variables Globales"
translationKey = "global-variables"
description = "Las variables globales son accesibles desde cualquier nodo en un programa o plataforma de automatización, permitiendo compartir datos entre flujos, funciones y contextos. Descubra su uso en chatbots de IA."
keywords = ["Variables Globales", "Chatbot de IA", "Plataforma de Automatización", "Variables de Programación", "Ámbito de Variables"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Global-Variables/"

+++
## Introducción y Definición

Una **variable global**es una variable definida fuera de cualquier función, bloque o nodo y es accesible en todo el programa o flujo de automatización. En el contexto tanto de lenguajes de programación tradicionales como C y Python, como de plataformas de chatbot de IA y automatización, una variable global puede ser accedida y potencialmente modificada desde cualquier parte del código o flujo. Esto contrasta con las variables locales, que están limitadas al ámbito donde se declaran.

Por ejemplo, en programación:
- Una variable declarada fuera de todas las funciones (normalmente al inicio del archivo fuente en C, o fuera de cualquier función en Python) se considera global y permanece accesible durante todo el programa ([GeeksforGeeks: Variables Globales en C](https://www.geeksforgeeks.org/c/global-variables-in-c/), [W3Schools: Variables Globales en Python](https://www.w3schools.com/python/python_variables_global.asp)).
- En plataformas de chatbot de IA, una variable global puede configurarse para persistir entre temas de conversación, pasos de automatización o incluso sesiones, según la arquitectura de la plataforma.

Las variables globales se utilizan comúnmente para:
- Compartir configuraciones entre módulos
- Mantener datos de sesión de usuario entre flujos de conversación
- Permitir el intercambio de contexto entre partes distintas de una aplicación o bot

## Cómo Funcionan las Variables Globales

### Ámbito de las Variables Globales

- **Ámbito Global:**Una variable definida en el ámbito global es accesible desde cualquier función, nodo o tema en la aplicación.
- **Ámbito Local vs. Global:**- Las variables locales están limitadas a la función, bloque o nodo en el que se declaran.
  - Las variables globales son accesibles en cualquier parte del código después de su declaración.

#### Ejemplo en C:
```c
#include <stdio.h>
int x = 5; // variable global

int main() {
    int y = 10; // variable local
    printf("%d", x + y); // x es accesible aquí
    return 0;
}
```
([GeeksforGeeks: Variables Globales en C](https://www.geeksforgeeks.org/c/global-variables-in-c/))

#### Ejemplo en Python:
```python
x = "awesome"  # Variable global

def myfunc():
    print("Python is " + x)  # Accede a la x global

myfunc()
print("Python is " + x)
```
([W3Schools: Variables Globales en Python](https://www.w3schools.com/python/python_variables_global.asp))

#### Ejemplo en Plataformas de Chatbot:
- Una variable configurada como "global" puede ser referenciada en cualquier nodo de diálogo, tema o acción de automatización, como `Global.UserName` o `bot.UserName` en Microsoft Copilot Studio ([Microsoft Copilot Studio – Trabajar con Variables Globales](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot)).

### Ciclo de Vida y Persistencia

- **Duración:**La duración de una variable global puede ir desde todo el tiempo de ejecución de un programa (C, Python), hasta la duración de la sesión de un usuario en un chatbot, o la persistencia entre sesiones si está respaldada por almacenamiento externo.
- **Inicialización:**- En C, las variables globales se inicializan en cero por defecto si no se inicializan explícitamente ([GeeksforGeeks](https://www.geeksforgeeks.org/c/global-variables-in-c/)).
  - En Python, deben ser asignadas antes de su uso.
  - En plataformas de chatbot, pueden inicializarse al inicio de la conversación o establecerse a partir de un parámetro externo.
- **Persistencia:**- Las variables globales estándar se reinician cuando la aplicación o la sesión termina.
  - Para persistir entre sesiones es necesario almacenar el valor en una base de datos o almacenamiento externo.

## Creación, Asignación y Uso de Variables Globales

### En Lenguajes de Programación

#### Python

- **Definir una Variable Global:**Declare una variable fuera de todas las funciones para que sea global.
- **Acceso a Variables Globales:**Puede leerse dentro de cualquier función.
- **Modificar Variables Globales:**Use la palabra clave `global` dentro de una función para modificar una variable global.

**Ejemplo:**```python
x = "awesome"  # Variable global

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  # Salida: Python is fantastic
```
([W3Schools: Variables Globales en Python](https://www.w3schools.com/python/python_variables_global.asp))

- Si existe una variable local con el mismo nombre dentro de una función, esta oculta la variable global dentro del ámbito de esa función. La palabra clave `global` es necesaria para modificar la variable global desde dentro de una función.

#### C

- **Declarar Variables Globales:**Declare variables fuera de cualquier función, normalmente al inicio del archivo.
- **Acceso y Modificación:**Son accesibles y modificables desde cualquier función en el programa.
- **Inicialización por Defecto:**Las variables globales no inicializadas se establecen en cero.

**Ejemplo:**```c
#include <stdio.h>
int a, b; // variables globales

void add() {
    printf("%d", a + b);
}

int main() {
    a = 10;
    b = 15;
    add(); // Salida: 25
    return 0;
}
```
([GeeksforGeeks: Variables Globales en C](https://www.geeksforgeeks.org/c/global-variables-in-c/))

### En Plataformas de Chatbot y Automatización de IA

#### Proceso General

1. **Crear una Variable:**La mayoría de plataformas permiten la creación de variables en ámbitos locales (nodo/tema/paso) y globales (bot/flujo/sesión).
2. **Configurar Ámbito Global:**Configure el ámbito de la variable como "global" o "nivel bot" para acceso entre flujos.
3. **Acceso en Cualquier Nodo:**#### Ejemplo en Microsoft Copilot Studio

- Para crear una variable global:
  1. Cree una variable.
  2. Establezca su ámbito en **Global (cualquier tema puede acceder)**en el panel de propiedades.
  3. El nombre de la variable se muestra con prefijo (por ejemplo, `Global.UserName`).
  4. Ahora la variable puede ser accedida o modificada en cualquier tema o nodo de automatización.
- Para usar una variable global:
  - Use el selector de variables o escriba el nombre con prefijo.
- Para establecer desde fuentes externas:
  - Acepte valores mediante query strings o llamadas API al inicio de la conversación.

([Microsoft Copilot Studio – Trabajar con Variables Globales](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot))

#### Ejemplo en ServiceNow

- Configure una variable como global en Ítems del Catálogo o Flow Designer para hacerla disponible en varios flujos o ítems.
- Úselo con precaución; las variables globales son accesibles y modificables por cualquier función, lo que puede poner en riesgo la consistencia de los datos.

([ServiceNow Community – Discusión sobre Variables Globales](https://www.servicenow.com/community/developer-forum/global-variables/m-p/2608732#M1014639))

### Asignación desde Fuentes Externas

- Muchas plataformas de chatbot permiten inicializar variables globales desde sistemas externos, como parámetros de consulta de páginas web, cabeceras o llamadas API.
- Esto permite pasar contexto (por ejemplo, ID de usuario, tokens de sesión) a un bot o flujo de automatización.

**Ejemplo (Microsoft Copilot Studio):**- Use una URL como `https://web.powerva.microsoft.com/webchat/bots/12345?UserName=Ana` para inicializar `Global.UserName` antes de iniciar la sesión.

## Ejemplos Prácticos

### Ejemplo de Programación: Python

**Variable global dentro y fuera de una función**```python
x = "awesome"

def myfunc():
    print("Python is " + x)  # Accede a la x global

myfunc()
print("Python is " + x)
```
**Salida:**```
Python is awesome
Python is awesome
```

**Cambiar variable global desde una función**```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```
**Salida:**```
Python is fantastic
```
([W3Schools: Variables Globales en Python](https://www.w3schools.com/python/python_variables_global.asp))  
[YouTube: Variables Globales en Python](https://youtu.be/VZW9CGZymqU&list=PLP9IO4UYNF0UgPfkTBECSKIJGdc_9FYZ9)

### Ejemplo de Programación: C

**Declaración y uso de variable global**```c
#include <stdio.h>
int x = 5; // variable global

int main() {
    int y = 10; // variable local
    printf("%d", x + y); // x es accesible aquí
    return 0;
}
```

**Variables globales actualizadas por funciones**```c
#include <stdio.h>
int a, b; // variables globales

void add() {
    printf("%d", a + b);
}

int main() {
    a = 10;
    b = 15;
    add(); // Salida: 25
    return 0;
}
```
([GeeksforGeeks: Variables Globales en C](https://www.geeksforgeeks.org/c/global-variables-in-c/))

### Ejemplo en Plataforma de Chatbot de IA: Microsoft Copilot Studio

**Crear y Usar una Variable Global:**1. Cree una variable llamada `UserName`.
2. Establezca su ámbito en **Global (cualquier tema puede acceder)**.
3. En el tema "Bienvenida", asigne la entrada del usuario a `UserName`.
4. En temas posteriores (por ejemplo, "Reserva de Cita"), haga referencia a `UserName` para respuestas personalizadas.

**Pasar Variables Globales desde Fuentes Externas:**- Inicie el chatbot con una URL como:
  ```
  https://web.powerva.microsoft.com/webchat/bots/12345?UserName=Ana
  ```
- La sesión del chatbot establece la variable `Global.UserName` en "Ana".

**Restablecer Variables Globales:**- Use el tema de sistema **Reset Conversation**para limpiar todas las variables globales, devolviéndolas a su estado inicial.

([Microsoft Copilot Studio – Trabajar con Variables Globales](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot))

## Casos de Uso de Variables Globales

- **Persistencia de Datos de Usuario:**Almacene información del usuario (nombre, correo) una vez y reutilícela en varios temas sin solicitarla repetidamente.
- **Gestión de Sesiones:**Mantenga el estado o atributos de sesión durante toda una conversación o flujo de trabajo.
- **Configuración:**Almacene [feature flags](/en/glossary/feature-flags/) o configuraciones de entorno a las que acceden varios flujos.
- **Intercambio de Contexto:**Pase datos entre subflujos, scripts o ramas.
- **Integración Externa:**Reciba contexto inicial o datos de sesión desde sistemas externos o aplicaciones web.

## Ventajas y Desventajas

### Ventajas

- **Accesibilidad:**Acceso y modificación desde cualquier parte de la aplicación o flujo.
- **Intercambio de Datos:**Facilita compartir información entre módulos o temas que de otro modo estarían aislados.
- **Reducción de Redundancia:**Declaración única; evita solicitudes repetidas al usuario.
- **Gestión de Datos de Sesión:**Ideal para datos de nivel de sesión en chatbots y automatización.

### Desventajas

- **Riesgo de Efectos Colaterales:**Cualquier parte de la aplicación o flujo puede modificar una variable global, lo que puede causar comportamientos no deseados.
- **Complejidad en la Depuración:**Rastrear cambios es difícil en bases de código o flujos grandes.
- **Conflictos Potenciales:**Pueden ocurrir conflictos de nombres o sobrescrituras accidentales sin convenciones de nombres cuidadosas.
- **Uso de Recursos:**El uso excesivo de variables globales puede aumentar el consumo de memoria.
- **Problemas de Concurrencia:**En entornos multiusuario, el acceso simultáneo puede causar inconsistencias en los datos.

## Buenas Prácticas y Consideraciones

- **Uso Limitado:**Use variables globales con moderación; prefiera variables locales para datos no compartidos.
- **Nombres Únicos:**Use nombres claros y únicos para evitar conflictos (por ejemplo, con prefijos `Global.` o `bot.`).
- **Modificación Controlada:**Limite la cantidad de lugares donde se modifican las variables globales.
- **Inicialización:**Inicialice siempre con valores por defecto para evitar estados indefinidos.
- **Documentar Uso:**Documente claramente qué flujos o módulos usan cada variable global.
- **Restablecer cuando sea necesario:**Proporcione mecanismos para restablecer variables globales en los puntos adecuados (por ejemplo, fin de sesión).
- **Seguridad y Privacidad:**Evite almacenar datos sensibles en variables globales a menos que estén debidamente protegidos.

## Notas Específicas por Plataforma

### Microsoft Copilot Studio

- **Prefijo de Variable:**Las variables globales se muestran con el prefijo `Global.` o `bot.` (por ejemplo, `Global.UserName`).
- **Configuración de Ámbito:**Se establece como global mediante el panel de propiedades de la variable.
- **Ámbito de Sesión:**Las variables globales duran toda la sesión del usuario.
- **Inicialización desde Fuentes Externas:**Pueden configurarse mediante parámetros en la URL o programáticamente.
- **Restablecimiento:**Use el tema "Reset Conversation" para limpiar todas las variables globales.

([Microsoft Copilot Studio – Trabajar con Variables Globales](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot))

### ServiceNow

- **Variables en Ítems de Catálogo:**Configurar una variable como global permite su reutilización en tareas y flujos de catálogo.
- **Precaución:**El uso inadecuado puede causar picos de uso de recursos y problemas de integridad de datos por sobrescrituras accidentales.

([ServiceNow Community – Discusión sobre Variables Globales](https://www.servicenow.com/community/developer-forum/global-variables/m-p/2608732#M1014639))

### Otras Plataformas de Automatización y Bots

- **Conceptos Similares:**La mayoría soporta variables globales con reglas de acceso y modificación similares.
- **Documentación de la Plataforma:**Consulte la documentación de cada plataforma para detalles específicos.

## Conceptos Relacionados

- **Variables Locales:**Limitadas a una función, nodo o tema.
- **Variables de Sesión:**Persisten solo durante la duración de una sesión.
- **Variables de Entorno:**Definidas a nivel de sistema o entorno, normalmente para configuración.
- **Constantes:**Variables cuyo valor permanece sin cambios.
- **Gestión de Estado:**Técnicas para gestionar el estado de la aplicación o conversación, a menudo usando variables locales y globales.

## Referencias y Lecturas Adicionales

- [W3Schools Python Global Variables](https://www.w3schools.com/python/python_variables_global.asp)
- [GeeksforGeeks Global Variables in C](https://www.geeksforgeeks.org/c/global-variables-in-c/)
- [Microsoft Copilot Studio – Work with Global Variables](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables-bot)
- [ServiceNow Community – Global Variables Discussion](https://www.servicenow.com/community/developer-forum/global-variables/m-p/2608732#M1014639)
- [YouTube: Python Global Variables](https://youtu.be/VZW9CGZymqU&list=PLP9IO4UYNF0UgPfkTBECSKIJGdc_9FYZ9)

**Resumen:**Las variables globales proporcionan un mecanismo para compartir y almacenar información entre múltiples partes de sistemas de automatización, lenguajes de programación y plataformas de chatbot de IA. Si bien permiten flujos dinámicos, contextuales y eficientes, su gestión cuidadosa es esencial para evitar efectos colaterales y mantener la calidad del código. Para mayor profundidad técnica, consulte las referencias y la documentación de cada plataforma.