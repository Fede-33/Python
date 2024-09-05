-- Liste todas las ciudades que terminan con el sufijo “ndo” o “rlo”.

SELECT * FROM ciudades 
	WHERE nombre LIKE '%ndo' 
	OR nombre LIKE '%rlo';