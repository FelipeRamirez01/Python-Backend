SELECT 
    tablas.guarderias.*,
    tablas.perros.nombre AS nombre_perro, tablas.perros.raza, tablas.perros.edad, tablas.perros.peso,
    tablas.cuidadores.nombre AS nombre_cuidador, tablas.cuidadores.celular
FROM 
    tablas.guarderias
JOIN 
    tablas.perros ON tablas.guarderias.id = tablas.perros.id_guarderia
JOIN 
    tablas.cuidadores ON tablas.perros.id_cuidador = tablas.cuidadores.id
WHERE 
    tablas.guarderias.nombre = 'La favorita';