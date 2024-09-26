/*Modificar la población de todas las ciudades cuyo código de país es ASM. La población debe ser igual a 3000.*/

UPDATE ciudades
SET poblacion = 3000
WHERE codigo_pais = 'ASM';

SELECT * FROM ciudades WHERE codigo_pais = 'ASM';