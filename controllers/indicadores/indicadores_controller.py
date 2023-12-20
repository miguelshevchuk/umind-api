def generarIndicadores(predicciones):
    indicadores = []
    sinManos(predicciones, indicadores)
    sinBrazos(predicciones, indicadores)
    sinNariz(predicciones, indicadores)
    sinBoca(predicciones, indicadores)
    sinPiernas(predicciones, indicadores)
    sinCabeza(predicciones, indicadores)
    sinOjos(predicciones, indicadores)
    brazosCortos(predicciones, indicadores)
    brazosLargos(predicciones, indicadores)
    manosGrandes(predicciones, indicadores)
    manosChicas(predicciones, indicadores)
    ojosChicos(predicciones, indicadores)
    cabezaChica(predicciones, indicadores)

    return indicadores

def sinPiernas(predicciones, indicadores):
    if len(predicciones["pierna"]) < 2:
        indicadores.append({
            "Indicador": "No se detectan piernas",
            "Descripcion": "Puede reflejar indefension ante ciertas situaciones"
        })
        indicadores.append({
            "Indicador": "No se detectan piernas",
            "Descripcion": "Puede ser indicador de conflictos para controlar impulsos hostiles"
        })
def sinManos(predicciones, indicadores):
    if len(predicciones["mano"]) < 2:
        indicadores.append({
            "Indicador": "No se detectan manos",
            "Descripcion": "Puede ser indicador de timidez y depresión"
        })
        indicadores.append({
            "Indicador": "No se detectan manos",
            "Descripcion": "Puede reflejar indefension ante ciertas situaciones y tendencias a sentirse insuficiente"
        })
        indicadores.append({
            "Indicador": "No se detectan manos",
            "Descripcion": "Puede reflejar sentimientos de inadecuación o culpa por no lograr actuar correctamente"
        })

def sinBrazos(predicciones, indicadores):
    if len(predicciones["brazo"]) < 2:
        indicadores.append({
            "Indicador": "No se detectan brazos",
            "Descripcion": "Puede indicar un pedido de ayuda del paciente"
        })
        indicadores.append({
            "Indicador": "No se detectan brazos",
            "Descripcion": "Puede indicar sentimientos de culpa y ansiedad con relación al mal uso o al pobre desempeño con brazos y manos"
        })
        indicadores.append({
            "Indicador": "No se detectan brazos",
            "Descripcion": "Puede reflejar sentimientos de ansiedad y culpa de conductas sociales inaceptables que implican los brazos o las manos"
        })

def sinNariz(predicciones, indicadores):
    if len(predicciones["nariz"]) == 0:
        indicadores.append({
            "Indicador": "No se detecta nariz",
            "Descripcion": "Puede ser indicador de ansiedad"
        })
        indicadores.append({
            "Indicador": "No se detecta nariz",
            "Descripcion": "Puede ser indicador de retraimiento y timidez"
        })
        indicadores.append({
            "Indicador": "No se detecta nariz",
            "Descripcion": "Puede ser indicador de aislamiento social"
        })
        indicadores.append({
            "Indicador": "No se detecta nariz",
            "Descripcion": "Puede ser indicador de infelicidad"
        })
def sinBoca(predicciones, indicadores):
    if len(predicciones["feliz"]) == 0:
        indicadores.append({
            "Indicador": "No se detecta boca",
            "Descripcion": "Puede ser indicador de inseguridad, falta de autoestima o confianza en si mismo"
        })
        indicadores.append({
            "Indicador": "No se detecta boca",
            "Descripcion": "Puede ser indicador de infelicidad"
        })
        indicadores.append({
            "Indicador": "No se detecta boca",
            "Descripcion": "Puede reflejar dificultad para comunicarse con los demas"
        })
        indicadores.append({
            "Indicador": "No se detecta boca",
            "Descripcion": "Puede reflejar sentimientos de angustia"
        })

def sinCabeza(predicciones, indicadores):
    if len(predicciones["cabeza"]) == 0:
        indicadores.append({
            "Indicador": "No se detecta cabeza",
            "Descripcion": "Puede ser indicador de desadaptacion social"
        })

