/* Eliminar todas las ciudades cuya cantidad de población sea menor a 5000
   el distrito contenga la cadena ‘la’ y el código del país sea CCK. 
   Ayuda, deben usar el operador lógico AND y deben utilizar el LIKE 
   para determinar la existencia de la cadena ´la´ en el nombre del distrito.*/

DELETE FROM ciudades 
	WHERE poblacion < 5000
	AND distrito LIKE '%la%'
	AND codigo_pais = 'CCK';