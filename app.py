import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta

RETOS_DIARIOS = [
    {"id": 1, "descripcion": "Toma 8 vasos de agua hoy", "puntos": 10, "categoria": "Hidratación"},
    {"id": 2, "descripcion": "Consume 2 frutas locales", "puntos": 15, "categoria": "Alimentación"},
    {"id": 3, "descripcion": "Camina 30 minutos", "puntos": 20, "categoria": "Ejercicio"},
    {"id": 4, "descripcion": "Prepara una comida con ingredientes locales", "puntos": 25, "categoria": "Cocina"},
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
    valores = [17, 22, 27, 35]  # Valores representativos
    colors = ["#FF6B6B", "#4ECDC4", "#FFA726", "#EF5350"]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=categorias,
        y=[1, 1, 1, 1],
        marker_color=colors,
        opacity=0.3,
        name="Rangos IMC"
    ))
