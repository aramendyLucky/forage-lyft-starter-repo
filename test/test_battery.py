import unittest
from datetime import date, timedelta
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        # Crear una instancia de SpindlerBattery con una fecha de servicio que supera el umbral.
        battery = SpindlerBattery(last_service_date=date.today() - timedelta(days=800))
        # Verificar que el método needs_service() devuelva True, ya que la fecha de servicio ha superado el umbral.
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        # Crear una instancia de SpindlerBattery con una fecha de servicio que no supera el umbral.
        battery = SpindlerBattery(last_service_date=date.today() - timedelta(days=400))
        # Verificar que el método needs_service() devuelva False, ya que la fecha de servicio no ha superado el umbral.
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        # Crear una instancia de NubbinBattery con una fecha de servicio que supera el umbral.
        battery = NubbinBattery(last_service_date=date.today() - timedelta(days=1800))
        # Verificar que el método needs_service() devuelva True, ya que la fecha de servicio ha superado el umbral.
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        # Crear una instancia de NubbinBattery con una fecha de servicio que no supera el umbral.
        battery = NubbinBattery(last_service_date=date.today() - timedelta(days=1200))
        # Verificar que el método needs_service() devuelva False, ya que la fecha de servicio no ha superado el umbral.
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
