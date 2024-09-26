/*Todas las ciudades cuyo id sean: 4074, 4075, 4076, 4077, 4078, 4079 
deben tener la misma población, debe ser: 36000.*/

UPDATE ciudades
SET poblacion = 36000 
WHERE id BETWEEN 4074 AND 4079;

SELECT * FROM ciudades WHERE id BETWEEN 4074 AND 4079;