import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    ciudad = Column(String(250), nullable=False)
    slogan = Column(String(250), nullable=False)



class Videojuego(Base):
    __tablename__ = 'videojuego'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    rate = Column(Integer, nullable=False)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    empresa = relationship(Empresa)


class Consola(Base):
    __tablename__ = 'consola'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    precio = Column(Integer, nullable=False)


class ConsolaVideojuego(Base):
    __tablename__ = 'consola_videojuego'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    consola_id = Column(Integer, ForeignKey('consola.id'))
    consola = relationship(Consola)
    videojuego_id = Column(Integer, ForeignKey('videojuego.id'))
    videojuego = relationship(Videojuego)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
