# LeadHit test task for Junior Python developer position

## How to run application

## Python 3.12 and TinyDB were used

- Clone repo

```git clone git@github.com:AlexanderUp/leadhit.git```

- Change dir to leadhit

```cd leadhit```

- Create virtual environment

```python3 -m venv venv```

- Activate virtual environment

```source venv/bin/activate```

- Install dependencies (no development dependencies like flake8, etc.)

```python3 -m pip install -r requirements/requirements_base.txt```

- Install dependencies (with development dependencies like flake8, etc.)

```python3 -m pip install -r requirements/requirements_dev.txt```

- Run server at ```http://127.0.0.1:8000```

```uvicorn main:app```

- Target endpoint is available at

```http://127.0.0.1:8000/get_form```

## Running test scripts

- Make script executable

```chmod +x ./test_script.sh```

- Run script

```test_script.sh```
