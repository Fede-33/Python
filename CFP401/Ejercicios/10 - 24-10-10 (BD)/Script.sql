-- Intentar una búsqueda general con el siguiente comando:

SELECT(COUNT(*)) FROM ciudades, paises 

-- Devuelve el valor 946328, que resulta ser el producto cartesiano de ambas tablas (4079*232)

/* En esta nueva versión de la BD tenemos dos tablas. Si queremos consultar por todos los registros
   pero no queremos que se repitan los valores, debemos igualar el ID (Foreign Key) mediante la 
   sentencia WHERE: */

SELECT * FROM ciudades, paises 
	WHERE ciudades.pais_id = paises.id_pais;

