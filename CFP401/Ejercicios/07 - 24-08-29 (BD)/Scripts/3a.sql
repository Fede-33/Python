/* Realice una consulta que liste todas las ciudades pero los nombres de las columnas deben ser:
CIUDAD | COD. PAIS | DISTRITO | HABITANTES*/

SELECT 
	id as " ",
	nombre as "CIUDAD", 
	codigo_pais as "COD. PAIS", 
	distrito as "DISTRITO", 
	poblacion as "HABITANTES" 
FROM ciudades; 