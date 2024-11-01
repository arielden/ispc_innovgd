
-- Se muestran solo estas columnas en la tabla usuario
SELECT idUsuario, email, nombre, apellido, Membresia_idMembresia FROM usuario;

-- Se muestra el Id y nombre de los juegos con categorias "accion" y "shooter"
SELECT j.idJuego, j.nombre, c.tipo
FROM juego j
JOIN categoria c ON j.Categoria_idCategoria = c.idCategoria
WHERE c.tipo = 'accion' OR c.tipo = 'shooter';

-- Se muestran los usuarios con ID entre 9 y 12
SELECT idUsuario, email, nombre, apellido FROM usuario
WHERE idUsuario BETWEEN 9 AND 12;

-- Se muestran los 3 primeros usuarios con membresia estandard
SELECT idUsuario, email, nombre, apellido FROM usuario
WHERE Membresia_idMembresia = 2 LIMIT 3;

-- Se crea un nuevo usuario
INSERT INTO usuario (idUsuario, email, password, nombre, apellido, Membresia_idMembresia, fecha_creacion)
VALUES (16, "Bati@gmail.com", "goleador10", "Gabriel", "Batistuta", 1, CURRENT_TIMESTAMP);

-- Se modifica la suscripcion del ultimo usuario agregado
UPDATE usuario
SET Membresia_idMembresia = 2, fecha_modificacion = CURRENT_TIMESTAMP
WHERE idUsuario = 16;

-- Se elimina el ultimo usuario agregado
DELETE FROM usuario
WHERE idUsuario = 16;

-- Se muestra nombre, apellido y tipo de suscripcion
SELECT usuario.nombre, usuario.apellido, membresia.tipo
FROM usuario
JOIN membresia ON usuario.Membresia_idMembresia = membresia.idMembresia;

-- En tabla carrito: se agregan campos de timestamp
ALTER TABLE carrito
ADD COLUMN fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN fecha_modificacion DATETIME ON UPDATE CURRENT_TIMESTAMP;

-- Tabla carrito_has_juego: se agregan campos de timestamp
ALTER TABLE carrito_has_juego
ADD COLUMN fecha_adicion DATETIME DEFAULT CURRENT_TIMESTAMP;

-- Tabla compra: se ajusta para permitir múltiples juegos
CREATE TABLE compra_detalle (
    idDetalle INT AUTO_INCREMENT PRIMARY KEY,
    Compra_idCompra INT,
    Juego_idJuego INT,
    precio DECIMAL(10, 2),
    FOREIGN KEY (Compra_idCompra) REFERENCES compra(idCompra),
    FOREIGN KEY (Juego_idJuego) REFERENCES juego(idJuego)
);

-- Tabla membresia: se agrega verificación para el campo descuento
ALTER TABLE membresia
ADD CONSTRAINT chk_descuento CHECK (descuento >= 0 AND descuento <= 100);

