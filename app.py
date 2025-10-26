import streamlit as st
import plotly.graph_objects as go
import random
from datetime import datetime

# Datos de retos diarios
RETOS_DIARIOS = [
    {"id": 1, "descripcion": "Toma 8 vasos de agua hoy", "puntos": 10, "categoria": "Hidratación"},
    {"id": 2, "descripcion": "Consume 2 frutas locales", "puntos": 15, "categoria": "Alimentación"},
    {"id": 3, "descripcion": "Camina 30 minutos", "puntos": 20, "categoria": "Ejercicio"},
    {"id": 4, "descripcion": "Come una comida saludable", "puntos": 25, "categoria": "Alimentación"},
    {"id": 5, "descripcion": "Evita alimentos procesados por un día", "puntos": 30, "categoria": "Salud"}
]

# Funciones auxiliares
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso", "#FF6B6B", "💪"
    elif imc < 25:
        return "Peso normal", "#4ECDC4", "✅"
    elif imc < 30:
        return "Sobrepeso", "#FFA726", "⚠️"
    else:
        return "Obesidad", "#EF5350", "🚨"

def calcular_meta(imc):
    if imc < 18.5:
        return "Ganar peso saludablemente"
    elif imc < 25:
        return "Mantener peso actual"
    elif imc < 30:
        return "Perder 5-10% de peso"
    else:
        return "Perder 10-15% de peso"

def crear_grafico_progreso(imc):
    categorias = ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]
    colors = ["#FF6B6B", "#4ECDC4", "#FFA726", "#EF5350"]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=categorias,
        y=[1, 1, 1, 1],
        marker_color=colors,
        opacity=0.3,
        name="Rangos IMC"
    ))
    
    # Marcador para el IMC actual
    categoria_actual, color_actual, emoji = clasificar_imc(imc)
    
    fig.add_trace(go.Scatter(
        x=[categoria_actual],
        y=[0.5],
        marker=dict(size=20, color=color_actual),
        mode="markers+text",
        text=[f"Tú: {imc:.1f}"],
        textposition="bottom center",
        name="Tu IMC"
    ))
    
    fig.update_layout(
        title="Tu IMC en el contexto de los rangos de salud",
        showlegend=False,
        height=300
    )
    return fig

def generar_consejo_local(imc):
    consejos_bajo_peso = [
        "Incluye más nueces chihuahuenses en tus snacks - son calóricas y nutritivas",
        "Prepara atole de maíz con leche para ganar peso saludablemente"
    ]
    consejos_normal = [
        "Mantén tu rutina visitando los mercados locales por frutas frescas",
        "La manzana de Cuauhtémoc es tu aliada perfecta para mantener el peso"
    ]
    consejos_sobrepeso = [
        "Sustituye refrescos por aguas frescas de frutas locales sin azúcar",
        "Camina en los parques de tu ciudad 30 min al día, ¡Chihuahua tiene espacios perfectos!"
    ]
    consejos_obesidad = [
        "Consulta en el Centro de Salud más cercano para plan personalizado",
        "Inicia con cambios pequeños: usa frijoles en lugar de carnes procesadas"
    ]
    
    categoria, _, _ = clasificar_imc(imc)
    if categoria == "Bajo peso":
        return random.choice(consejos_bajo_peso)
    elif categoria == "Peso normal":
        return random.choice(consejos_normal)
    elif categoria == "Sobrepeso":
        return random.choice(consejos_sobrepeso)
    else:
        return random.choice(consejos_obesidad)

def calcular_nivel(puntos):
    if puntos < 50:
        return "Principiante 🌱"
    elif puntos < 150:
        return "Intermedio 🚀"
    elif puntos < 300:
        return "Avanzado 💪"
    else:
        return "Experto 🏆"

