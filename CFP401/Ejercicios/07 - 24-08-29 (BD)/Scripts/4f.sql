-- Determine el total de habitantes de las ciudades de Buenos Aires y Montevideo.

SELECT SUM(poblacion) FROM ciudades 
	WHERE nombre = 'Buenos Aires' 
	OR nombre = 'Montevideo';