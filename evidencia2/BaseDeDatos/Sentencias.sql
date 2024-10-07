-- Mostrar todos los datos
SELECT * FROM usuario;
-- Mostrar ID, nombre y apellido
SELECT idUsuario, nombre, apellido FROM usuario;
-- Mostrar el Id de los juegos de accion y shooter
SELECT * FROM categoria
	WHERE tipo = "accion" OR tipo = "shooter";
-- Mostrar todos los datos de los usuarios con ID entre 9 y 12
SELECT * FROM usuario
	WHERE idUsuario BETWEEN 9 AND 12;
-- Mostrar solo los 3 primeros ID con membresia estandard
SELECT * FROM usuario
	WHERE Membresia_idMembresia = 2 LIMIT 3;
-- Crear un nuevo usuario
INSERT INTO usuario (idUsuario,email,password,nombre,apellido,Membresia_idMembresia)
	VALUE
    (16,"Bati@gmail.com","goleador10","Gabriel","Batistuta",1);
-- Modificar la suscripcion del ultimo usuario agregado
UPDATE usuario
	SET Membresia_idMembresia = 2
    WHERE idUsuario = 16;
-- Eliminar el ultimo usuario agregado
DELETE FROM usuario
	WHERE idUsuario = 16;
-- Mostrar nombre, apellido y tipo de suscripcion (nombre de la suscripcion)
SELECT usuario.nombre, usuario.apellido, membresia.tipo FROM usuario
	INNER JOIN membresia
    ON usuario.Membresia_idMembresia = membresia.idMembresia;
-- Mostrar nombre, apellido y tipo de suscripcion (nombre de la suscripcion) solo los que sean Plus
SELECT usuario.nombre, usuario.apellido, membresia.tipo FROM usuario
	INNER JOIN membresia
    ON usuario.Membresia_idMembresia = membresia.idMembresia
    WHERE membresia.tipo = "plus";
-- Mostrar el nombre y apellido de cada usuario para cada compra y la fecha de la misma
SELECT compra.idCompra, usuario.nombre, usuario.apellido, compra.fecha FROM compra
	INNER JOIN usuario
    ON compra.Usuario_idUsuario = Usuario.idUsuario;


