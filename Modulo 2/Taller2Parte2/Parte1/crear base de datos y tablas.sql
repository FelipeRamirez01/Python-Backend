-- Crear base de datos
CREATE DATABASE tablas;

-- Crear tabla Guarderia
CREATE TABLE tablas.guarderias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono INT
);

-- Crear tabla Cuidadores
CREATE TABLE tablas.cuidadores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    celular VARCHAR(15) NOT NULL,
    id_guarderia INT,
    FOREIGN KEY (id_guarderia) REFERENCES guarderias(id) ON DELETE SET NULL
);

-- Crear tabla Perro
CREATE TABLE tablas.perros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    raza VARCHAR(50),
    edad INT,
    peso DECIMAL(5,2),
    id_cuidador INT,
    id_guarderia INT,
    FOREIGN KEY (id_cuidador) REFERENCES cuidadores(id) ON DELETE SET NULL,
    FOREIGN KEY (id_guarderia) REFERENCES guarderias(id) ON DELETE SET NULL
);
