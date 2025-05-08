# IDS
Repositorio para la practica de contenedores

Aplicación web completa con arquitectura de microservicios usando Docker, Flask (Backend), MySQL (DB) y Nginx (Frontend).

📦 Estructura del Proyecto
proyecto/
├── backend/
│   ├── app.py              # API Flask
│   ├── requirements.txt    # Dependencias Python
│   └── Dockerfile
├── frontend/
│   ├── index.html          # Interfaz web
│   ├── css/
│   ├── js/
│   └── Dockerfile
├── docker-compose.yml      # Orquestación de contenedores
└── .env.example            # Plantilla de variables de entorno


🔧 Requisitos Previos
Docker 20.10+

Docker Compose 2.0+

Python 3.9+ (solo para desarrollo local)

🚀 Instalación
Clonar repositorio:

bash
git clone https://github.com/tu-usuario/tu-proyecto.git
cd tu-proyecto
Configurar entorno:

bash
cp .env.example .env
# Editar .env con tus credenciales
Iniciar servicios:

bash
docker-compose up --build

🌐 Acceso a los Servicios

Servicio	URL Local	Puerto	Descripción
Frontend	http://localhost	80	Interfaz web
Backend	http://localhost:5000	5000	API REST
MySQL	-	3306 (solo interno)	Base de datos

⚙️ Variables de Entorno (env)
Clave	Descripción	Ejemplo

MYSQL_ROOT_PASSWORD	Contraseña root de MySQL	SuperSecret123!
MYSQL_DATABASE	Nombre de la DB	app_db
MYSQL_USER	Usuario de aplicación	app_user
MYSQL_PASSWORD	Contraseña de aplicación	AppPass456!
FLASK_SECRET_KEY	Clave para sesiones Flask	TuClaveSecretaAquí

🛠️ Comandos Útiles

bash
# Reconstruir contenedores
docker-compose up --build

# Detener servicios
docker-compose down

# Ver logs del backend
docker-compose logs backend

# Acceder a MySQL
docker-compose exec db mysql -u app_user -p

# Eliminar todo (incluidos volúmenes)
docker-compose down -v
