# Flaskr

A basic blog application called Flaskr. Users will be able to register, log in, create posts, and edit or delete their own posts.

## Install

Clone the repository:
```bash
$ git clone git@github.com:shektor/flask-tutorial.git
$ cd flask-tutorial
```

Create a virtualenv and activate it:
```bash
$ python3 -m venv env
$ . env/bin/activate
```

Install package requirements:
```bash
$ pip install -r requirements.txt
```

Configure environment variables:
```bash
$ touch .env

# Add following lines to .env file and save
FLASK_APP=flaskr
FLASK_ENV=development
```

Initialize the database:
```bash
$ flask init-db
```

## Run

```bash
$ flask run
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.
