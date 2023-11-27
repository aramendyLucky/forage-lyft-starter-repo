
from engine import Engine
from service_criteria import CapuletEngineServiceCriteria

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        # Implementa la lógica específica para el Capulet Engine
        service_threshold = self.last_service_mileage + 30000
        return self.current_mileage >= service_threshold

class CapuletEngineServiceCriteria(CapuletEngineServiceCriteria):
    def needs_service(self, engine):
        # Implementa la lógica específica para los criterios del Capulet Engine
        return engine.needs_service()
 