def mostrar_todos_consejos():
    st.header("💡 Consejos por Categoría de IMC")
    
    # Consejos para Bajo Peso
    with st.expander("📉 Consejos para **Bajo Peso**", expanded=False):
        st.markdown("""
        - Incluye más nueces chihuahuenses en tus snacks - son calóricas y nutritivas
        - Prepara atole de maíz con leche para ganar peso saludablemente
        - Aumenta el consumo de aguacate en tus comidas
        - Incluye frijoles en tu alimentación diaria
        - Consume 5-6 comidas pequeñas al día
        """)
    
    # Consejos para Peso Normal
    with st.expander("✅ Consejos para **Peso Normal**", expanded=False):
        st.markdown("""
        - Mantén tu rutina visitando los mercados locales por frutas frescas
        - La manzana de Cuauhtémoc es tu aliada perfecta para mantener el peso
        - Varía tus verduras según la temporada
        - Combina proteínas animales y vegetales
        - No saltes comidas y mantén horarios regulares
        """)
    
    # Consejos para Sobrepeso
    with st.expander("⚠️ Consejos para **Sobrepeso**", expanded=False):
        st.markdown("""
        - Sustituye refrescos por aguas frescas de frutas locales sin azúcar
        - Camina en los parques de tu ciudad 30 min al día
        - Reduce el consumo de harinas refinadas
        - Controla las porciones usando platos más pequeños
        - Aumenta el consumo de verduras de hoja verde
        """)
    
    # Consejos para Obesidad
    with st.expander("🚨 Consejos para **Obesidad**", expanded=False):
        st.markdown("""
        - Consulta en el Centro de Salud más cercano para plan personalizado
        - Inicia con cambios pequeños: usa frijoles en lugar de carnes procesadas
        - Establece metas realistas - perder 5-10% de peso ya mejora tu salud
        - Busca apoyo en grupos comunitarios de salud en tu municipio
        - Prioriza la actividad física diaria
        """)
    
    # Consejos generales para todos
    st.header("🌿 Consejos Generales para Todos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🍎 Alimentación")
        st.markdown("""
        - Consume frutas y verduras de temporada
        - Prefiere alimentos locales y frescos
        - Toma al menos 2 litros de agua al día
        - Incluye proteínas en cada comida
        - Modera el consumo de sal y azúcar
        """)
    
    with col2:
        st.subheader("🏃‍♂️ Estilo de Vida")
        st.markdown("""
        - Realiza 30 minutos de actividad física diaria
        - Duerme 7-8 horas cada noche
        - Controla el estrés con técnicas de relajación
        - Evita el tabaco y limita el alcohol
        - Realiza chequeos médicos periódicos
        """)

# Inicialización del estado de la sesión
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
if 'retos_completados' not in st.session_state:
    st.session_state.retos_completados = set()

# Configuración de la página
st.set_page_config(page_title="Retos Saludables", page_icon="🏆", layout="wide")

# Estilos CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f8f0;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E8B57;
        margin: 10px 0;
    }
    .reto-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Barra lateral de navegación
with st.sidebar:
    st.image("https://via.placeholder.com/150x150/2E8B57/FFFFFF?text=ABC", width=150)
    
    menu = st.radio("Navegación", [
        "🏆 Retos Saludables", 
        "📊 Diagnóstico Personal", 
        "💡 Consejos de Salud",
        "🔄 Reiniciar Progreso"
    ])

