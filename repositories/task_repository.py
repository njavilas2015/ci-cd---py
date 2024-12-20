from adapters.clickup_adapter import ClickUpAdapter
from typing import Tuple, List, Dict, Any


class ClickUpTaskRepository:
    def __init__(self):
        self.adapter = ClickUpAdapter()

    def move_task(self, id_task: str, state: str) -> Tuple[bool, str]:
        endpoint = f"task/{id_task}"
        data = {"status": state}

        status_code, response = self.adapter.put(endpoint, data)

        if status_code == 200:
            return True, f"Tarea {id_task} movida al estado '{state}'."
        else:
            return False, f"{status_code} - {response}"

    def get_tasks(self, list_id: str) -> Tuple[List[Dict[str, Any]], str]:
        endpoint = f"list/{list_id}/task"
        status_code, response = self.adapter.get(endpoint)

        if status_code == 200:
            return response.get("tasks", []), ""
        else:
            return [], f"{status_code} - {response}"
