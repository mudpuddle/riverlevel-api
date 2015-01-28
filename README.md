# riverlevel-api

A simple python api built using [Flask](http://flask.pocoo.org/), used to access Northwest river level
data from the [NOAA Northwest River Forecast Center](http://www.nwrfc.noaa.gov).


## Running Locally

Make sure you have [Flask](http://nodejs.org/) ready to go.  I typically follow the virtualenv method.

Clone or fork this repo...

```sh
$ cd riverlevel-api
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python server.py
```

Your app should now be running on [127.0.0.1:5000](http://127.0.0.1:5000/).

## Deploying to Heroku

This api is currently setup to run on Heroku.  Make sure you have a [Heroku](https://www.heroku.com/) account
and the [Heroku Toolbelt](https://toolbelt.heroku.com/) set up.

```sh
$ heroku create
$ git push heroku master
$ heroku open
```

### ToDo
- Secure it.
