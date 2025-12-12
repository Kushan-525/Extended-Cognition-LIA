import streamlit as st
import time

st.set_page_config(page_title="Temporizador Cognitivo", page_icon="🍅", layout="wide")

# --- ESTADO DE SESIÓN (La memoria de la app) ---
# Esto evita que la lista se borre cuando interactúas con el reloj
if 'lista_tareas' not in st.session_state:
    st.session_state.lista_tareas = []

st.title("🍅 Temporizador de Enfoque (Pomodoro)")
st.sidebar.success("Selecciona una herramienta arriba.")

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

st.markdown("Esta herramienta ayuda a **regular tu atención** y a **externalizar tu memoria de trabajo** mediante una lista de control.")

st.divider()

# Creamos dos columnas para organizar mejor la pantalla
col_reloj, col_lista = st.columns([1, 1.5], gap="large")

# --- COLUMNA 1: EL RELOJ ---
with col_reloj:
    st.subheader("⏱️ Configuración")
    minutos = st.slider("Duración del bloque (minutos):", 10, 60, 25)
    
    # Espacio para el temporizador visual
    contenedor_reloj = st.empty()
    
    iniciar = st.button("▶️ Iniciar Ciclo Cognitivo", type="primary")

    if iniciar:
        barra = st.progress(0)
        status = st.empty()
        
        total_segundos = minutos * 60
        
        for i in range(total_segundos):
            # Actualizar barra y números
            percent = (i + 1) / total_segundos
            barra.progress(percent)
            
            segundos_restantes = total_segundos - i
            mins = segundos_restantes // 60
            segs = segundos_restantes % 60
            
            # Mostramos el tiempo en grande
            status.metric("Tiempo Restante", f"{mins:02d}:{segs:02d}")
            time.sleep(1) # Espera real de 1 segundo
            
        st.balloons()
        st.success("¡Felicidades! Ciclo completado. Tu carga cognitiva merece un descanso.")

# --- COLUMNA 2: LA CHECKLIST (AGENDA EXTERNA) ---
with col_lista:
    st.subheader("📝 Agenda Externa (Checklist)")
    st.caption("Escribe aquí los pasos o tareas para liberar tu mente antes de empezar.")

    # 1. Input para nueva tarea (Con truco para limpiar)
    # Usamos 'key' para poder borrarlo después
    def agregar_tarea():
        tarea_texto = st.session_state.nueva_tarea_input
        if tarea_texto:
            st.session_state.lista_tareas.append({"texto": tarea_texto, "hecho": False})
            # ¡Aquí está la magia! Limpiamos la variable asociada al input
            st.session_state.nueva_tarea_input = ""

    # El text_input ahora tiene una 'key' y usamos on_change para que funcione con ENTER
    st.text_input("Agregar nueva actividad:", key="nueva_tarea_input", on_change=agregar_tarea)
    
    # También dejamos el botón por si prefieren hacer clic
    if st.button("➕ Agregar a la lista"):
        agregar_tarea()

    st.markdown("---")

    # 2. Mostrar las tareas
    if len(st.session_state.lista_tareas) == 0:
        st.info("Tu lista está vacía. Agrega una tarea para comenzar.")
    else:
        for i, tarea in enumerate(st.session_state.lista_tareas):
            checked = st.checkbox(tarea["texto"], value=tarea["hecho"], key=f"tarea_{i}")
            st.session_state.lista_tareas[i]["hecho"] = checked

    # Botón para limpiar completadas
    if st.button("🗑️ Limpiar completadas"):
        st.session_state.lista_tareas = [t for t in st.session_state.lista_tareas if not t["hecho"]]
        st.rerun()

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