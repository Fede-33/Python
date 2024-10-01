/* La forma general de la sentencia DELETE es DELETE FROM nombre_de_tabla WHERE condición;
   La siguiente consulta elimina la ciudad cuyo ID es 3: 
   		DELETE FROM ciudades WHERE id = 3;
   La siguientes consultas eliminan la ciudad cuyo ID es 5 y 6:
		DELETE FROM ciudades WHERE id = 5 OR id = 6;
		DELETE FROM ciudades WHERE id IN (5, 6);

Si quieren saber qué es lo que van a eliminar con antelación pueden hacer un SELECT para
seleccionar todas las filas que cumplen con la condición WHERE.

Ejemplo: eliminar todas las filas cuyo nombre comienza con Tan o Las.
		 Antes de hacerlo me fijo que ciudades cumplen con el criterio anterior:
		 SELECT * FROM ciudades WHERE nombre like 'LAS%' OR nombre like 'TAN%';


