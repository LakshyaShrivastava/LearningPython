# Useful python ORM Tools
import sqlalchemy as alch
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Create a database and the base class for our ORMs

engine = alch.create_engine("sqlite:///shelters.db", echo=False)
Base = declarative_base()

# Define ORMs

