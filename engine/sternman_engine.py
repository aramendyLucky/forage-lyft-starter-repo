
from engine import Engine
from service_criteria import SternmanEngineServiceCriteria

class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        # Implementa la lógica específica para el Sternman Engine
        return self.warning_light_is_on

class SternmanEngineServiceCriteria(SternmanEngineServiceCriteria):
    def needs_service(self, engine):
        # Implementa la lógica específica para los criterios del Sternman Engine
        return engine.needs_service()
 