# Contenido principal según la selección del menú
if menu == "🏆 Retos Saludables":
    # Título principal
    st.title("🏆 Retos Saludables Chihuahua")
    st.markdown("Completa retos diarios y gana puntos para mejorar tu salud")

    # Sección de progreso del usuario
    st.header("📊 Tu Progreso")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏅 Nivel Actual", calcular_nivel(st.session_state.puntos))
    with col2:
        st.metric("⭐ Puntos Acumulados", st.session_state.puntos)
    with col3:
        st.metric("✅ Retos Completados", len(st.session_state.retos_completados))

    # Barra de progreso
    progreso = min(st.session_state.puntos / 500 * 100, 100)
    st.progress(int(progreso))
    st.caption(f"Progreso hacia el siguiente nivel: {progreso:.1f}%")

    # Sección de retos diarios
    st.header("🎯 Retos de Hoy")

    for reto in RETOS_DIARIOS:
        completado = reto['id'] in st.session_state.retos_completados
        
        with st.container():
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                if completado:
                    st.markdown(f"~~**{reto['categoria']}:** {reto['descripcion']}~~ ✅")
                else:
                    st.markdown(f"**{reto['categoria']}:** {reto['descripcion']}")
            
            with col2:
                st.markdown(f"🎁 **{reto['puntos']} pts**")
            
            with col3:
                if completado:
                    st.success("Completado!")
                else:
                    if st.button("Completar", key=f"btn_{reto['id']}"):
                        st.session_state.puntos += reto['puntos']
                        st.session_state.retos_completados.add(reto['id'])
                        st.rerun()
            
            with col4:
                # Iconos según categoría
                iconos = {
                    "Hidratación": "💧",
                    "Alimentación": "🍎",
                    "Ejercicio": "🚶‍♂️",
                    "Salud": "❤️"
                }
                st.markdown(f"### {iconos.get(reto['categoria'], '🎯')}")
            
            st.markdown("---")

    # Sección de logros
    st.header("🏅 Tus Logros")

    logros_desbloqueados = []
    if st.session_state.puntos >= 50:
        logros_desbloqueados.append("🌱 **Principiante Saludable** - 50 puntos alcanzados")
    if st.session_state.puntos >= 150:
        logros_desbloqueados.append("🚀 **Intermedio Comprometido** - 150 puntos alcanzados")
    if st.session_state.puntos >= 300:
        logros_desbloqueados.append("💪 **Avanzado Ejemplar** - 300 puntos alcanzados")
    if len(st.session_state.retos_completados) >= 10:
        logros_desbloqueados.append("🔥 **Consistente** - 10 retos completados")

    if logros_desbloqueados:
        for logro in logros_desbloqueados:
            st.success(logro)
    else:
        st.info("¡Completa tus primeros retos para desbloquear logros!")

elif menu == "📊 Diagnóstico Personal":
    st.header("📊 Calcula Tu IMC")

    with st.expander("Haz tu diagnóstico personal", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            peso = st.slider("Peso (kg)", 30, 200, 70)
            altura = st.slider("Estatura (m)", 1.0, 2.5, 1.65)
        
        with col2:
            edad = st.number_input("Edad", 18, 100, 25)
            actividad = st.selectbox("Nivel de actividad", ["Sedentario", "Moderado", "Activo"])
        
        if st.button("🎯 Calcular Mi Salud", type="primary"):
            imc = peso / (altura**2)
            categoria, color, emoji = clasificar_imc(imc)
            meta = calcular_meta(imc)
            consejo = generar_consejo_local(imc)
            
            # Mostrar resultados
            st.subheader("📈 Resultados de tu IMC")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Tu IMC", f"{imc:.1f}")
            with col2:
                st.metric("Estado", f"{categoria} {emoji}")
            with col3:
                st.metric("Meta Recomendada", meta)
            
            # Gráfico de progreso
            st.plotly_chart(crear_grafico_progreso(imc), use_container_width=True)
            
            # Consejo local
            st.success(f"💡 **Consejo chihuahuense:** {consejo}")

elif menu == "💡 Consejos de Salud":
    mostrar_todos_consejos()

elif menu == "🔄 Reiniciar Progreso":
    st.header("🔄 Reiniciar Progreso")
    st.warning("Esta acción borrará todo tu progreso actual.")
    
    if st.button("⚠️ Confirmar Reinicio", type="primary"):
        st.session_state.puntos = 0
        st.session_state.retos_completados = set()
        st.success("¡Progreso reiniciado correctamente!")
        st.rerun()

# Pie de página
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "🍎 Aliméntate Bien Chihuahua - ¡Tu salud es tu mayor riqueza!"
    "</div>", 
    unsafe_allow_html=True
)
