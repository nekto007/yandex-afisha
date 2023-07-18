# Interactive map

The project allows you to create "your" interactive map of locations (events).  


## Where to see and try

Demo version of the site is located [here](http://142.93.229.60/).

Ability to add or tweak a location, add images,  
description or title, swap images you can in  
[admin mode here](http://142.93.229.60/admin/places/place)  
(test login and password on request).


## How to install and run

Download the code from the repository.

Python3 should already be installed. Then use pip (or pip3 if there is a conflict with Python2) to install the dependencies:
```bash
pip install -r requirements.txt
```

#### Environment variables
The following environment variables will be needed to run the site:
```bash
SECRET_KEY=YOUR_SECRET_KEY
ALLOWED_HOSTS=127.0.0.0.1
```
The variables below are set by default, set your own if necessary
```bash
DEBUG=False
STATIC_URL=/static/
STATIC_ROOT=static
MEDIA_URL=/media/
MEDIA_ROOT=media
```

## How to run

Apply migrations:

```bash
python3 manage.py migrate
```
Create a SuperUser to access the admin area:
```bash
python3 manage.py createsuperuser
```

To run the site locally:
```
python3 manage.py runserver
```
Access to the admin area will be at: http://127.0.0.1:8000/admin/.


## Load Locations

Examples and templates of location descriptions to load are provided at this [resource](https://github.com/devmanorg/where-to-go-places.git).
You must use the command manager to upload:
```bash
python manage.py load_place place_url
```
where `place_url` is a link to the json data, [example](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9A%D0%BE%D0%B2%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D0%B3%20Gravity.json)


# Project Purpose

The code is written for educational purposes for an online course for web developers:  
[Devman - From Beginner to Middle Python/Django Developer](https://dvmn.org/t/middle-python-dev-before-you-finish-the-course/).
