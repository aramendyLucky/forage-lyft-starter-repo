# En el archivo battery_service_criteria.py
from service_criteria import ServiceCriteria
from abc import ABC, abstractmethod

class BatteryServiceCriteria(ServiceCriteria):
    @abstractmethod
    def needs_service(self, battery):
        pass
