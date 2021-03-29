tabla = {} 

"""
Formato diccionario
{
    q0: {a:"q1,a,>",b:"...",...}
}
"""

# ===== Funciones ========

def direccion(d):
    if(d == ">"):
        return "D"
    elif(d == "<"):
        return "I"
    else:
        return "-"

def getColumns(dic):

    columnas = set()
    for key in dic:
        for k in dic[key]:
            columnas.add(k)
    columnas = list(columnas)
    columnas.sort()
    return columnas


def toString(t):
    return t[0]+","+t[1]+","+t[2]

def createTable(row,col,t):
    tabla = " "
    for c in col:
        c = blanco(c)
        tabla+="& ${}$ ".format(c)
    tabla+="\\\\ \\hline \n"
    for r in row:
        tabla+="${}$ ".format(r)
        for c in col:
            if c in t[r]:
                tabla+="& $({})$ ".format(t[r][c])
            else:
                tabla+="& $-$ "
        tabla+="\\\\ \\hline \n"
    return tabla

def blanco(t):
    if(t == "_"): 
        return "B"
    return t

#====== Main Program ==========

file = input("File name: ")
output = input("File output: ")

i = 0

with open(file) as f:
    lines = f.readlines()
    while(i < len(lines)-1):
        # fila y columna de la tabla
        claves = lines[i].strip()
        claves = claves.split(",")
        # data de la casilla
        transicion = lines[i+1].strip()
        transicion = transicion.split(",")
        transicion[-1] = direccion(transicion[-1]) #Corregir icono de direccion
        transicion[1] = blanco(transicion[1])
        if(claves[0] not in tabla):
            tabla[claves[0]] = {}
        tabla[claves[0]][claves[1]] = toString(transicion)
        i+=3 # saltar datos y linea en blanco

columnas = getColumns(tabla)
row = list(tabla.keys())

with open(output,'w') as f:
    f.write(createTable(row,columnas,tabla))

print("Terminado")


