# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:27:18 2016

v1
Coge txt de gastos (GASTOS.txt) para intentar organizarlos, pasandolo a CSV (salida.csv) separado por Comas

v1.1
Solicita el nombre de la salida

@author: Franky
"""
# Entrada: archivo GASTOS.txt
fichIn = open("C:/PROG/GASTOS.txt", encoding='UTF-8')
fichOut = open("C:/PROG/salida.csv", mode='w', encoding='UTF-8')

lineas = list(fichIn)
#  PARA VISUALIZAR EL CONTENIDO DEL ARCHIVO DE ENTRADA:
# print("IMPRIMIENDO FICHERO:")
# print(lineas)

cabecera = "DIA,SIGNO,IMPORTE,CONCEPTO\n"
fichOut.write(cabecera)

for temp in lineas:
    linea = temp.replace('  ', ' ')
    if linea.startswith('*'):
        dia = list(linea.rsplit(sep=' '))[1]
        diaMes = list(linea.rsplit(sep=' '))[2].replace(':','').replace('\n','')
        print("Día:", dia, diaMes)
    else:
        if linea.startswith(' \n') or linea.startswith('\n') or linea.startswith('#'):
            continue
        else:
            signo = linea.split(sep=' ')[1]
            importe = linea.split(sep=' ')[2]
            moneda = list(linea.split(sep=' '))[3]
            concepto = list(linea.split(sep='€'))[1]

        salida = dia + " " + diaMes + "," + signo + "," + importe + "," + concepto
        print(salida)
        fichOut.write(salida)

fichOut.close()
