"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    import pandas as pd
    import re
    filename = 'clusters_report.txt'
    clusters = open(filename, mode='r')
    texto=clusters.readlines()
    for j in range(0,len(texto)):
        texto[j]=texto[j].strip()
    texto=texto[4:len(texto)]
    texto=[line.replace(" %","") for line in texto]
    texto=[line.replace(".\n",".") for line in texto]
    texto=[re.sub(r"(\S) {2,}", r"\1 ",line) for line in texto]
    #texto=[re.sub(r"([0-9]+.)", r"\1 ",line) for line in texto]
    texto=[re.sub(r"([0-9]+[,]+[0-9])", r"\1 ",line) for line in texto]
    texto=[re.sub(r"([0-9]+) ([0-9]+) ([0-9]+[,]+[0-9])", r"\1  \2  \3",line) for line in texto]
    p=0
    perp=list()
    base=pd.DataFrame()
    for j in range(0,len(texto)):
        pop=texto[j].strip().split("  ")
        if len(pop)>1:
            for i in range(0,len(pop)):
                if(pop[i].strip()!=""):
                    if(i==0):
                        base.loc[p,"cluster"]=int(pop[0].strip())
                    elif(i==1):
                        base.loc[p,"cantidad_de_palabras_clave"]=int(pop[1].strip())
                    elif(i==2):
                        base.loc[p,"porcentaje_de_palabras_clave"]=float(pop[2].strip().replace(",","."))
                    elif(i==3):
                        perp.append(pop[3].strip())  
        elif(len(pop)==1 and pop[0]!=""):
            perp.append(pop[0])  
        elif(pop[0]==""):
            base.loc[p,"principales_palabras_clave"]=" ".join(perp).replace(".","")
            perp=list()
            p=p+1
    df=base
    return df
