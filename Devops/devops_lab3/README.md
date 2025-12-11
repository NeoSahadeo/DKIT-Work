# Lab 3 - Devops

Create a python alternative for the Nginx server from last week (lab 2 07/10/2024).

## Install Flask

### What is Flask

Flask is a micro web framework.

**Most popular use cases:**

- REST api's
- Websites


### Basic Install

```
pip install flask
```

### Using a Virtual Environment

```
python -m venv .venv
\.venv\Scripts\activate
pip install flask
```

## Creating app1.py

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5001)
```

### Code explained

`from flask import Flask` - Imports a class from the `flask` library.

`app = Flask(__name__)` - Creates an instance of the `Flask` class called `app`. The variable `__name__` is used to identify  the file.

> The idea of the first parameter is to give Flask an idea of what belongs to your application.  This name is used to find resources on the filesystem, can be used by extensions to improve debugging information and a lot more.

`@app.route('/')` - Is a Python "wrapper" method called a decorator. This sets the endpoint '/' to whatever the function returns. In this case it would be the return value of `def index()`.

`return <h1>Hello world</h1>` - A string return value which is in HTML syntax.

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5001)
```

`__name__` is `__main__` if the file is run as a script. `__name__` will be the module name if the file is run as that.

## Creating the Dockerfile

```Dockerfile
FROM python
RUN pip install flask
COPY app1.py /root

WORKDIR /root

CMD ["python", "app1.py"]
```

### Code explained

`FROM python` - creates a new build stage from the `python` image. (https://hub.docker.com/_/python)

`RUN pip install flask` - run the pip package manager to install flask.

`COPY app1.py /root` - Copies `app1.py` from host to the docker image at `/root`.

`WORKDIR /root` - Sets the current directory of the image to `/root`.

`CMD ["python", "app1.py"]` - Runs the server (actual command `python app1.py`).

## Building the image

```bash
docker build -t devops_lab_3 .
```

## Starting the image

```bash
docker run --rm --name devops_lab_3_instance_1 -p 5001:5001 devops_lab_3
```

## TODO - Load Balancing
