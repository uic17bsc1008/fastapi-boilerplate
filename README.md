# Work in Progress................

# More about database models

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
