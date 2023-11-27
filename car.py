
# En el archivo car.py
from engine import Engine
from battery import Battery
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires_condition):
        self.engine = engine
        self.battery = battery
        self.tires_condition = tires_condition

    def needs_service(self):
        # Llama a needs_service() en cada parte del auto y devuelve True si alguna necesita servicio.
        return (
            self.engine.needs_service() or
            self.battery.needs_service() or
            self.tires_condition == "replace"
        )
