from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all your models here so Alembic can detect them
from .user import User
from .task import Task
