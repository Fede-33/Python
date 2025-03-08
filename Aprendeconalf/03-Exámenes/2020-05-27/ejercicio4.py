# El fichero horas-trabajo.csv contiene el número de horas mensuales trabajadas por los empleados de una empresa durante el primer cuatrimestre. Crear un programa que realice las siguientes operaciones utilizando la librería Pandas:

    #1 Crear un DataFrame leyendo el fichero desde internet con la url http://aprendeconalf.es/python/examenes/soluciones/examen-2020-05-27/horas-trabajo.csv. Obsérvese que el separador de campos es el punto y coma.
    
import pandas as pd

df = pd.read_csv('https://aprendeconalf.es/docencia/python/examenes/inteligencia-negocios/soluciones/examen-2020-05-27/horas-trabajo.csv', sep=';')
print(df)    
    #2 Mostrar por pantalla una serie con el número total de horas trabajadas para cada mes.
    
print(df[['Enero', 'Febrero', 'Marzo', 'Abril']].sum())

    #3 Mostrar por pantalla una serie con el número de operarios de cada departamento.
    
print(df[['Departamento']].value_counts())
    
    #4 Mostrar por pantalla el número de empleados que han trabajado todos los meses, es decir, que tienen un número de horas todos los meses del cuatrimestre.

df_todos_los_meses = df.dropna()
print(f'La cantidad de empleados que trabajaron todos los meses es: {len(df_todos_los_meses)}')    
    
    #5 Convertir el DataFrame a formato largo, de manera que todas las horas aparezcan en la misma columna.

df_largo = pd.melt(df, id_vars=['Id', 'Departamento'], var_name='Mes', value_name='Horas')    
print(df_largo)
    
    #6 Mostrar por pantalla una serie con el número medio de horas trabajadas en cada departamento.

df_horas_depto = df_largo.groupby('Departamento')[['Horas']].mean()
print(df_horas_depto)    
    
    #7 Mostrar por pantalla una serie con el total de horas trabajadas de cada operario.

df_horas_op = df_largo.groupby('Id')[['Horas']].sum()
print(df_horas_op)     

    #8 Mostrar por pantalla una serie con los salarios de todos los operarios ordenados de mayor a menor.

print(df_horas_op.sort_values(by='Horas', ascending=False))
