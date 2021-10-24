from sqlalchemy import Boolean, Column, String, Date, Integer
from sqlalchemy.orm import relationship, validates

from .database import Base

unit_types = ['tsp', 'tbsp', 'fl oz', 'cup', 'pt', 'qt', 'gal', 'ml', 'l', 'lb', 'oz', 'mg', 'g', 'kg']

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

# class Ingredient(Base):
#     __tablename__ = "ingredients"

#     name = Column(String, primary_key=True, index=True, nullable=False, unique=True)
#     unit = Column(String)
#     quantity = Column(Integer)
#     exp_date = Column(Date)
#     essential = Column(Boolean, default=False)

#     @validates('unit')
#     def validate_unit(self, key, unit):
#         if unit not in unit_types:
#             raise ValueError('Unit provided not in available unit types')
