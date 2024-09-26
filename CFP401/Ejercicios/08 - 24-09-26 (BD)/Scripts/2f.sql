/*Inserte una localidad que contenga los siguientes datos:
nombre Villalonga, codigo_pais ARG, distrito Buenos Aires.
Observe que ha sucedido en este último caso, saque conclusiones.*/

INSERT INTO ciudades (id, nombre, codigo_pais, distrito)
VALUES (NULL, 'Villalonga', 'ARG', 'Buenos Aires');

SELECT * FROM ciudades WHERE nombre = 'Villalonga';

/*Agregó el registro y la población es 0 