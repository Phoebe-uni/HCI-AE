# HCI-AE
A web application that enables users to connect with each other to exchange recipes and monitor calories, helping them to track their daily calorie intake and learn to share recipes to improve their lives.

### Setting up
To ensure that this web application works properly, the following steps need to be followed to set up the environment.
Clone the repository and accsess the proper directory.
```
$ git clone -----
$ cd -----
```

Creating and activating the virtual environment.
```
$ conda create -n ---- python=3.8.0
$ conda activate ----
```

Installing the necessary package dependencies
```
(lanex)$ pip install -r requirements.txt
```

Making migrations and migrating
```
(lanex)$ python manage.py makemigrations lanex
(lanex)$ python manage.py migrate
```

Run the population script
```
(lanex)$ python populate_lanex.py
```

Running the web application
```
(----)$ python manage.py runserver
```

After that, the link to web application is:

### Running tests
```
(lanex)$ python manage.py test lanex
```
