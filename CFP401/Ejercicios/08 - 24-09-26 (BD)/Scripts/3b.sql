/*Modifica el nombre de la ciudad cuyo id es igual a 2. El nuevo nombre debe ser: QANDAHAR.*/

UPDATE ciudades
SET nombre = 'QANDAHAR'
WHERE id = 2;

SELECT * FROM ciudades WHERE id = 2;