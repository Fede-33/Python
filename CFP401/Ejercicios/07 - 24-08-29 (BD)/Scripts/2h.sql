-- Liste todas las ciudades cuya población se encuentre entre 190000 y 200000 y el código de país es BRA.

SELECT * FROM ciudades h 
	WHERE poblacion >= 190000 
	AND poblacion <= 200000
	AND codigo_pais = "BRA";