def sinOjos(predicciones, indicadores):
    if len(predicciones["ojos"]) == 0:
        indicadores.append({
            "Indicador": "No se detectan ojos",
            "Descripcion": "Puede ser indicador de frustracion y falta de confianza en si mismo"
        })
        indicadores.append({
            "Indicador": "No se detectan ojos",
            "Descripcion": "Puede ser indicador de aislamiento social"
        })
        indicadores.append({
            "Indicador": "No se detectan ojos",
            "Descripcion": "Puede reflejar negación a los problemas, rechazo a enfrentar al mundo y escapar a la fantasía."
        })
def brazosCortos(predicciones, indicadores):
    if len(predicciones["brazo"]) > 1:
        brazoD = predicciones["brazo"][0]
        brazoI = predicciones["brazo"][1]
        torso = predicciones["torso"][0]
        if brazoD["alto"] <= torso["alto"]*0.60 or brazoI["alto"] <= torso["alto"]*0.60:
            indicadores.append({
                "Indicador": "Tamaño de brazos muy corto",
                "Descripcion": "Puede ser indicador de aislamiento social"
            })
            indicadores.append({
                "Indicador": "Tamaño de brazos muy corto",
                "Descripcion": "Puede ser indicador de ansiedad, retraimiento o infelicidad. Tambien tendencia a encerrarse en si mismo"
            })
            indicadores.append({
                "Indicador": "Tamaño de brazos muy corto",
                "Descripcion": "Puede reflejar necesidad de proteccion"
            })
            indicadores.append({
                "Indicador": "Tamaño de brazos muy corto",
                "Descripcion": "Puede reflejar dificultad del niño para comunicarse con el mundo circundante y las otras personas"
            })


def brazosLargos(predicciones, indicadores):
    if len(predicciones["brazo"]) > 1:
        brazoD = predicciones["brazo"][0]
        brazoI = predicciones["brazo"][1]
        torso = predicciones["torso"][0]
        if brazoD["alto"] >= torso["alto"] * 1.15 or brazoI["alto"] >= torso["alto"] * 1.15:
            indicadores.append({
                "Indicador": "Tamaño de brazos muy largos",
                "Descripcion": "Puede ser indicador de impulsividad, hostilidad y actitud agresiva hacia si mismo y/o el mundo"
            })

def manosGrandes(predicciones, indicadores):
    if len(predicciones["mano"]) == 2:
        mano1 = predicciones["mano"][0]
        mano2 = predicciones["mano"][1]
        torso = predicciones["torso"][0]
        print(mano1["alto"])
        print(torso["alto"])
        if mano1["alto"] >= torso["alto"] * 0.3 or mano2["alto"] >= torso["alto"] * 0.3:
            indicadores.append({
                "Indicador": "Tamaño de manos muy grande",
                "Descripcion": "Puede ser indicador de conductas agresivas"
            })
            indicadores.append({
                "Indicador": "Tamaño de manos muy grande",
                "Descripcion": "Pueden reflejar una conducta compensadora de sentimientos de inadecuación, insuficiencia manipuladora o dificultad para establecer contactos con otros."
            })

def manosChicas(predicciones, indicadores):
    if len(predicciones["mano"]) == 2:
        mano1 = predicciones["mano"][0]
        mano2 = predicciones["mano"][1]
        torso = predicciones["torso"][0]
        if mano1["alto"] <= torso["alto"] * 0.05 or mano2["alto"] <= torso["alto"] * 0.05:
            indicadores.append({
                "Indicador": "Tamaño de manos muy pequeño",
                "Descripcion": "Puede ser indicador de pedido de ayuda de parte del paciente"
            })



def ojosChicos(predicciones, indicadores):
    if len(predicciones["ojos"]) > 0:
        ojos = predicciones["ojos"][0]
        cabeza = predicciones["cabeza"][0]
        if ojos["alto"] <= cabeza["alto"] * 0.02 or ojos["ancho"] <= cabeza["ancho"] * 0.2:
            indicadores.append({
                "Indicador": "Tamaño de ojos muy pequeños",
                "Descripcion": "Puede ser indicador de sentimientos de rabia y frustración"
            })

def cabezaChica(predicciones, indicadores):
    if len(predicciones["cabeza"]) > 0:
        torso = predicciones["torso"][0]
        cabeza = predicciones["cabeza"][0]
        if cabeza["alto"] <= torso["alto"] * 0.4 or cabeza["ancho"] <= torso["ancho"] * 0.4:
            indicadores.append({
                "Indicador": "Cabeza muy pequeña",
                "Descripcion": "Puede ser indicador de sentimientos intensos de inadecuación intelectual"
            })
