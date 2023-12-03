import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def desertores(df_anterior, df_posterior):
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

    # Convertir a string las variables: 'RBD', 'DGV_RBD', 'NOM_RBD', 'COD_REG_RBD', 'COD_PRO_RBD', 'COD_COM_RBD', 'NOM_COM_RBD', 'COD_DEPROV_RBD', 'NOM_DEPROV_RBD', 'COD_DEPE', 'COD_DEPE2', 'RURAL_RBD', 'ESTADO_ESTAB', 'COD_ENSE', 'COD_ENSE2', 'COD_ENSE3', 'COD_GRADO', 'COD_GRADO2', 'LET_CUR', 'COD_JOR', 'COD_TIP_CUR', 'COD_DES_CUR', 'MRUN', 'GEN_ALU', 'COD_REG_ALU', 'COD_COM_ALU', 'NOM_COM_ALU', 'COD_SEC', 'COD_ESPE', 'COD_RAMA', 'ENS', 'DESERTOR'
    desertores['RBD'] = desertores['RBD'].astype(str)
    desertores['DGV_RBD'] = desertores['DGV_RBD'].astype(str)
    desertores['NOM_RBD'] = desertores['NOM_RBD'].astype(str)
    desertores['COD_REG_RBD'] = desertores['COD_REG_RBD'].astype(str)
    desertores['COD_PRO_RBD'] = desertores['COD_PRO_RBD'].astype(str)
    desertores['COD_COM_RBD'] = desertores['COD_COM_RBD'].astype(str)
    desertores['NOM_COM_RBD'] = desertores['NOM_COM_RBD'].astype(str)
    desertores['COD_DEPROV_RBD'] = desertores['COD_DEPROV_RBD'].astype(str)
    desertores['NOM_DEPROV_RBD'] = desertores['NOM_DEPROV_RBD'].astype(str)
    desertores['COD_DEPE'] = desertores['COD_DEPE'].astype(str)
    desertores['COD_DEPE2'] = desertores['COD_DEPE2'].astype(str)
    desertores['RURAL_RBD'] = desertores['RURAL_RBD'].astype(str)
    desertores['ESTADO_ESTAB'] = desertores['ESTADO_ESTAB'].astype(str)
    desertores['COD_ENSE'] = desertores['COD_ENSE'].astype(str)
    desertores['COD_ENSE2'] = desertores['COD_ENSE2'].astype(str)
    desertores['COD_ENSE3'] = desertores['COD_ENSE3'].astype(str)
    desertores['COD_GRADO'] = desertores['COD_GRADO'].astype(str)
    desertores['COD_GRADO2'] = desertores['COD_GRADO2'].astype(str)
    desertores['LET_CUR'] = desertores['LET_CUR'].astype(str)
    desertores['COD_JOR'] = desertores['COD_JOR'].astype(str)
    desertores['COD_TIP_CUR'] = desertores['COD_TIP_CUR'].astype(str)
    desertores['COD_DES_CUR'] = desertores['COD_DES_CUR'].astype(str)
    desertores['MRUN'] = desertores['MRUN'].astype(str)
    desertores['GEN_ALU'] = desertores['GEN_ALU'].astype(str)
    desertores['COD_REG_ALU'] = desertores['COD_REG_ALU'].astype(str)
    desertores['COD_COM_ALU'] = desertores['COD_COM_ALU'].astype(str)
    desertores['NOM_COM_ALU'] = desertores['NOM_COM_ALU'].astype(str)
    desertores['COD_SEC'] = desertores['COD_SEC'].astype(str)
    desertores['COD_ESPE'] = desertores['COD_ESPE'].astype(str)
    desertores['COD_RAMA'] = desertores['COD_RAMA'].astype(str)
    desertores['ENS'] = desertores['ENS'].astype(str)
    desertores['DESERTOR'] = desertores['DESERTOR'].astype(str)

    estudiantes_regulares['RBD'] = estudiantes_regulares['RBD'].astype(str)
    estudiantes_regulares['DGV_RBD'] = estudiantes_regulares['DGV_RBD'].astype(str)
    estudiantes_regulares['NOM_RBD'] = estudiantes_regulares['NOM_RBD'].astype(str)
    estudiantes_regulares['COD_REG_RBD'] = estudiantes_regulares['COD_REG_RBD'].astype(str)
    estudiantes_regulares['COD_PRO_RBD'] = estudiantes_regulares['COD_PRO_RBD'].astype(str)
    estudiantes_regulares['COD_COM_RBD'] = estudiantes_regulares['COD_COM_RBD'].astype(str)
    estudiantes_regulares['NOM_COM_RBD'] = estudiantes_regulares['NOM_COM_RBD'].astype(str)
    estudiantes_regulares['COD_DEPROV_RBD'] = estudiantes_regulares['COD_DEPROV_RBD'].astype(str)
    estudiantes_regulares['NOM_DEPROV_RBD'] = estudiantes_regulares['NOM_DEPROV_RBD'].astype(str)
    estudiantes_regulares['COD_DEPE'] = estudiantes_regulares['COD_DEPE'].astype(str)
    estudiantes_regulares['COD_DEPE2'] = estudiantes_regulares['COD_DEPE2'].astype(str)
    estudiantes_regulares['RURAL_RBD'] = estudiantes_regulares['RURAL_RBD'].astype(str)
    estudiantes_regulares['ESTADO_ESTAB'] = estudiantes_regulares['ESTADO_ESTAB'].astype(str)
    estudiantes_regulares['COD_ENSE'] = estudiantes_regulares['COD_ENSE'].astype(str)
    estudiantes_regulares['COD_ENSE2'] = estudiantes_regulares['COD_ENSE2'].astype(str)
    estudiantes_regulares['COD_ENSE3'] = estudiantes_regulares['COD_ENSE3'].astype(str)
    estudiantes_regulares['COD_GRADO'] = estudiantes_regulares['COD_GRADO'].astype(str)
    estudiantes_regulares['COD_GRADO2'] = estudiantes_regulares['COD_GRADO2'].astype(str)
    estudiantes_regulares['LET_CUR'] = estudiantes_regulares['LET_CUR'].astype(str)
    estudiantes_regulares['COD_JOR'] = estudiantes_regulares['COD_JOR'].astype(str)
    estudiantes_regulares['COD_TIP_CUR'] = estudiantes_regulares['COD_TIP_CUR'].astype(str)
    estudiantes_regulares['COD_DES_CUR'] = estudiantes_regulares['COD_DES_CUR'].astype(str)
    estudiantes_regulares['MRUN'] = estudiantes_regulares['MRUN'].astype(str)
    estudiantes_regulares['GEN_ALU'] = estudiantes_regulares['GEN_ALU'].astype(str)
    estudiantes_regulares['COD_REG_ALU'] = estudiantes_regulares['COD_REG_ALU'].astype(str)
    estudiantes_regulares['COD_COM_ALU'] = estudiantes_regulares['COD_COM_ALU'].astype(str)
    estudiantes_regulares['NOM_COM_ALU'] = estudiantes_regulares['NOM_COM_ALU'].astype(str)
    estudiantes_regulares['COD_SEC'] = estudiantes_regulares['COD_SEC'].astype(str)
    estudiantes_regulares['COD_ESPE'] = estudiantes_regulares['COD_ESPE'].astype(str)
    estudiantes_regulares['COD_RAMA'] = estudiantes_regulares['COD_RAMA'].astype(str)
    estudiantes_regulares['ENS'] = estudiantes_regulares['ENS'].astype(str)
    estudiantes_regulares['DESERTOR'] = estudiantes_regulares['DESERTOR'].astype(str)

    
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

    # Convertir a string las variables: 'RBD', 'DGV_RBD', 'NOM_RBD', 'COD_REG_RBD', 'COD_PRO_RBD', 'COD_COM_RBD', 'NOM_COM_RBD', 'COD_DEPROV_RBD', 'NOM_DEPROV_RBD', 'COD_DEPE', 'COD_DEPE2', 'RURAL_RBD', 'ESTADO_ESTAB', 'COD_ENSE', 'COD_ENSE2', 'COD_ENSE3', 'COD_GRADO', 'COD_GRADO2', 'LET_CUR', 'COD_JOR', 'COD_TIP_CUR', 'COD_DES_CUR', 'MRUN', 'GEN_ALU', 'COD_REG_ALU', 'COD_COM_ALU', 'NOM_COM_ALU', 'COD_SEC', 'COD_ESPE', 'COD_RAMA', 'ENS', 'DESERTOR'
    desertores['RBD'] = desertores['RBD'].astype(str)
    desertores['DGV_RBD'] = desertores['DGV_RBD'].astype(str)
    desertores['NOM_RBD'] = desertores['NOM_RBD'].astype(str)
    desertores['COD_REG_RBD'] = desertores['COD_REG_RBD'].astype(str)
    desertores['COD_PRO_RBD'] = desertores['COD_PRO_RBD'].astype(str)
    desertores['COD_COM_RBD'] = desertores['COD_COM_RBD'].astype(str)
    desertores['NOM_COM_RBD'] = desertores['NOM_COM_RBD'].astype(str)
    desertores['COD_DEPROV_RBD'] = desertores['COD_DEPROV_RBD'].astype(str)
    desertores['NOM_DEPROV_RBD'] = desertores['NOM_DEPROV_RBD'].astype(str)
    desertores['COD_DEPE'] = desertores['COD_DEPE'].astype(str)
    desertores['COD_DEPE2'] = desertores['COD_DEPE2'].astype(str)
    desertores['RURAL_RBD'] = desertores['RURAL_RBD'].astype(str)
    desertores['ESTADO_ESTAB'] = desertores['ESTADO_ESTAB'].astype(str)
    desertores['COD_ENSE'] = desertores['COD_ENSE'].astype(str)
    desertores['COD_ENSE2'] = desertores['COD_ENSE2'].astype(str)
    desertores['COD_ENSE3'] = desertores['COD_ENSE3'].astype(str)
    desertores['COD_GRADO'] = desertores['COD_GRADO'].astype(str)
    desertores['COD_GRADO2'] = desertores['COD_GRADO2'].astype(str)
    desertores['LET_CUR'] = desertores['LET_CUR'].astype(str)
    desertores['COD_JOR'] = desertores['COD_JOR'].astype(str)
    desertores['COD_TIP_CUR'] = desertores['COD_TIP_CUR'].astype(str)
    desertores['COD_DES_CUR'] = desertores['COD_DES_CUR'].astype(str)
    desertores['MRUN'] = desertores['MRUN'].astype(str)
    desertores['GEN_ALU'] = desertores['GEN_ALU'].astype(str)
    desertores['COD_REG_ALU'] = desertores['COD_REG_ALU'].astype(str)
    desertores['COD_COM_ALU'] = desertores['COD_COM_ALU'].astype(str)
    desertores['NOM_COM_ALU'] = desertores['NOM_COM_ALU'].astype(str)
    desertores['COD_SEC'] = desertores['COD_SEC'].astype(str)
    desertores['COD_ESPE'] = desertores['COD_ESPE'].astype(str)
    desertores['COD_RAMA'] = desertores['COD_RAMA'].astype(str)
    desertores['ENS'] = desertores['ENS'].astype(str)
    desertores['DESERTOR'] = desertores['DESERTOR'].astype(str)

    
    # Año de df_anterior
    year = str(df_anterior['AGNO'].unique()[0])

    # Exportar en carpeta data/tablas un archivo csv identificando el AGNO del df_anterior con separador ;
    desertores.to_csv('data/tablas/estudiantes'+  year +'.csv', sep=';')