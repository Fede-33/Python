/*Vamos con uno más difícil. Modificar el distrito de todas las ciudades cuyo código de país es ASM. 
El distrito se debe pasar a mayúsculas, es decir, ahora debe ser igual a: TUTUILA.*/

UPDATE ciudades
SET distrito = UPPER(distrito) 
WHERE codigo_pais = 'ASM';

SELECT * FROM ciudades WHERE codigo_pais = 'ASM';