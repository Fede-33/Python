/* Liste todas las ciudades cuya población se encuentre entre 190000 y 200000 y el código de país 
   es BRA, ARG, IND o ITA. Investigue sobre la sentencia IN.*/

SELECT * FROM ciudades i 
	WHERE poblacion >= 190000 
	AND poblacion <= 200000
	AND codigo_pais IN ("BRA", "ARG", "IND", "ITA");