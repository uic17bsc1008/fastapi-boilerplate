# FastAPI Project Setup Guidelines Using Our Boilerplate

```bash
git clone https://github.com/uic17bsc1008/fastapi-boilerplate.git
cd fastapi-boilerplate
```

# 1 - Create `.env` in your project directory.

```
DB_USER='your_db_username'
DB_PASSWORD='your_db_password'
DB_HOST='127.0.0.1'
DB_PORT='5432'
DB_NAME='your_db_name'
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

# 2 - Create virtualenv for your project

```bash
python3 -m venv .venv
```

- Active your `virtualenv`

```bash
source .venv/bin/activate
```

# 3 - Run your `requirements.txt` file inside your project.

```bash
pip install -r requirements.txt
```

# 4 - Database Model Setup and Registration

### Step - 1

- Create a new database model file (e.g., `user.py`)

### Step - 2

- Inherit the `Model` model from `base.py` in the model you want to create.

```python
from sqlalchemy import Column, Integer, String
from models.base import Model


class User(Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

```

### Step - 3

- Register your model in `main.py` so the tables are created in the database.

```python
from models.user import User
from models.product import Product

@app.on_event('startup')
async def on_startup():
    User.metadata.create_all(engine) # Registered User
    Product.metadata.create_all(engine) # Registered Product
```

- Now You're all set. Thank you for visiting us!
