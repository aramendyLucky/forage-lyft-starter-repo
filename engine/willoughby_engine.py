
from engine import Engine
from service_criteria import WilloughbyEngineServiceCriteria

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        # Implementa la lógica específica para el Willoughby Engine
        service_threshold = self.last_service_mileage + 60000
        return self.current_mileage >= service_threshold

class WilloughbyEngineServiceCriteria(WilloughbyEngineServiceCriteria):
    def needs_service(self, engine):
        # Implementa la lógica específica para los criterios del Willoughby Engine
        return engine.needs_service()
