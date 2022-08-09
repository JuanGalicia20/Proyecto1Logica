def seleccionar_literal(B): #función para seleccionar la literal
    B2=B[0][0].replace("-","")
    return B2

def DPLL(B,I={}):
    if len(B)==0: #Si B es vacía
        return True, I #retornamos true e I (asignación parcial)
    for b in B:
        if len(b)==0: #Si hay una disyunción vacía en B
            return False, None #retornamos false y none

    L=seleccionar_literal(B)
    BC = [] #Creamos B complemento
    for b in B: #para cada disyunción
        if len([x for x in b if x == L])==0:
            BC.append([x for x in b if x != ("-"+L)])
    IC = {**I, **{L: True}} #I’ = I ∪ {valor de L es verdadero}
    resultado, I1 = DPLL(BC, IC)
    if resultado is True:
        return True, I1

    BC=[]
    for b in B:
        if len([x for x in b if x == ("-"+L)])==0:
            BC.append([x for x in b if x != L])
    IC = {**I, **{L: False}} #I’ = I ∪ {valor de L es falso}
    resultado, I2 = DPLL(BC, IC)
    if resultado is True:
        return True, I2


    return False, None
    
