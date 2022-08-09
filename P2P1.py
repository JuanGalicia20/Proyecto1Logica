B= [[("r",True),("q",False)],
    [("q", False),("r",False)]
    ,[("p",False),("q",True),("r",False)]]

I={} #asignación parcial vacía

def seleccionar_literal(B): #función para seleccionar la literal 
    L=B[0][0][0]
    return L

def DPLL(B,I={}):
    if not B: #Si B es vacía
        return True, I #retornamos true e I (asignación parcial)
    for b in B:
        if not b: #Si hay una disyunción vacía en B
            return False, None #retornamos false y none 

    L=seleccionar_literal(B)
    BC = [] #Creamos B complemento
    """for b in B: #para cada disyunción
        if (L, True) not in b: #Buscamos donde L no esté en B, para "eliminar" todas las cláusulas donde la L está en B  
            #Empezamos a construir BC
            BC.append(b) #agregamos todas las cláusulas donde B no contenga L
    for bc in BC: #eliminaremos las ocurrencias en cada disyunción
        print(bc)
        BC = bc.difference({(L, False)}) #buscamos la diferencia entre el conjunto BC y la cláusula de L complemento
    """
    for b in B:
        if len([x for x in b if x == (L, True)])==0:
            BC.append([x for x in b if x != (L,False)])

    ##IC = {**I, **{L: True}} #I’ = I ∪ {valor de L es verdadero}
    resultado, I1 = DPLL(BC, {**I, **{L:True}})
    if resultado:
        return resultado, I1

    BC=[]
    """for b in B: #para cada disyunción
        if (L, False) not in b: #Buscamos donde L complemento no esté en B, para "eliminar" todas las cláusulas donde la L complemento está en B  
            #Empezamos a construir BC
            BC.append(b) #agregamos todas las cláusulas donde B no contenga L complemento
    for bc in BC: #eliminaremos las ocurrencias en cada disyunción
        BC = bc.difference({(L, True)}) #buscamos la diferencia entre el conjunto BC y la cláusula de L
    """
    for b in B:
        if len([x for x in b if x == (L, False)])==0:
            BC.append([[x for x in b if x != L]])
    #IC = {**I, **{L: False}} #I’ = I ∪ {valor de L es falso}
    resultado, I2 = DPLL(BC, {**I, **{L:False}})
    if resultado:
        return resultado, I2


    return False, None 
    
