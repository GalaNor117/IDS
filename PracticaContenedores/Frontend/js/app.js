document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    // Cargar tareas al iniciar
    fetchTasks();

    // Agregar nueva tarea
    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const task = { title: taskInput.value };
        fetch('http://localhost:5000/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(task)
        }).then(() => {
            taskInput.value = '';
            fetchTasks();
        });
    });

    // Cargar todas las tareas
    function fetchTasks() {
        fetch('http://localhost:5000/tasks')
            .then(response => response.json())
            .then(tasks => {
                taskList.innerHTML = '';
                tasks.forEach(task => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        ${task.title} 
                        <button onclick="deleteTask(${task.id})">Eliminar</button>
                    `;
                    taskList.appendChild(li);
                });
            });
    }

    // Eliminar tarea
    window.deleteTask = (id) => {
        fetch(`http://localhost:5000/tasks/${id}`, { method: 'DELETE' })
            .then(() => fetchTasks());
    };
});