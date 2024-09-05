-- Listar todas las ciudades cuyo nombre comienza con la A y terminan con la o.

SELECT * FROM ciudades 
	WHERE nombre LIKE 'A%' 
	AND nombre LIKE '%o';