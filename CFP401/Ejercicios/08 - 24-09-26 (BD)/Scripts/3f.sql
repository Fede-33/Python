/*Otro un poco más difícil. Pasar a mayúsculas todas las ciudades cuyo código de país sea igual a DZA 
y cuya población sea mayor a 153106. Tener en cuenta que se debe usar el where en combinación con el AND.*/

UPDATE ciudades
SET nombre = UPPER(nombre) 
WHERE codigo_pais = 'DZA' AND poblacion > 153106;

SELECT * FROM ciudades WHERE codigo_pais = 'DZA';