/* Listar las ciudades cuyo nombre es Córdoba o Alexandria. Repasen el concepto OR. 
   Ambas condiciones deben expresarse en la sentencia WHERE.*/

SELECT * FROM ciudades e 
	WHERE nombre = "Córdoba"
	OR nombre = "Alexandria";