# Colorifix Forms

![image](https://user-images.githubusercontent.com/23616603/110259932-e90d8c80-7fcb-11eb-947f-860bdfcd7c3b.png)

![image](https://user-images.githubusercontent.com/23616603/196010778-56fd1db4-5a39-48b2-b4a4-31a483ef2d8c.png)

![image](https://user-images.githubusercontent.com/23616603/196010787-2bb4f577-0e13-4d4f-ad45-a0e68e0734ee.png)

This is a web service for Colorifix researchers to fill in their latest findings as they are discovered.

Schema for all forms are given in a JSON config file called `data.json`.

The frontend is in [Vue.js](https://vuejs.org/) and backend uses [FastApi](https://fastapi.tiangolo.com/). 

Frontend is served via [nginx](https://www.nginx.com/).

Backend is served with [uvicorn](https://www.uvicorn.org/).

## Getting Started:

```
git clone https://github.com/sobia20/Colorifix-forms
cd Colorifix-forms
docker-compose up
```
The app would be running on your [localhost:8080](localhost:8080)
## Websocket Protocol:

The communication between frontend and backend occurs on /ws channel using JSON.
The key `action` dictates the required action:

`get-form-name`: Returns the list of all forms available.

`get-form-specs`: Returns the specifications of the chosen form.

`submit-form`: Sends form data to the server.

## Vue.js Frontend:

This flowchart explains the structure of the frontend components.

![image](https://user-images.githubusercontent.com/23616603/110260107-badc7c80-7fcc-11eb-9547-de15a82fcba4.png)


[Vuetify](https://vuetifyjs.com/en/) components are used for UI.

`/` redirects to `/forms`.
This displays the list of forms available.
Forms can be filtered using search bar.

Clicking on a form routes to the form specifications `localhost:8080/forms/:name`.

For example, `localhost:8080/forms/request_color`.


## FAST-API Backend:

The FastApi backend runs on Python 3.7.7.

Singleton `Data` Class, encapsulates how the backend interact with the schema file.

`/`:        The forms schema can be accessed.

`/update`:  The data is reloaded from the file (if schema is updated)

### Testing the app:

Tests reside in /tests directory. 

To test the app, simply run 

```
python -m pytest
```

Current coverage:
```
Name                 Stmts   Miss  Cover
----------------------------------------
__init__.py              0      0   100%
config.py                6      2    67%
data.py                 27      1    96%
main.py                 29     18    38%
tests/__init__.py        0      0   100%
tests/test_data.py      17      6    65%

```
 
