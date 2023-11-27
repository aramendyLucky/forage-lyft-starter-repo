
from abc import ABC, abstractmethod

# Interfaz para los criterios de servicio de los motores
class EngineServiceCriteria(ABC):
    @abstractmethod
    def needs_service(self, engine):
        pass

# Criterios de servicio específicos para el Capulet Engine
class CapuletEngineServiceCriteria(EngineServiceCriteria):
    def needs_service(self, engine):
        # Implementa la lógica específica para los criterios del Capulet Engine
        return engine.needs_service()

# Criterios de servicio específicos para el Willoughby Engine
class WilloughbyEngineServiceCriteria(EngineServiceCriteria):
    def needs_service(self, engine):
        # Implementa la lógica específica para los criterios del Willoughby Engine
        return engine.needs_service()

# Criterios de servicio específicos para el Sternman Engine
class SternmanEngineServiceCriteria(EngineServiceCriteria):
    def needs_service(self, engine):
        # Implementa la lógica específica para los criterios del Sternman Engine
        return engine.needs_service()
