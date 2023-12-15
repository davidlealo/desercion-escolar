import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def desertoresr(df_anterior, df_posterior):
    # Filtrar los estudiantes que no son prebásica o de educación para adultos
    desertores = df_anterior[(~df_anterior['COD_ENSE2'].isin([1, 3, 4, 6, 8]))]
    # print("Estudiantes regulares sin prebasica y adultos año anterior",desertores.shape)


    # Filtrar los estudiantes que no asisten a 4to medio el año a analizar
    desertores = desertores[~((desertores['COD_GRADO'] == 4) & (df_anterior['COD_ENSE2'].isin([5, 7])))]
    # print("Desertores sin 4to medio año anterior", desertores.shape)

    # Filtrar a los estudiantes df_posterior que no están en 'COD_ENSE2' 1, 3, 4, 6 y 8
    df_posterior = df_posterior[(~df_posterior['COD_ENSE2'].isin([1, 3, 4, 6, 8]))]
    # print("Estudiantes sistema regular año posterior",df_posterior.shape)

    # Verificar si los estudiantes están presentes en el archivo actual
    desertores = desertores[~desertores['MRUN'].isin(df_posterior['MRUN'].unique())]
    # print("Desertores año a analizar", desertores.shape)
    
    # Estudiantes que se mantienen en el sistema regular
    estudiantes_regulares = df_posterior[df_posterior['MRUN'].isin(df_anterior['MRUN'].unique())]
    # print("Estudiantes regulares año a analizar", estudiantes_regulares.shape)

    # Nueva columna que indica si el estudiante es desertor o no
    desertores['DESERTOR'] = 1
    estudiantes_regulares['DESERTOR'] = 0

    # Eliminar registros con valores ' ' en EDAD_ALU en df_anterior
    desertores = desertores[desertores['EDAD_ALU'] != ' ']
    estudiantes_regulares = estudiantes_regulares[estudiantes_regulares['EDAD_ALU'] != ' ']

    # Convertir EDAD_ALU a int
    desertores['EDAD_ALU'] = desertores['EDAD_ALU'].astype(int)
    estudiantes_regulares['EDAD_ALU'] = estudiantes_regulares['EDAD_ALU'].astype(int)

    
    # Año de df_anterior
    year = str(df_anterior['AGNO'].unique()[0])

    # Exportar en carpeta data/tablas dataframes a csv identificando el AGNO del df_anterior con separador ;
    desertores.to_csv('data/tablas/desertores'+  year +'.csv', sep=';')
    estudiantes_regulares.to_csv('data/tablas/regulares'+  year +'.csv', sep=';')


def estudiantes(df_anterior, df_posterior):
    # Filtrar los estudiantes que no son prebásica o de educación para adultos
    desertores = df_anterior[(~df_anterior['COD_ENSE2'].isin([1, 3, 4, 6, 8]))]
    # print("Estudiantes regulares sin prebasica y adultos año anterior",desertores.shape)


    # Filtrar los estudiantes que no asisten a 4to medio el año a analizar
    desertores = desertores[~((desertores['COD_GRADO'] == 4) & (df_anterior['COD_ENSE2'].isin([5, 7])))]
    # print("Desertores sin 4to medio año anterior", desertores.shape)

    # Filtrar a los estudiantes df_posterior que no están en 'COD_ENSE2' 1, 3, 4, 6 y 8
    df_posterior = df_posterior[(~df_posterior['COD_ENSE2'].isin([1, 3, 4, 6, 8]))]
    # print("Estudiantes sistema regular año posterior",df_posterior.shape)

    # Verificar si los estudiantes están presentes en el archivo actual
    desertores = desertores[~desertores['MRUN'].isin(df_posterior['MRUN'].unique())]
    # print("Desertores año a analizar", desertores.shape)
    
    # Nueva columna que indica si el estudiante es desertor o no
    desertores['DESERTOR'] = 1
    # Valores nulos de variable desertor = 0
    desertores['DESERTOR'] = desertores['DESERTOR'].fillna(0)

    # Eliminar registros con valores ' ' en EDAD_ALU en df_anterior
    desertores = desertores[desertores['EDAD_ALU'] != ' ']

    # Convertir EDAD_ALU a int
    desertores['EDAD_ALU'] = desertores['EDAD_ALU'].astype(int)

    
    # Año de df_anterior
    year = str(df_anterior['AGNO'].unique()[0])

    # Exportar en carpeta data/tablas un archivo csv identificando el AGNO del df_anterior con separador ;
    desertores.to_csv('data/tablas/estudiantes'+  year +'.csv', sep=';')