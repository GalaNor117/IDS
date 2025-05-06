-- Crear la base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS dockeroque;
USE dockeroque;

-- Crear tabla 'tasks' para el CRUD
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Opcional: Insertar datos de ejemplo
INSERT INTO tasks (title) VALUES 
    ('Aprender Docker'),
    ('Crear API con Flask'),
    ('Configurar MySQL');