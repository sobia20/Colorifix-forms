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

![alt text](https://github.com/sobia20/Colorifix-forms/blob/main/readme.png)

Vuetify is used for designing and UI.

`localhost:8080/` redirects to `localhost:8080/forms`.
This displays the list of forms available.
We can filter the form through a search bar as well.

Clicking on a form routes to the form specifications `localhost:8080/forms/:name`.

For example, `localhost:8080/forms/request_color`.


## Backend:

Python 3.7.7 is used. The architecture follows Singleton design pattern.
There is a class Data in data.py that has an object created once which can be imported to reuse wherever needed in the application.

On `/`, JSON data from the file is hosted

If there is any change in data, we can cater to that by going to `/update` and back to `/`. The changes would be added to `/`.

A refresh on the frontend would sync the data.

### Testing the app:

Tests reside in /tests directory. 
To test the app, simply run 

> python -m pytest

This will run the test cases. To view coverage report, 

> coverage report

## Running the app:

Clone the repository,

>git clone https://github.com/sobia20/Colorifix-forms

>cd Colorifix-forms

And start the container,

>docker-compose up

 The frontend is using nginx server and fast api is using uvicorn. 
