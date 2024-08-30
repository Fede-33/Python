SELECT * FROM ciudades i 
	WHERE poblacion >= 190000 
	AND poblacion <= 200000
	AND codigo_pais IN ("BRA", "ARG", "IND", "ITA");