from . import router;
import requests;

@router.get("/")
def status():
    response = requests.get('https://swapi.dev/api/');
    response.raise_for_status();
    return f"Status da API \'{response.reason}\'"