
-- Insertar datos guarderia
INSERT INTO tablas.guarderias (nombre, direccion, telefono) VALUES 
('La favorita','Calle Siempre viva No 123',8352705),
('Happy','Calle Siempre Triste No 456',8357895);

-- Insertar datos cuidador
INSERT INTO tablas.cuidadores (nombre, celular, id_guarderia) VALUES 
('Felipe',3203656015,1), 
('Mario',3005173589,1), 
('Julian',3208105196,2);

-- Insertar datos perros
INSERT INTO tablas.perros (nombre, raza, edad, peso, id_cuidador, id_guarderia) VALUES
('Max', 'Labrador', 3, 22.5, 1, 1),
('Bella', 'Golden Retriever', 2, 24.0, 2, 1),
('Rocky', 'Bulldog', 4, 18.3, 3, 1),
('Luna', 'Poodle', 1, 5.2, 1, 1),
('Lassie', 'Beagle', 5, 12.1, 2, 1),
('Lucy', 'Chihuahua', 3, 3.0, 3, 1),
('Buddy', 'Pug', 2, 7.5, 1, 1),
('Daisy', 'Shih Tzu', 4, 6.7, 2, 1),
('Bailey', 'Boxer', 3, 28.4, 3, 1),
('Molly', 'German Shepherd', 2, 30.5, 1, 1),
('Cooper', 'Cocker Spaniel', 4, 14.2, 2, 1),
('Lassie', 'Rottweiler', 3, 35.7, 3, 1),
('Oliver', 'Dachshund', 2, 8.9, 1, 1),
('Zoe', 'Doberman', 5, 40.3, 2, 1),
('Toby', 'Pit Bull', 1, 30.0, 3, 1),
('Lily', 'Pomeranian', 4, 4.8, 1, 1),
('Duke', 'Great Dane', 2, 45.2, 2, 1),
('Lassie', 'Basset Hound', 3, 20.6, 3, 1),
('Leo', 'Border Collie', 4, 22.1, 1, 1),
('Nala', 'Mastiff', 3, 55.3, 2, 1);