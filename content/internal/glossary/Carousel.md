+++
title = "Carrusel (Componente UI)"
translationKey = "carousel-ui-component"
description = "Un carrusel es un componente interactivo de UI que muestra una secuencia de elementos de contenido, como imágenes o tarjetas, dentro de una sola vista, permitiendo a los usuarios recorrerlos."
keywords = ["carrusel", "componente UI", "diseño web", "diseño UX", "accesibilidad"]
category = "Chatbot de IA y Automatización"
type = "glosario"
date = 2025-12-02
draft = false
url = "/internal/glossary/Carousel/"

+++
## 1. Definición y resumen <a name="definition-overview"></a>

Un **carrusel** es un componente interactivo de UI que muestra una secuencia de elementos de contenido—como imágenes, tarjetas de texto, productos destacados o llamados a la acción—dentro de una sola vista. Los elementos se organizan horizontalmente y los usuarios pueden recorrerlos haciendo clic en flechas de navegación, usando gestos de deslizamiento o permitiendo la rotación automática para avanzar las diapositivas. Los carruseles a veces se llaman *sliders de imágenes*, *sliders de contenido* o *carruseles de tarjetas*.

**Origen del término:**  
La palabra “carrusel” proviene del juego mecánico de feria, reflejando la manera en que el contenido se rota o recorre de forma circular.

**En chatbots y automatización de IA:**  
Los componentes de carrusel presentan múltiples opciones o respuestas en una UI conversacional compacta, ayudando a guiar las elecciones del usuario sin saturar la ventana de chat.


## 2. Características clave y anatomía <a name="key-features-anatomy"></a>

Diseñar un carrusel usable requiere comprender sus componentes principales:

### **Desglose del componente**

- **Diapositivas (Elementos/Tarjetas):**  
  Cada diapositiva es una unidad individual de contenido (imagen, tarjeta, mensaje, etc.) que se muestra en la vista del carrusel.

