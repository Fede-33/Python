SELECT * FROM ciudades l 
	WHERE nombre IN ("Buenos Aires", "Rosario", "Bahía Blanca", "Asunción", "Montevideo")
	OR poblacion > 9000000;