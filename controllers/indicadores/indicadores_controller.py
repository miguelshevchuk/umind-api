def generarIndicadores(predicciones):
    indicadores = []
    sinManos(predicciones, indicadores)

    return indicadores

def sinManos(predicciones, indicadores):
    if len(predicciones["mano"]) == 0:
        indicadores.append({
            "Indicador": "No se detectan manos",
            "Descripcion": "Puede ser indicador de tendencia al retraimiento con dificultades para abrirse al exterior y con las otras personas"
        })

