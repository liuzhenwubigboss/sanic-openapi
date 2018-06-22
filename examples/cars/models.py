from datetime import date

from sanic_openapi.doc import String, Boolean, Integer


class Manufacturer:
    name = String('name')
    start_date = date


class Driver:
    name = String('name')
    birthday = date


class Car:
    on = Boolean('on')
    doors = Integer('doors')
    color = String('color')
    make = Manufacturer
    driver = Driver
    passengers = [Driver]


class Garage:
    spaces = Integer('spaces')
    cars = [Car]


class Status:
    success = Boolean('success')
