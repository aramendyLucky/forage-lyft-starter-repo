# En el archivo spindler_battery.py
from datetime import date, timedelta

class SpindlerBattery:
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date

    def needs_service(self):
        # Modificar para requerir servicio después de tres años
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date <= date.today()

# Tests para SpindlerBattery
# Se deben escribir pruebas que cubran los casos de requerir y no requerir servicio después de tres años.
 