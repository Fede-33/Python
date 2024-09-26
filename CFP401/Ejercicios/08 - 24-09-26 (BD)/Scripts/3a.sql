/* Realiza una consulta que modifique el nombre de la ciudad de la fila 1. El nuevo nombre debe decir KABUL.*/ 

UPDATE ciudades
SET nombre = 'KABUL'
WHERE id = 1;

SELECT * FROM ciudades WHERE id = 1;