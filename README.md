# Project Title

Survey and Survey Response Demo (Built for
[Prolific](https://prolific.ac))

## About

This is a demo project built to provide an API for creating, amending
and viewing `Survey` and `SurveyResponse` objects. It was built using
[Django](https://docs.djangoproject.com/en/1.11/),
[Django-REST-framework](http://www.django-rest-framework.org/) as well
as [Markdown](https://pypi.org/project/Markdown/) for an easier
navigation of the API and
[Django-filter](https://pypi.org/project/django-filter/) to provide
out-of-the-box query support relying on Django's builtin ORM filtering.



### Features

- Allows the retrieval and creation of `Survey` instances
- Allows the filtering of `Survey` instances by `User`
- Allows the retrieval and creation of `SurveyResponse` instances
- Allows filtering of `SurveyResponse` instances by `Survey` and by
`User`
- Limits the number of `SurveyResponse` submissions to the number of
places specified in the parent `Survey` object's `available_places` field


### Mentions

Due to the fact that this has been built as a simple demo app, a few
things should be noted.

- There is little to no information actually held in the objects created
- There is no authentication required to access endpoints (although
auth is required to create new objects)
- Other than the API explorer there are no other pages

#### Going to production

In order for this project to become the foundation of a production-ready
web app, a few recommendations are made as follows:

- Change the db backend to something more robust, e.g. PostgreSQL, MySQL
, or a NoSQL database engine if needed
- Move valuable and sensitive information into a non-versioned file
(e.g. `local.py`); information to be stored here would be:
    - `SECRET_KEY`
    - Database connection details
    - `DEBUG` value, to allow test and production environments to run
    easily
    - `STATIC_URL`
    - `ALLOWED_HOSTS`
- Install and set up a web server, e.g. nginx, Apache2
- Set up static files to be served from the web server as opposed to the
web app itself
- If necessary, set up async task processors like `celery` to process
certain aspects asynchronously (e.g. email notifications for completed
surveys)
- Implement the use of API credentials to ensure only authorised parties
are able to navigate and manipulate the API

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

### Prerequisites

Create a virtual environment

```
user@my-machine:~/$ virtualenv prolific-demo
```

Once it has been created, activate it as such:

```
user@my-machine:~/$ source prolific-demo/bin/activate
```

### Installing

With the virtual environment activated, do the following:

1. Clone the repo from [here](https://github.com/virbose/prolific-demo)

```
user@my-machine:~/$ git clone https://github.com/virbose/prolific-demo.git
```

2. Navigate to the project root folder

```
user@my-machine:~/$ cd prolific-demo/
```

3. Run `pip` to install the project requirements

```
user@my-machine:~/$ pip install -r requirements.txt
```

4. Once the requirements have been installed, run the initial migrations

   (Note: this will create your copy of the SQLite database)

```
user@my-machine:~/$ python manage.py migrate
```

5. **RECOMMENDED** You should create a superuser so you can access the
Django admin as well as the API explorer

```
user@my-machine:~/$ python manage.py createsuperuser
```

Just follow the steps there

6. You can finally run your server and start exploring!

```
user@my-machine:~/$ python manage.py runserver
```

### Navigation

There are 3 main URLs to use for exploring:

- `/surveys/` will list all existing surveys or can be used to send
data to create a new `Survey`
- `/survey-responses/` will list all existing `SurveyResponse` objects
or post a new response
- `/profiles/` to list all existing `Member` objects (using just
Django's `AbstractUser` base class)

You can use an object ID after each to list a specific instance of that
model, e.g. `/surveys/1/` will only return the `Survey` with `pk=1`.

You can also use filtering as you would with a regular HTTP Request,
e.g. `/survey-responses/?survey=2` will return a list of all survey
responses for `Survey` with `pk=2`.

The above can be done to filter `Survey` and `SurveyResponse` objects
by `user`

## Versioning

I have used [git](https://git-scm.com/) for versioning and the entire project has been uploaded and maintained on [github](https://github.com/virbose/prolific-demo)

## Authors

* **Vlad Birtocian** - [virbose](https://github.com/virbose)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Many thanks to Prolific once again for giving me the change to work on
this demo for them.

