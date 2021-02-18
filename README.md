Fyyur
-----

### Introduction

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.


### Test the functionality of this project

To start and run the local development server,

1. Clone this repo:
    ```
    $ git clone https://github.com/ahmed96-sudo/Fyyur-Musical-Website
    ```

2. Install the dependencies:
    ```
    $ pip3 install -r requirements.txt
    ```

3. Make migrations:
    ```
    $ flask db migrate
    $ flask db upgrate
    ```

4. Run the development server:
    ```
    $ FLASK_APP=app.py flask run
    ```

5. Navigate to Home page [http://localhost:8080](http://localhost:808)