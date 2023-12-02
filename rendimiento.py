import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def analisis_rendimiento(df_anterior, df_posterior, r_anterior):
    # Filtrar los estudiantes que no son prebásica o de educación para adultos
    desertores = df_anterior[(~df_anterior['COD_ENSE2'].isin([1, 3, 4, 6, 8]))]
    print("Estudiantes regulares sin prebasica y adultos año anterior",desertores.shape)


    # Filtrar los estudiantes que no asisten a 4to medio el año a analizar
    desertores = desertores[~((desertores['COD_GRADO'] == 4) & (df_anterior['COD_ENSE2'].isin([5, 7])))]
    print("Estudiantes sin 4to medio año anterior", desertores.shape)

    # Filtrar a los estudiantes df_posterior que no están en 'COD_ENSE2' 1, 3, 4, 6 y 8
    df_posterior = df_posterior[(~df_posterior['COD_ENSE2'].isin([1, 3, 4, 6, 8]))]
    print("Estudiantes sistema regular año posterior",df_posterior.shape)

    # Verificar si los estudiantes están presentes en el archivo actual
    desertores = desertores[~desertores['MRUN'].isin(df_posterior['MRUN'].unique())]
    print("Desertores año a analizar", desertores.shape)
    
    # Estudiantes que se mantienen en el sistema regular
    estudiantes_regulares = df_posterior[df_posterior['MRUN'].isin(df_anterior['MRUN'].unique())]
    print("Estudiantes regulares año a analizar", estudiantes_regulares.shape)

    # Rendimiento estudiantes desertores
    r_desertores = desertores.merge(r_anterior, on='MRUN')
    print("Shape desertores rendimiento", r_desertores.shape)

    # Rendimiento estudiantes regulares
    r_estudiantes_regulares = estudiantes_regulares.merge(r_anterior, on='MRUN')
    print("Shape estudiantes regulares rendimiento",r_estudiantes_regulares.shape)

    # Transformación 'PROM_GRAL' a float
    r_desertores['PROM_GRAL'] = r_desertores['PROM_GRAL'].str.replace(',', '.').astype(float)
    r_estudiantes_regulares['PROM_GRAL'] = r_estudiantes_regulares['PROM_GRAL'].str.replace(',', '.').astype(float)

    # Describe desertores 'PROM_GRAL'
    desc_desertores = r_desertores['PROM_GRAL'].describe()
    print("ESTUDIANTES DESERTORES:",desc_desertores)
    year = str(df_anterior['AGNO'].unique()[0])
    desc_desertores.to_csv('data/tablas/describe_desertores'+  year +'.csv')


    # Describe estudiantes regulares 'PROM_GRAL'
    desc_estudiantes_regulares = r_estudiantes_regulares['PROM_GRAL'].describe()
    print("ESTUDIANTES REGULARES",desc_estudiantes_regulares)
    desc_estudiantes_regulares.to_csv('data/tablas/describe_regulares'+  year +'.csv')


    # Agregamos una nueva columna 'Tipo' a cada DataFrame
    r_desertores['Tipo'] = 'Desertor'
    r_estudiantes_regulares['Tipo'] = 'Regular'

    # Concatenamos ambos DataFrames
    df_rendimiento = pd.concat([r_desertores, r_estudiantes_regulares])
    display(df_rendimiento.head())
    # Exportamos el DataFrame a un archivo Excel
    # year = str(df_anterior['AGNO'].unique()[0])
    # df_rendimiento.to_csv('data/tablas/rendimiento' + year + '.csv', index=False)


    # Creamos el boxplot con seaborn
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Tipo', y='PROM_GRAL', data=df_rendimiento)
    plt.title('Boxplot del rendimiento de estudiantes regulares y desertores')
    plt.show()

    # Estadísticas de 'PROM_GRAL' agrupadas por 'Tipo'
    estadisticas_prom_gral = df_rendimiento.groupby('Tipo')['PROM_GRAL'].describe()

    print("Estadísticas de PROM_GRAL por tipo de estudiante:\n", estadisticas_prom_gral)
    estadisticas_prom_gral.to_csv('data/tablas/estadisticas_prom_gral' + year + '.csv')

    # Estadisticas de 'ASISTENCIA' agrupadas por 'Tipo'
    estadisticas_asistencia = df_rendimiento.groupby('Tipo')['ASISTENCIA'].describe()
    estadisticas_asistencia.to_csv('data/tablas/estadisticas_asistencia' + year + '.csv')

    # Histograma de 'PROM_GRAL' por 'Tipo'
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_rendimiento, x='PROM_GRAL', hue='Tipo', kde=True)
    plt.title('Distribución del rendimiento de estudiantes regulares y desertores')
    plt.show()



    # Porcentaje de asistencia 'ASISTENCIA' estudiantes desertores 
    print("Porcentaje de asistencia estudiantes desertores", r_desertores['ASISTENCIA'].value_counts(normalize=True))
    print(r_desertores['ASISTENCIA'].describe())
    # Exportar a Excel
    # r_desertores['ASISTENCIA'].to_excel('data/rendimiento/2019/asistencia_desertores.xlsx')

    # Porcentaje de asistencia 'ASISTENCIA' estudiantes regulares
    print("Porcentaje de asistencia estudiantes regulares", r_estudiantes_regulares['ASISTENCIA'].value_counts(normalize=True))
    print(r_estudiantes_regulares['ASISTENCIA'].describe())

    # Concatenamos ambos DataFrames
    df_asistencia = pd.concat([r_desertores, r_estudiantes_regulares])
    display(df_asistencia.head())

    # Creamos el boxplot con seaborn
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Tipo', y='ASISTENCIA', data=df_asistencia)
    plt.title('Boxplot de la asistencia de estudiantes regulares y desertores')
    plt.show()

    # Crear una tabla de contingencia para 'Tipo' y 'ASISTENCIA'
    tabla_contingencia = pd.crosstab(df_asistencia['Tipo'], df_asistencia['ASISTENCIA'])

    display("Tabla de contingencia:\n", tabla_contingencia)

    # Crear una tabla de contingencia normalizada para 'Tipo' y 'ASISTENCIA'
    tabla_contingencia_normalizada = pd.crosstab(df_asistencia['Tipo'], df_asistencia['ASISTENCIA'], normalize='index')

    display("Tabla de contingencia normalizada:\n", tabla_contingencia_normalizada)
