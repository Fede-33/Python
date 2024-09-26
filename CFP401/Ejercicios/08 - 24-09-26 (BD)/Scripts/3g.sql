/*Otro un poco más y más difícil. Pasar a mayúsculas todas las ciudades cuyo distrito 
comience con el prefijo “Son”. El like puede ser un gran aliado.*/

UPDATE ciudades
SET nombre = UPPER(nombre) 
WHERE distrito LIKE 'Son%';

SELECT * FROM ciudades WHERE distrito LIKE 'Son%';