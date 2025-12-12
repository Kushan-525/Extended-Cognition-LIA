import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

# --- Texto principal de la página ---


st.set_page_config(page_title="Extensión Cognitiva CNN", layout="wide", page_icon="🧠")
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

st.title("🧠 Cognición Extendida: Simulador de Visión")
st.markdown("""
Esta herramienta es una **memoria externa**. 

Ayuda a visualizar cómo una Red Neuronal _"ve"_ y _"transforma"_ tus imágenes.

Sube una foto y ajusta los parámetros matemáticos para ver el efecto en tiempo real.
""")

# --- Barra lateral ---
st.sidebar.header("1. Configuración de la Capa")

# Input para subir imagen
uploaded_file = st.sidebar.file_uploader("Sube tu imagen (jpg/png)", type=["jpg", "png", "jpeg"])

st.sidebar.markdown("---")
st.sidebar.header("2. Hiperparámetros")

# El tamaño de entrada ahora depende de si hay imagen o es manual
if uploaded_file is not None:
    img_original = Image.open(uploaded_file)
    st.sidebar.info(f"Imagen original: {img_original.size}")
    # Por defecto se coloca un valor de 224
    W = st.sidebar.number_input("Redimensionar entrada a (px):", min_value=10, value=213)
else:
    W = st.sidebar.number_input("Tamaño Entrada Simulado (W):", min_value=10, value=213)

F = st.sidebar.slider("Tamaño Filtro / Kernel (F)", 1, 15, 3)
S = st.sidebar.slider("Stride / Paso (S)", 1, 5, 2)
P_type = st.sidebar.radio("Tipo de Padding", ["Valid (Sin relleno)", "Same (Mantiene tamaño)", "Manual"])

# Lógica del Padding
P = 0
if P_type == "Same (Mantiene tamaño)":
    if S == 1:
        P = (F - 1) // 2
    else:
        st.sidebar.warning("Con Stride > 1, 'Same' no mantiene el tamaño, solo agrega borde.")
        P = (F - 1) // 2
elif P_type == "Manual":
    P = st.sidebar.slider("Padding Manual (P)", 0, 10, 1)

# --- Formula de la red ---
output_raw = ((W - F + (2 * P)) / S) + 1
output_size = int(output_raw)

# --- Caja de visualización ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Entrada (Input)")
    st.metric(label="Dimensiones", value=f"{W} x {W} px")
    
    if uploaded_file is not None:
        # Redimensionamos la imagen real al tamaño de entrada W
        img_input_display = img_original.resize((W, W))
        st.image(img_input_display, caption="Lo que entra a la neurona", use_container_width=True)
    else:
        # Si no hay foto, mostramos el cuadrado azul abstracto
        fig, ax = plt.subplots(figsize=(4, 4))
        rect_in = patches.Rectangle((0, 0), W, W, linewidth=2, edgecolor='#B3497E', facecolor='#FFB6C1', label='Entrada')
        ax.add_patch(rect_in)
        ax.set_xlim(-10, W+10)
        ax.set_ylim(-10, W+10)
        ax.axis('off')
        st.pyplot(fig)

with col2:
    st.subheader("Salida (Feature Map)")
    
    if output_raw.is_integer() and output_size > 0:
        st.metric(label="Dimensiones", value=f"{output_size} x {output_size} px", delta=f"{output_size - W} px (Reducción)")
        
        if uploaded_file is not None:
            # Redimension la imagen para simular la pérdida de resolución espacial
            # 'Image.NEAREST' para que se vea pixelado y sea evidente la "convolución"
            img_output_display = img_input_display.resize((output_size, output_size), resample=Image.NEAREST)
            
            # La mostramos al tamaño "real" visualmente en pantalla para comparar
            st.image(img_output_display, caption=f"Mapa de características resultante ({output_size}x{output_size})", width=output_size if output_size > 100 else 200)
            
            st.success("Visualización exitosa: Así es como la red comprime la información espacial.")
        else:
            # Cuadrado Rojo de comparacion
            fig2, ax2 = plt.subplots(figsize=(4, 4))
            rect_out = patches.Rectangle((0, 0), output_size, output_size, linewidth=2, edgecolor='#B3497E', facecolor='#FFB7B2', label='Salida')
            ax2.add_patch(rect_out)
            ax2.set_xlim(-10, W+10) # Escala del input para comparar tamaño
            ax2.set_ylim(-10, W+10)
            ax2.axis('off')
            st.pyplot(fig2)
            
    else:
        st.error(f"⚠️ Error matemático: La salida es {output_raw:.2f}. Revisa el Stride o Padding.")

# --- Generador de código de abajo ---
st.markdown("---")
st.subheader("💻 Código Generado")
code = f"model.add(Conv2D(filters=32, kernel_size=({F},{F}), strides=({S},{S}), padding='{'same' if P_type == 'Same (Mantiene tamaño)' else 'valid'}'))"
st.code(code, language='python')

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