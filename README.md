
### Installation

1. Clone the repo
`git clone https://github.com/oksanaaam/airline-software.git`
2. Open the project folder in your IDE
3. Open a terminal in the project folder
4. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```


### Set up the SQLite database and run server
Run the database migrations to create the necessary tables in the SQLite database
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
The ZipAirlines software is now running and can be accessed at http://localhost:8000/api/airline/.


### Usage
1. Open a web browser and go to http://localhost:8000 to access the ZipAirlines software.

2. To input information about airplanes, click on the "Airplanes" link in the navigation menu.

3. On the airplanes page, you can view a list of existing airplanes and their details. To add a new airplane, click on the "Add Airplane" button.

4. Fill in the required fields for the new airplane, including the ID (a unique identifier for the airplane) and the number of passengers.

5. Click the "Save" button to create the airplane. The software will automatically calculate the fuel tank capacity, fuel consumption per minute, and maximum minutes able to fly based on the provided information.

6. To view the list of created airplanes and their details, you can navigate back to the airplanes page by clicking on the "Airplanes" link in the navigation menu.

7. On the airplanes page, you will see a table displaying the list of airplanes, including their ID, passenger count, fuel tank capacity, fuel consumption per minute, and maximum minutes able to fly.

8. You can also edit or delete existing airplanes by clicking on the corresponding buttons in the table.

### API Documentation
The ZipAirlines software also provides a RESTful API for managing airplanes. The API allows you to perform CRUD operations (Create, Read, Update, Delete) on the airplanes.

API Endpoint: http://localhost:8000/api/airline/airplanes/

Methods:

GET: Retrieves the list of airplanes and their details.
POST: Creates a new airplane with user-defined ID and passenger assumptions.
PUT: Updates the details of an existing airplane.
DELETE: Deletes an existing airplane.
Data Format: The API accepts and returns data in JSON format.

### API Documentation
The ZipAirlines software also provides a RESTful API for managing airplanes.

API Endpoint: http://localhost:8000/api/airline/airplanes/

Methods:

GET: Retrieves the list of airplanes and their details.
POST: Creates a new airplane with user-defined ID and passenger assumptions.

Data Format: The API accepts and returns data in JSON format.

Test Coverage : 98%
You can check it 
```
coverage run manage.py test
coverage report
```

Authentication: No authentication is required to access the API in this setup.

Please refer to the API documentation or use tools like cURL or Postman to interact with the API endpoints and perform the desired operations.