- **Controles de navegación:**  
  - **Flechas/Cheurones:** Permiten moverse a la diapositiva anterior/siguiente.
  - **Puntos de paginación/Indicadores:** Visualizan la cantidad de diapositivas y la posición actual. (Nota: [Los puntos de progreso suelen ser demasiado pequeños y poco descriptivos; se prefieren etiquetas o miniaturas para mejor usabilidad. Ver: Smart Interface Design Patterns](https://smart-interface-design-patterns.com/articles/better-carousel-ux/#replace-progress-dots-with-better-labels))
  - **Controles de deslizamiento:** Habilitan la navegación horizontal en dispositivos táctiles.

- **Contenedor:**  
  El elemento que agrupa todo el contenido y controles del carrusel.

- **Rotación automática (opcional):**  
  Avanza automáticamente las diapositivas tras un intervalo definido. Siempre debe ser controlable y pausable por el usuario para la accesibilidad.

- **Bucle (opcional):**  
  Permite que el carrusel pase de la última diapositiva a la primera.

### **Requisitos de accesibilidad**
- Todos los controles deben poder usarse con navegación por teclado.
- El estado del carrusel (qué elemento está activo) debe comunicarse a tecnologías de asistencia.
- Los usuarios deben poder pausar la rotación automática.

**Diagrama anotado:**  
![Anatomía de un carrusel](https://bytescale.mobbin.com/FW25bBB/image/mobbin.com/prod/file.webp?enc=1.DfSR4rss.18iJ_v3n_QwbR2lJ.eh09PQcAjLspC7jzH8D3WbLJaJGelpLbklsuKqetwUOCDosoXs2ea-WYbZG8Uk0RpCzCp8anGjzBz08jYUYBGoqDtSALiyo1CQ34QW_Z62FOhKls1wyO0dzEEI4dlCs4rMMkmHHjF8UjRFmIsvvLG4QiRNedyJ4BW6je98fsCoVyUXeNUZ6JMF7NC2nK4yHqbbTZb4jnO9z_DuexAtrUpg)


## 3. Casos de uso comunes <a name="common-use-cases"></a>

Los carruseles aparecen en muchos productos digitales. Su uso principal es presentar múltiples elementos relacionados sin ocupar mucho espacio vertical.

### **A. Galerías de imágenes**
- E-commerce: Deslizar entre diferentes fotos de productos.
- Portafolios: Mostrar obras, fotografías o casos de estudio.

### **B. Catálogos de productos**
- Tiendas online: Mostrar productos destacados, más vendidos o categorías.
- Chatbots: Sugerir productos o servicios en un flujo conversacional.

### **C. Onboarding y tutoriales**
- Incorporación en apps: Guiar a nuevos usuarios paso a paso por las funciones.
- Recorridos de procesos: Dividir flujos complejos en tarjetas digeribles.

### **D. Controles de navegación**
- Pantallas de inicio: Categorizar contenido con tarjetas deslizables.
- Dashboards: Resumir métricas, alertas o novedades clave.

### **E. Banners promocionales y hero**
- Homepages: Rotar promociones, anuncios o imágenes principales.

**Interacción en el mundo real:**  
Los estudios de usabilidad muestran que la mayoría de los usuarios interactúan solo con la primera diapositiva—[solo el 1% hace clic en los controles del carrusel y el 84% interactúa solo una vez, rara vez avanzando más allá de la primera diapositiva](https://erikrunyon.com/2013/01/carousel-interaction-stats/). Nunca debe ocultarse información crítica en diapositivas posteriores.


## 4. Ventajas y desventajas <a name="benefits-drawbacks"></a>

Los carruseles se usan ampliamente, pero suelen criticarse. Aquí un análisis detallado de sus pros y contras, basados en la experiencia y la investigación.

### **Ventajas**

- **Eficiencia de espacio:**  
  Varios elementos ocupan solo una región de la UI, maximizando el uso del espacio disponible.

- **Enganche visual:**  
  Las animaciones y transiciones atraen la atención, especialmente para contenido destacado o promociones.

- **Variedad de contenido:**  
  Presenta diversas opciones (productos, artículos, características) en un módulo compacto.

- **Control del usuario:**  
  Permiten que el usuario explore a su ritmo, siempre que la navegación sea clara y accesible.

- **Narrativa:**  
  Guía a los usuarios por secuencias (ej. onboarding, historias) de forma ordenada.

### **Desventajas**

- **Bajo engagement más allá de la primera diapositiva:**  
  La mayoría de usuarios ignora o nunca ve las diapositivas posteriores; el contenido vital en estas suele pasar desapercibido. ([NN/g, Eleken, Erik Runyon stats](https://erikrunyon.com/2013/01/carousel-interaction-stats/))

- **Distracción y carga cognitiva:**  
  Los carruseles auto-rotativos pueden distraer, interrumpir la lectura y provocar ceguera a banners.

- **Contenido oculto:**  
  Solo uno (o pocos) elementos se ven a la vez; los usuarios pueden no notar que hay más contenido.

- **Decisión más lenta:**  
  El usuario debe hacer clic/deslizar o esperar la rotación para ver opciones, lo que puede ralentizar su navegación.

- **Problemas de accesibilidad:**  
  Muchos carruseles resultan difíciles de usar con lectores de pantalla y teclado, salvo que sean diseñados específicamente para accesibilidad. ([Guía de Accesibilidad W3C](https://www.w3.org/WAI/tutorials/carousels/))

- **Ceguera a banners:**  
  Los elementos rotativos suelen ser ignorados, sobre todo si se parecen a anuncios o contenido no esencial. ([NN/g sobre Banner Blindness](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/))

**Consejo:**  
Nunca coloques información crítica en diapositivas más allá de la primera—la mayoría de usuarios no la verá.


## 5. Buenas prácticas de diseño <a name="design-best-practices"></a>

Para que los carruseles sean efectivos y fáciles de usar, sigue estas buenas prácticas, extraídas de investigaciones y guías de expertos:

### **A. Limita el número de diapositivas**
- **Óptimo:** 3–5 diapositivas. El engagement cae bruscamente después de las primeras.

### **B. Optimiza la legibilidad**
- Usa imágenes de alta resolución y tipografías grandes y claras.
- Evita saturar las tarjetas con información; mantén el texto conciso.

### **C. Navegación clara**
- Usa flechas visibles e intuitivas o indicaciones de deslizamiento.
- Prefiere pestañas con etiquetas o miniaturas sobre puntos genéricos para la navegación, especialmente en escritorio. ([Smart Patterns](https://smart-interface-design-patterns.com/articles/better-carousel-ux/#replace-progress-dots-with-better-labels))

### **D. Navegación manual por encima de la automática**
- Se prefiere la navegación manual. Si se usa rotación automática, permite pausarla y que el intervalo sea largo (al menos 3–5 segundos).
- Nunca auto-rotes en móvil; los usuarios se desplazan rápido y pueden perder cambios.

### **E. Accesibilidad**
- Todos los controles y diapositivas deben ser accesibles vía teclado.
- Ofrece textos alternativos descriptivos para imágenes.
- Usa roles ARIA y regiones `aria-live` para anunciar cambios a tecnologías de asistencia.
- Permite pausar el movimiento o las animaciones.
- Asegura controles grandes, de alto contraste y amigables al tacto.

### **F. Diseño responsivo**
- El carrusel debe adaptarse fluidamente entre escritorio y móvil.
- En móvil, prioriza los gestos de deslizamiento sobre puntos o flechas pequeños.

### **G. Consistencia y contexto**
- Ajusta el estilo del carrusel a tu marca y UI.
- Asegúrate de que todas las diapositivas sean relevantes—evita contenido de relleno.

### **Checklist: Buen diseño de carrusel**

- [ ] No más de 5 diapositivas
- [ ] Texto e imágenes grandes y legibles
- [ ] CTA fuerte en cada tarjeta
- [ ] Controles de navegación visibles e intuitivos
- [ ] Accesible por teclado y lector de pantalla
- [ ] Totalmente responsivo
- [ ] Rotación automática opcional y controlable por el usuario

**Referencias autorizadas:**  
- [NN/g Guía de Usabilidad de Carruseles](https://www.nngroup.com/articles/designing-effective-carousels/)  
- [W3C: Guía completa de accesibilidad en carruseles](https://www.w3.org/WAI/tutorials/carousels/)  
- [Smart Interface Design Patterns: Mejor UX de Carrusel](https://smart-interface-design-patterns.com/articles/better-carousel-ux/)


## 6. Guía de implementación <a name="implementation-guidance"></a>

### **A. Prototipado (Figma, UXPin, Justinmind)**

**Paso 1: Crea el contenedor**  
Dibuja un marco para el carrusel. Establece restricciones de tamaño para los puntos de quiebre deseados.

**Paso 2: Añade las diapositivas**  
Diseña cada tarjeta—imagen, título, descripción y CTA. Organiza las tarjetas horizontalmente.

**Paso 3: Añade controles de navegación**  
Diseña las flechas izquierda/derecha o cheurones y los indicadores de paginación (mejor etiquetados o miniaturas).

**Paso 4: Define estados/variantes**  
Usa capas o componentes para representar el estado de cada diapositiva.

**Paso 5: Interactividad**  
Vincula los controles para transitar entre diapositivas; simula gestos de deslizamiento en móvil.

**Paso 6: Pruebas responsivas**  
Previsualiza y optimiza para múltiples tamaños de dispositivo.

### **B. Programar un carrusel (React, Vue, JavaScript)**

#### **Opción 1: Usa una librería**

- **React:**  
  - [Swiper.js (React)](https://swiperjs.com/react)
  - [Splide.js (React)](https://splidejs.com/integration/react/)
  - [Nuka Carousel](https://github.com/FormidableLabs/nuka-carousel)
  - [Material-UI Carousel](https://mui.com/material-ui/react-carousel/)

- **Vue:**  
  - [PrimeVue Carousel](https://www.primefaces.org/primevue/carousel)
  - [Vueper Slides](https://antoniandre.github.io/vueper-slides/)

- **Vanilla JS:**  
  - [Swiper.js](https://swiperjs.com/)
  - [Slick Carousel](https://kenwheeler.github.io/slick/)

#### **Opción 2: Implementación personalizada**

**Estructura HTML básica:**
```html
<div class="carousel" role="region" aria-label="Recomendaciones de productos">
  <button class="carousel-arrow left" aria-label="Diapositiva anterior">‹</button>
  <div class="carousel-track">
    <div class="carousel-slide" aria-hidden="false">...</div>
    <div class="carousel-slide" aria-hidden="true">...</div>
    <!-- Más diapositivas -->
  </div>
  <button class="carousel-arrow right" aria-label="Siguiente diapositiva">›</button>
  <div class="carousel-pagination">
    <!-- Puntos o mejor: pestañas con etiqueta o miniaturas -->
  </div>
</div>
```

**CSS:**
- `.carousel-track` usa `display: flex; overflow: hidden;`
- Las diapositivas son hijos flex con `flex: 0 0 100%` para mostrar una por pantalla.

**JavaScript:**
- Mantén un `currentIndex` para rastrear la diapositiva activa.
- Agrega listeners para controles de navegación y gestos de deslizamiento.
- Actualiza `aria-hidden`, el foco y la diapositiva visible en cada interacción.
- Anuncia los cambios de diapositiva a tecnologías de asistencia mediante `aria-live`.

**Guía de accesibilidad:**  
- Usa `<button>` para todos los controles interactivos.
- Todos los controles deben ser accesibles y operables vía teclado.
- Anuncia los cambios a lectores de pantalla usando `aria-live`.
- Ofrece botón de pausa si hay rotación automática.


## 7. Alternativas al carrusel <a name="alternatives-carousels"></a>

El carrusel no siempre es la mejor solución, especialmente para descubrimiento de contenido o accesibilidad. Considera estas alternativas:

### **A. Grillas**
- **Cuándo usar:** Para mostrar muchos elementos a la vez.
- **Pros:** Alto descubrimiento, fácil comparación.
- **Contras:** Requiere más espacio en pantalla.

### **B. Pestañas**
- **Cuándo usar:** Para categorías o secciones distintas.
- **Pros:** Cambio instantáneo, visión clara de las secciones.
- **Contras:** Poco escalable para muchas categorías.

### **C. Listas**
- **Cuándo usar:** Para contenido secuencial o desplazable, especialmente en móvil.
- **Pros:** Navegación natural, fácil de escanear.
- **Contras:** Menos compacto que un carrusel.

### **D. Acordeones**
- **Cuándo usar:** Para información textual y seccionada (FAQs, políticas).
- **Pros:** Reduce el desorden, fácil de recorrer.
- **Contras:** No apto para galerías visuales.


## 8. Ejemplos inspiradores <a name="inspirational-examples"></a>

### **A. Carrusel de productos E-commerce**
![Carrusel de productos relacionados en Amazon](https://assets.justinmind.com/wp-content/uploads/2016/10/amazon-related-products-carousel.png)
- **Características:** Imagen del producto, nombre, precio, valoración, Añadir al carrito.
- **Mejor práctica:** Cada tarjeta es accionable; la navegación es clara.

### **B. Carrusel de hero image**
![Samsung Galaxy S25 Ultra destacado en un carrusel de hero a pantalla completa.](https://assets.justinmind.com/wp-content/uploads/2016/10/samsung-galaxy-s25-ultra-carousel.png)
- **Características:** Imagen de ancho completo, texto conciso, flechas de navegación.
- **Mejor práctica:** Texto mínimo, alto impacto visual.

### **C. Carrusel de equipo**
![Carrusel de equipo](https://assets.justinmind.com/wp-content/uploads/2016/10/team-carousel-example.png)
- **Características:** Fotos de perfil, cargos, desplazamiento manual fluido.
- **Mejor práctica:** Diseño limpio, presentaciones rápidas.

### **D. Carrusel de onboarding (móvil)**
![Carrusel de onboarding](https://bytescale.mobbin.com/FW25bBB/image/mobbin.com/prod/file.webp?enc=1.DfSR4rss.JQo1mVWgGOqeq3f-.SwFc2Ch7GAV1WYEBXSLTaGFaYPE0nPyTcTykp_Ll-t57kpYhuaoPEcq8NdrS2UVOCFvRMX2DDYX81t-_Od_nLnS2mOAJD58vL2ad9tU-Vb4mS73ZbAIlZpkBhIZ6dcQUK4QLdu_rBCGa7mav54eWXRRmqQIQfAiKGyk3VJ5mwRT7PK4u_gmr63E6W6ZQ0GUS2UaVJQ8fSgpsMyMZNb7-Lw)
- **Características:** Guía paso a paso, navegación por deslizamiento, puntos de progreso.
- **Mejor práctica:** Cada paso enfoca un solo mensaje; el deslizamiento es intuitivo.

**Prototipos descargables:**
- [Carrusel de libros Justinmind](https://www.justinmind.com/open-resource?url=/design-templates/Online-bookstore-template.vp)
- [Ejemplo de panel dinámico de carrusel Justinmind](https://www.justinmind.com/open-resource?url=/examples/Carousel-DynamicPanel.vp)

**UI