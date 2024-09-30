from fastapi import HTTPException;
from routes import router;
from models.vehicle import Vehicle;
import requests;

@router.get("/vehicles/")
def list_all_vehicles():
    url = 'https://swapi.dev/api/vehicles/';
    vehicles = [];

    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        vehicles.extend(data['results']);
        url = data['next'];

    return vehicles;

def get_vehicle(vehicle_id: int):
    if vehicle_id < 1 or vehicle_id > 39:
        raise HTTPException(status_code=400, detail="ID deve ser um número entre 1 e 39.");
    
    url = f'https://swapi.dev/api/vehicles/{vehicle_id}/';
    response = requests.get(url);

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Veículo não encontrado.");

    response.raise_for_status();
    vehicle_data = response.json();

    vehicle = Vehicle(
        id=vehicle_id,
        name=vehicle_data['name'],
        model=vehicle_data['model'],
        manufacturer=vehicle_data['manufacturer'],
        cost_in_credits=vehicle_data['cost_in_credits'],
        length=vehicle_data['length'],
        max_atmosphering_speed=vehicle_data['max_atmosphering_speed'],
        crew=vehicle_data['crew'],
        passengers=vehicle_data['passengers'],
        cargo_capacity=vehicle_data['cargo_capacity'],
        vehicle_class=vehicle_data['vehicle_class']
    );

    return vehicle;

@router.get("/vehicles/{vehicle_id}")
def get_vehicle_data(vehicle_id: int):
    return get_vehicle(vehicle_id);

@router.get("/vehicles/{vehicle_id}/save")
def save_vehicle_data(vehicle_id: int):
    vehicle = get_vehicle(vehicle_id);
    vehicle.createTable();  # Cria a tabela se não existir
    vehicle.save();
    
    return f'Veículo \'{vehicle.name}\' salvo no banco de dados.';

@router.get("/vehicles/{vehicle_id}/delete")
def delete_vehicle_data(vehicle_id: int):
    vehicle = get_vehicle(vehicle_id);
    vehicle.createTable();  # Cria a tabela se não existir
    vehicle.delete();
    
    return f'Veículo \'{vehicle.name}\' removido do banco de dados.';
