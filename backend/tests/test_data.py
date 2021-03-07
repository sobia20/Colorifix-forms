import pytest
from data import data_model
from config import TEST_DATA_PATH

@pytest.fixture
def get_data_model():
    '''Returns the data_model object'''
    data_model.data_path = TEST_DATA_PATH
    data_model.load_data()
    return data_model


def test_flush_cache(get_data_model):
    '''Tests if the data is being flushed'''
    get_data_model.flush_cache()
    assert get_data_model.data == {}, get_data_model.form_names == []


def test_get_all_form_names(get_data_model):
    '''Tests if Name of all available forms are returned from get_all_form_names'''
    form_list = get_data_model.get_all_form_names()
    assert form_list == [{'label': 'Register new pigment', 'name': 'request_colour'}, {
        'label': 'Register a dye round', 'name': 'request_dyeing'}]


def test_get_specs(get_data_model):
    '''Tests if specifications of a form is being returned from get_specs if we pass the name of that form'''
    form_specs = get_data_model.get_specs('request_dyeing')
    assert form_specs == {"label": "Register a dye round", "name": "request_dyeing", "description": "Send a new dyeing request to the dyeing team", "parameters": [{"name": "colour", "label": "Colour used", "type": "select", "rerquired": "true", "options": [
        "Flamingo Pink", "Golden Yellow", "Swamp Green", "Cosmic Blue"]}, {"name": "fabric", "label": "Fabric used", "type": "select", "rerquired": "true", "options": ["Cotton", "Polyester", "Wool", "Silk"]}, {"name": "duration", "label": "Duration of the dye round (min)", "type": "number", "rerquired": "false"}]}
