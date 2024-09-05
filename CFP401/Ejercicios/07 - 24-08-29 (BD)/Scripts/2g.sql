-- Liste todas las ciudades cuya población se encuentre entre 190000 y 200000.

SELECT * FROM ciudades g 
	WHERE poblacion >= 190000 
	AND poblacion <= 200000;