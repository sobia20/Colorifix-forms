from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
from main import app

client = TestClient(app)

def test_show_data_file():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"data": {"parameter_types": ["string", "number", "bool", "select"], "forms": [{"label": "Register new pigment", "name": "request_colour", "description": "Record discovery of a new pigment", "parameters": [{"name": "pigment_name", "label": "Pigment name", "type": "string", "rerquired": "true"}, {"name": "origin", "label": "Organism of origin", "type": "string", "rerquired": "true"}, {"name": "available", "label": "Genome is available?", "type": "bool", "rerquired": "true"}]}, {
        "label": "Register a dye round", "name": "request_dyeing", "description": "Send a new dyeing request to the dyeing team", "parameters": [{"name": "colour", "label": "Colour used", "type": "select", "rerquired": "true", "options": ["Flamingo Pink", "Golden Yellow", "Swamp Green", "Cosmic Blue"]}, {"name": "fabric", "label": "Fabric used", "type": "select", "rerquired": "true", "options": ["Cotton", "Polyester", "Wool", "Silk"]}, {"name": "duration", "label": "Duration of the dye round (min)", "type": "number", "rerquired": "false"}]}]}, "form_names": [], "data_path": "./tests/test_data.json"}


def test_update_data():
    response = client.get("/update")
    assert response.status_code == 200
    assert response.json() == None
