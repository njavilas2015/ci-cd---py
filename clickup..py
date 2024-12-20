import requests
from requests import Response

API_URL = "https://api.clickup.com/api/v2"
API_TOKEN = "TOKEN_CLICKUP" 
HEADERS = {
    "Authorization": API_TOKEN
}

def move_task(id_task: str, state: str):
    url: str = f"{API_URL}/task/{id_task}"
    data = {
        "status": state
    }
    response = requests.put(url, headers=HEADERS, json=data)

    if response.status_code == 200:
        print(f"Tarea {id_task} movida al estado '{state}'.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def get_tasks(id: str):
    url: str = f"{API_URL}/list/{id}/task"

    response: Response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        tasks = response.json()
        return tasks["tasks"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

if __name__ == "__main__":
    ID_LISTA = "tu_id_lista_aquí"

    tasks = get_tasks(ID_LISTA)

    if tasks:
        print("Tareas obtenidas:")
        for task in tasks:
            print(f"- {task['name']} (ID: {task['id']})")
    else:
        print("No se encontraron tareas o hubo un error.")
