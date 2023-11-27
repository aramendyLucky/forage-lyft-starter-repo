# En el archivo engine_service_criteria.py
from service_criteria import ServiceCriteria
from abc import ABC, abstractmethod

class EngineServiceCriteria(ServiceCriteria):
    @abstractmethod
    def needs_service(self, engine):
        pass
