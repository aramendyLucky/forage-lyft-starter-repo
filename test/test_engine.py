import unittest
from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        # Crear una instancia de CapuletEngine con un kilometraje que supera el umbral de servicio.
        engine = CapuletEngine(last_service_mileage=50000, current_mileage=80000)
        # Verificar que el método needs_service() devuelva True, ya que el kilometraje actual supera el umbral.
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        # Crear una instancia de CapuletEngine con un kilometraje que no supera el umbral de servicio.
        engine = CapuletEngine(last_service_mileage=50000, current_mileage=70000)
        # Verificar que el método needs_service() devuelva False, ya que el kilometraje actual no supera el umbral.
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        # Crear una instancia de WilloughbyEngine con un kilometraje que supera el umbral de servicio.
        engine = WilloughbyEngine(last_service_mileage=60000, current_mileage=120000)
        # Verificar que el método needs_service() devuelva True, ya que el kilometraje actual supera el umbral.
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        # Crear una instancia de WilloughbyEngine con un kilometraje que no supera el umbral de servicio.
        engine = WilloughbyEngine(last_service_mileage=60000, current_mileage=80000)
        # Verificar que el método needs_service() devuelva False, ya que el kilometraje actual no supera el umbral.
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_warning_light_on(self):
        # Crear una instancia de SternmanEngine con la luz de advertencia encendida.
        engine = SternmanEngine(last_service_date=datetime.now(), warning_light_is_on=True)
        # Verificar que el método needs_service() devuelva True, ya que la luz de advertencia está encendida.
        self.assertTrue(engine.needs_service())

    def test_needs_service_warning_light_off(self):
        # Crear una instancia de SternmanEngine con la luz de advertencia apagada.
        engine = SternmanEngine(last_service_date=datetime.now(), warning_light_is_on=False)
        # Verificar que el método needs_service() devuelva False, ya que la luz de advertencia está apagada.
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
