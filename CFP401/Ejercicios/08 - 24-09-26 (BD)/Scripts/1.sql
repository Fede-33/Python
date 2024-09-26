--Ejecute la sentencia: 
SELECT COUNT(1) FROM ciudades;

--Esa consulta retorna el total de filas de la tabla ciudades. Anota ese número. Luego ejecuta la sentencia insert:
INSERT INTO ciudades (id, nombre, codigo_pais, distrito, poblacion)
VALUES (NULL, 'Carmen de Patagones', 'ARG', 'Patagones', 13847);

--Nuevamente ejecute la sentencia: 
SELECT COUNT(1) FROM ciudades;

/*Anote ese número ¿Qué conclusión saca al respecto? ¿qué sucedió en la tabla ciudades?
Lo que ocurrió es que se agregó una nueva fila a la tabla ciudades. 
Eso provocó que el total de filas se incrementara en uno. 
No obstante quedan muchas consultas para destacar en la sentencia insert. 
Cuestiones a analizar:
¿Qué valor tiene la columna ID? 
Recuerda que esa columna es la clave primaria de la tabla, es decir es la columna que no se repite, 
identifica a cada fila. La nueva ciudad “Carmen de Patagones” tiene un ID no hay duda pero ¿cuál?
Análisis:
¿Cómo determino qué valor tiene el ID de la localidad “Carmen de Patagones”?
¿Por qué el campo ID en la sentencia insert se puso NULL?
¿Qué efecto provoca ese NULL?*/
SELECT * FROM ciudades WHERE nombre = 'Carmen de Patagones';

--El ID de Carmen de Patagones se autonumeró a 4080.

--Ejecute esta sentencia: 
INSERT INTO ciudades (id, nombre, codigo_pais, distrito, poblacion)
VALUES (33, 'Carmen de Patagones', 'ARG', 'Patagones', 13847);

/*y determine qué ocurre. Sacar conclusiones:
Se genera un error porque el ID 33 ya está ocupado.
