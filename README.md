# 🧠 Extended-Cognition-LIA: Suite de Herramientas Cognitivas

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![Status](https://img.shields.io/badge/Status-Academic_Project-success)

## 📋 Descripción del Proyecto
Este software ha sido desarrollado como parte de la **Licenciatura en Inteligencia Artificial**. Funciona como un sistema de **"Andamiaje Cognitivo"**, diseñado para externalizar procesos computacionales costosos y regular la atención del estudiante.

El proyecto se fundamenta en la tesis de la **Mente Extendida (Clark & Chalmers)**, demostrando cómo herramientas digitales interactivas pueden integrarse en el bucle cognitivo del ingeniero de IA, permitiendo liberar recursos mentales para tareas de mayor abstracción arquitectónica .

---

## 🚀 Módulos y Fundamentación Teórica

La aplicación cuenta con una arquitectura modular que ataca distintas necesidades cognitivas identificadas en la carrera:

### 1. Visión CNN (Simulador de Convoluciones)
* **Tipo de Cognición:** *Cognición Extendida / Descarga Cognitiva.*
* **Función:** Externaliza el cálculo matemático de la reducción dimensional en Redes Neuronales Convolucionales (CNN).
* **Justificación:** En lugar de realizar aritmética mental propensa a errores, el estudiante manipula parámetros visuales (Kernel, Stride, Padding).
* **Enfoque Enactivo:** El uso de *sliders* y la visualización en tiempo real de la imagen propia del usuario permite "aprender haciendo" (acción epistémica), observando cómo se pierde información espacial al aumentar el *stride* .

### 2. Reloj Pomodoro + Agenda Externa
* **Tipo de Cognición:** *Cognición Regulada / Memoria Prospectiva.*
* **Función:** Sistema de gestión atencional con lista de tareas persistente.
* **Justificación:** Actúa como un regulador externo del foco atencional y una memoria externa para la gestión de tareas, reduciendo la carga cognitiva asociada al *multitasking*.

---

## 🛠️ Características Técnicas
* **Framework:** Python + Streamlit.
* **Interfaz:** Diseño UI/UX personalizado con selector de temas (**Pink Theme** por defecto y **Dark Mode** de alto contraste).
* **Interactividad:** Procesamiento de imágenes en tiempo real usando `Pillow` y `NumPy`.
* **Persistencia:** Uso de `Session State` para el manejo de listas de tareas y configuraciones.

---

## 💻 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/Extended-Cognition-LIA.git](https://github.com/TU_USUARIO/Extended-Cognition-LIA.git)
    cd Extended-Cognition-LIA
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install streamlit matplotlib pillow numpy
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    python -m streamlit run Inicio.py
    ```

---

## 📂 Estructura del Proyecto

```text
Extended-Cognition-LIA/
│
├── .streamlit/          # Configuración de temas (Pink Mode)
│   └── config.toml
├── pages/               # Módulos de la aplicación
│   ├── 1_🧠_Vision_CNN.py
│   └── 2_🍅_Reloj_Pomodoro.py
├── Inicio.py            # Hub principal (Main Entry Point)
└── README.md            # Documentación
