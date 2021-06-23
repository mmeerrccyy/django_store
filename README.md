## Async Django store

This is online shop ELTEX.UA 

You can use this repository like template for yours web site.

### What we used

There is:
  * Python
  * Django
  * JavaScript
  * jQuery
  * RabbitMQ
  * Celery
  * SQLite
  * Bootstrap
 
### How to run

**You can run this site without RabbitMQ and Celery**

First of All download this repository.
```bash
git clone https://github.com/mmeerrccyy/eltexua_async.git
```

#### Running

```bash
cd eltexua_async
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

#### Create super user



```bash
python manage.py createsuperuser
```
And follow the instruction

#### Running with RabbitMQ and Celery

Download and install from [official website](https://www.rabbitmq.com/)

##### Run RabbitMQ Server

```bash
rabbitmq-server
```

##### Run Celery

**!!!You must be on venv!!!**

```bash
celery -A eltex_ua worker -l info
```

##### (Optional) Run Flower

**!!!You must be on venv!!!**

```bash
celery -A eltex_ua flower
```


