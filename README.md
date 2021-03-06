# Colorifix Forms

This is a web service for Colorifix researchers to fill in their latest findings as they are discovered.

The schema for each form is dynamically generated from a JSON config file called `data.json`.

The frontend is Vue.js and backend is FAST API. Websockets are used for the communication between frontend and backend.

The communication occurs on /ws channel using JSON with key `action` determining which of the three tasks should the server perform.

`get-form-name`: Returns the list of all forms available.

`get-form-specs`: Returns the specifications of the chosen form.

`submit-form`: Sends form data to the server.

## Frontend:

This flowchart explains the structure of the app.

![alt text](https://github.com/sobia20/Colorifix-forms/readme.png)

For designing and UI, Vuetify is used.

`localhost:8080/` redirects to `localhost:8080/forms`.
This displays the list of forms available.
We can filter the form through a search bar as well.

Clicking on a form routes to the form specifications `localhost:8080/forms/{form_name}`.

For example, `localhost:8080/forms/request_color`.

## Backend:

Python 3.8.2 is used. The architecture follows Singleton design pattern.
There is a class Data in data.py that has an object created once which can be imported to reuse wherever needed in the application.

On `/`, JSON data from the file is hosted.

If there is any change in data, we can cater to that by going to `/update` and back to `/`. The changes would be added to `/`.

On `/{name}`, individual form data is visible. For example, `/request_color`.

## How to run the app:

Clone the repository,

>`git clone https://github.com/sobia20/Colorifix-forms`

To start the <b>frontend</b>, 

>`cd Colorifix-forms/frontend/colorifix_forms_frontend`

To install dependencies,

>`npm install`

To run the server in dev mode,

>`npm run serve`

To start <b>backend</b>

>`cd Colorifix-forms/backend` 

Activate the python virtual environment,

>`source env/bin/activate`

And to start the server,
>`uvicorn main:app --reload`

# Or

>`docker-compose up`