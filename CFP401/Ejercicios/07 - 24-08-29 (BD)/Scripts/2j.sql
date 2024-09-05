/* Realice una consulta que liste solamente las ciudades cuyo nombre se encuentre entre las siguientes: 
   Buenos Aires, Rosario, Bahia, Asunción y Montevideo.*/

SELECT * FROM ciudades j WHERE nombre IN ("Buenos Aires", "Rosario", "Bahía Blanca", "Asunción", "Montevideo");