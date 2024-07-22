# This is the project of model of an electronics sales network With Django API

## Description

My Project is a web application designed to manage a network of electronic goods suppliers and retailers. It includes
features for creating and managing networks, tracking products, and handling supplier debts. This project is built using
Django and Django REST Framework.

The network is a hierarchical structure and has three types of networks:

1. Factory
2. Retail Network
3. Individual Entrepreneur

Each link in the network refers to only one equipment supplier (not necessarily the previous one in the hierarchy). It
is important to note that the hierarchy level is determined not by the name of the link, but by its relationship to
other elements of the network, i.e. the plant is always at level 0, and if the retail network relates directly to the
plant, bypassing other links, its level is 1.

Example: Factory #1 -> Retail Network #1 -> Retail Network #2 -> Individual Entrepreneur #1
so, Factory#1 level=0, Retail Network #1 level=1, Retail Network #2 level=2, Individual Entrepreneur #1 level=3

Remark: Factory always has 0 level

## Technical requirements

* Python 3.8+
* Django 3+
* DRF 3.10+
* PostgreSQL 10+

## Installation

Clone the repository:

```bash
   git clone https://github.com/munquzbek/trading_net.git
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install requirements.txt
```

Create a superuser:

```bash
python manage.py createsuperuser
```

or use custom command:

```bash
python manage.py csu
```

Run server

## Usage

1. Use Postman app or similar
2. Create and fill .env as in .env.sample file
3. Most perform you can also do in admin panel

```url
http://127.0.0.1:8000/admin/
```

There you can see Products, Networks, Users model change, create, filter, sort, perform an admin action to clear debt,
see links to supplier for each network as superuser

```bash
python3 manage.py loaddata fixtures/data.json
```

this code to load database with Network, Product, User data

```bash
pytest
```

this code to perform tests

```bash
flake8
```

this code to perform coverage

```bash
coverage report
```

check PEP-8 mistakes

### User

```url
http://127.0.0.1:8000/users/signup/
```

use this url to sign up in project

```url
http://127.0.0.1:8000/users/list/
```

list all users

```url
http://127.0.0.1:8000/users/update/1/
```

update user with 1 id

```url
http://127.0.0.1:8000/users/delete/1/
```

delete user with 1 id

### Network

```url
http://127.0.0.1:8000/network/
```

you can change the action to GET, PUT, POST, DELETE in postman to interact with course model

### Product

```url
http://127.0.0.1:8000/product/
```

you can change the action to GET, PUT, POST, DELETE in postman to interact with course model

### Documentation

```url
http://127.0.0.1:8000/swagger/
```

or

```url
http://127.0.0.1:8000/redoc/
```

use these two links to see documentations

## Thanks
