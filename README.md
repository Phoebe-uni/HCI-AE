# HCI-AE-UofG Food
UofG Food is a website for students and staff at the University of Glasgow to monitor their calories intake and to communicate and learn about healthy diets. The site is based on a live update of the University canteen's daily menu, allowing users to like and rate dishes. Staff at the University canteen then adapt and modify the dishes based on user feedback.
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
