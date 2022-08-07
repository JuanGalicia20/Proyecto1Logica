import random

B = [{("q", True),  # Fórmula clausal
      ("p", True),
      ("p", False)},{}]

I = {}  # asignación parcial vacía


def seleccionar_literal(B):  # función para seleccionar la literal
    #for b in B:
     #   for literal in b:
      #      B2 = literal[0]
       #     return B2
    a= random.choice(B)
    L = random.choice(list(B[a]))
    return L


def DPLL(B, I={}):
    if not len(B):  # Si B es vacía
        return True, I  # retornamos true e I (asignación parcial)
    for b in range(len(B)):
        if not B[b]:  # Si hay una disyunción vacía en B
            return False, None  # retornamos false y none

    L = seleccionar_literal(B)
    BC = []  # Creamos B complemento
    for b in range(len(B)):  # para cada disyunción
        if (L, True) not in B[b]:  # Buscamos donde L no esté en B, para "eliminar" todas las cláusulas donde la L está en B
            # Empezamos a construir BC
            BC.append(B[b])  # agregamos todas las cláusulas donde B no contenga L
    for bc in BC:  # eliminaremos las ocurrencias en cada disyunción
        BC = bc.difference({(L, False)})  # buscamos la diferencia entre el conjunto BC y la cláusula de L complemento
    IC = {**I, **{L: True}}  # I’ = I ∪ {valor de L es verdadero}
    resultado, I1 = DPLL(BC, IC)
    if resultado is True:
        return True, I1

    for b in B:  # para cada disyunción
        if (L,
            False) not in b:  # Buscamos donde L complemento no esté en B, para "eliminar" todas las cláusulas donde la L complemento está en B
            # Empezamos a construir BC
            BC.append(b)  # agregamos todas las cláusulas donde B no contenga L complemento
    for bc in BC:  # eliminaremos las ocurrencias en cada disyunción
        BC = bc.difference({(L, True)})  # buscamos la diferencia entre el conjunto BC y la cláusula de L
    IC = {**I, **{L: False}}  # I’ = I ∪ {valor de L es falso}
    resultado, I2 = DPLL(BC, IC)
    if resultado is True:
        return True, I2

    return False, None
print(DPLL(B,I))   
    
