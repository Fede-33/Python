/* Elabore una consulta que liste todas las ciudades cuyo nombre sea alguno de los siguientes: 
   Buenos Aires, Rosario, Bahia, Asunción y Montevideo o tenga una población mayor a 9000000.*/

SELECT * FROM ciudades l 
	WHERE nombre IN ("Buenos Aires", "Rosario", "Bahía Blanca", "Asunción", "Montevideo")
	OR poblacion > 9000000;