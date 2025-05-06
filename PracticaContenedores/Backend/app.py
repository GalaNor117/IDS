from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import time
import pymysql
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
CORS(app)

# Configuración mejorada de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
    f"@{os.getenv('MYSQL_HOST', 'db')}/{os.getenv('MYSQL_DATABASE')}"
    "?charset=utf8mb4"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
    'pool_size': 5,
    'max_overflow': 10
}
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')

db = SQLAlchemy(app)

# Modelo de la tabla tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)

# Función para inicializar la base de datos con reintentos
def initialize_database():
    max_retries = 5
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            with app.app_context():
                db.create_all()
            print("✅ Conexión a la base de datos establecida")
            return True
        except OperationalError as e:
            print(f"⚠️ Intento {attempt + 1}/{max_retries}: Error de conexión - {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
        except Exception as e:
            print(f"⚠️ Error inesperado: {str(e)}")
            return False
    
    print("❌ No se pudo conectar a la base de datos después de varios intentos")
    return False

# Endpoints mejorados con manejo de errores
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        try:
            tasks = Task.query.all()
            return jsonify([{'id': task.id, 'title': task.title} for task in tasks])
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    elif request.method == 'POST':
        try:
            data = request.get_json()
            if not data or 'title' not in data:
                return jsonify({'error': 'Datos inválidos'}), 400
                
            new_task = Task(title=data['title'])
            db.session.add(new_task)
            db.session.commit()
            return jsonify({'message': 'Tarea agregada!', 'id': new_task.id}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Tarea eliminada!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if initialize_database():
        app.run(host='0.0.0.0', port=5000, debug=True)