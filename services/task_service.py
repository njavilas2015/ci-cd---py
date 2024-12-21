from repositories.task_repository import ClickUpTaskRepository


class ClickUpTaskService:
    def __init__(self):
        self.task_repository = ClickUpTaskRepository()

    def move_task(self, id_task: str, state: str):

        success, message = self.task_repository.move_task(id_task, state)

        if success:
            print(f"Tarea {id_task} movida al estado '{state}'.")
        else:
            print(f"Error al mover la tarea: {message}")

    def get_tasks(self, list_id: str):

        tasks, error = self.task_repository.get_tasks(list_id)

        if error:
            print(f"Error al obtener las tareas: {error}")
            return []
        return tasks
