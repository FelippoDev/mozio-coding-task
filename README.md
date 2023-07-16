# Mozio API Integration
Project created for the Mozio code challenge.


## Project Structure
```C:.
│   .env.example
│   .gitignore
│   README.md
│   requirements.txt
│   
└───app
    │   __main__.py
    │   
    ├───apis
    │   │   __init__.py
    │   │   
    │   └───mozio
    │           api.py
    │           api_second.py
    │           __init__.py
    │
    └───utils
            dummy.py
            __init__.py
```

Inside ```mozio``` folder, we have the API structure containing all theses three methods: *search*, *booking* and *cancelling*.
All methods are integrated from the Mozio API.
In the folder utils we have the ```dummy.py``` file, which is responsible for handling all the Dummy data for testing the API integration and for selecting the dummy data in the Mozio endpoints.


## How to Run the Code
1. Clone github repository in your local system ```git clone https://github.com/FelippoDev/mozio-coding-task.git```
2. Navigate to the project directory in your terminal
3. Create new virtual python environment ```python3 -m venv .venv```
4. Activate virtual python environment Linux: ```source venv/bin/activate``` Windows: ```.venv/Scripts/activate```
5. Install the APP dependencies ```pip install -r requirements.txt```
6. Create a ```.env``` containing all the needed environment variables to run the application, create the variables just like the variables inside ```.env.example```
7. At last, run the command ```python app```
