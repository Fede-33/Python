import os

os.mkdir('./archivos_tablas')

for j in range(1,11):
    
    with open(f'./archivos_tablas/tabla_{j}.txt', 'w') as f: 
        f.write(f'Tabla del {j}\n')
    
    with open(f'./archivos_tablas/tabla_{j}.txt', 'a') as f:    
        for i in range(11):
            f.write(f'\n{j} X {i} = {i*j}')