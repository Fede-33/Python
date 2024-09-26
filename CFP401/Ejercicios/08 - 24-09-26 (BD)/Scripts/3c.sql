/*Modifica el nombre de la ciudad cuyo id es igual a 3. 
El nuevo nombre debe ser: HERAT y la población debe ser igual a: 186888.*/

UPDATE ciudades
SET nombre = 'HERAT', poblacion = 186888
WHERE id = 3;

SELECT * FROM ciudades WHERE id = 3;