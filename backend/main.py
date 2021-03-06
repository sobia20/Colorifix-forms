from fastapi import FastAPI, WebSocket
from data import data_model
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def show_data_file():
    '''Displays data on /'''
    return data_model


@app.get("/update")
def update_data():
    '''Loads data again when routed to /update'''
    data_model.load_data()


@app.websocket("/ws")
async def get_form_name(websocket: WebSocket):
    '''Establishes connection with frontend through websockets and responds to each action'''
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        data = json.loads(data)
        if data['action'] == 'get-form-name':
            await websocket.send_json(data_model.get_all_form_names())
        elif data['action'] == 'get-form-specs':
            await websocket.send_json(get_form_specs(data['name']))
        elif data['action'] == 'submit-form':
            del data['action']
            await websocket.send_text(submit_form(data['form_name'], data))


@app.get('/{name}')
def get_form_specs(name: str):
    '''Returns the selected form's specification'''
    return data_model.get_specs(name)


def submit_form(name: str, data: json):
    '''Receives data from the user'''
    print('Submitted form data', name, data)
    return 'Form specs data received'
