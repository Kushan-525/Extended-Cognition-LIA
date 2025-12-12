import streamlit as st

st.set_page_config(
    page_title="Suite de Cognición Extendida",
    page_icon="🐼",
    layout="wide"
)

st.title("🐼 Bienvenido al Hub de Externalización Cognitiva")

st.sidebar.success("Selecciona una herramienta arriba.")

st.markdown("""
### Suite de Herramientas de Cognición Extendida

Este software ha sido diseñado para la **Licenciatura en Inteligencia Artificial** con el propósito de servir como un "andamiaje cognitivo" para los estudiantes.

**Fundamentación:**
Basado en la tesis de la **Mente Extendida (Clark & Chalmers)**, esta suite ofrece módulos que externalizan procesos computacionales costosos, permitiendo al usuario liberar recursos mentales para tareas de mayor abstracción.

### Módulos Disponibles:

1.  **🧠 Visión CNN (Cognición Computacional):**

    * *Simulador de convoluciones para entender la reducción dimensional sin realizar el cálculo matemático manual.*

    * *Extiende la capacidad de visualización espacial.*

2.  **🍅 Reloj Pomodoro (Cognición Regulada):**

    * *Herramienta de gestión atencional para sesiones de estudio profundo.*

    * *Regula los ciclos de atención y descanso (ritmos cognitivos).*

**Selecciona una herramienta en la barra lateral para comenzar.**
""")

# Puedes poner una imagen decorativa o un esquema aquí si quieres
# st.info("Proyecto realizado por: Oscar Eduardo Morales Mora")

st.sidebar.markdown(
    """
    <style>
        /* Ajustamos la barra lateral para que tenga espacio al final */
        [data-testid="stSidebar"] > div:first-child {
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        
        /* Esta clase empuja el contenido hacia abajo */
        .spacer {
            flex-grow: 1; 
        }
        
        /* Estilo elegante para el footer */
        .footer-credit {
            margin-top: auto; /* Esto lo manda al fondo automáticamente */
            padding-top: 20px;
            padding-bottom: 20px;
            border-top: 1px solid rgba(0,0,0,0.1);
            color: #4F4F4F;
            font-size: 11px;
            font-style: italic;
            text-align: left;
        }
    </style>
    """,
    unsafe_allow_html=True
)



# Insertamos un "separador invisible" que crecerá para empujar lo demás
st.sidebar.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Finalmente, el texto de créditos
st.sidebar.markdown(
    """
    <div class="footer-credit">
        Proyecto realizado por:<br>
        <b>Oscar Eduardo Morales Mora</b>
    </div>
    """,
    unsafe_allow_html=True
)