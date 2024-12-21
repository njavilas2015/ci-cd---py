"""Task management in ClickUp through an efficient and specific repository"""

from typing import Tuple, List, Dict, Any
from adapters.clickup_adapter import ClickUpAdapter


class ClickUpTaskRepository:
    """Task management in ClickUp through an efficient and specific repository"""

    def __init__(self):
        """Init Task management"""
        self.adapter = ClickUpAdapter()

    def move_task(self, id_task: str, state: str) -> Tuple[bool, str]:
        """Move task"""

        endpoint: str = f"task/{id_task}"

        data: dict[str, str] = {"status": state}

        status_code, response = self.adapter.put(endpoint, data)

        if status_code == 200:
            return True, f"Tarea {id_task} movida al estado '{state}'."

        return False, f"{status_code} - {response}"

    def get_tasks(self, list_id: str) -> Tuple[List[Dict[str, Any]], str]:
        """Get info task"""
        endpoint: str = f"list/{list_id}/task"

        status_code, response = self.adapter.get(endpoint)

        if status_code == 200:
            return response.get("tasks", []), ""

        return [], f"{status_code} - {response}"
