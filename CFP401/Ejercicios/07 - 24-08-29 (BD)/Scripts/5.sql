/* Busquen información sobre la sentencia GROUP BY y HAVING. 
   Este tipo de sentencias se utilizan para agrupar resultados 
   y para aplicar restricciones sobre estos resultados. 
   Por ejemplo, pruebe esta consulta:*/

SELECT COUNT(nombre) 'Se repite x veces', nombre 'Nombre' FROM ciudades 
	GROUP BY nombre 
	HAVING COUNT(nombre) > 1;
