# En el archivo car_factory.py
from datetime import date
from car import Car
from engine import Calliope, Glissade, Palindrome, Rorschach, Thovex
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery
from engine_service_criteria import EngineServiceCriteria
from battery_service_criteria import BatteryServiceCriteria
from capulet_engine_service_criteria import CapuletEngineServiceCriteria
from sternman_engine_service_criteria import SternmanEngineServiceCriteria
from willoughby_engine_service_criteria import WilloughbyEngineServiceCriteria
from spindler_battery_service_criteria import SpindlerBatteryServiceCriteria
from nubbin_battery_service_criteria import NubbinBatteryServiceCriteria
 
class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        engine_criteria = CapuletEngineServiceCriteria()
        battery_criteria = SpindlerBatteryServiceCriteria()
        return Calliope(engine, battery, "good", engine_criteria, battery_criteria)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        engine_criteria = WilloughbyEngineServiceCriteria()
        battery_criteria = SpindlerBatteryServiceCriteria()
        return Glissade(engine, battery, "good", engine_criteria, battery_criteria)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        engine_criteria = SternmanEngineServiceCriteria()
        battery_criteria = SpindlerBatteryServiceCriteria()
        return Palindrome(engine, battery, "good", engine_criteria, battery_criteria)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        engine_criteria = WilloughbyEngineServiceCriteria()
        battery_criteria = NubbinBatteryServiceCriteria()
        return Rorschach(engine, battery, "good", engine_criteria, battery_criteria)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        engine_criteria = CapuletEngineServiceCriteria()
        battery_criteria = NubbinBatteryServiceCriteria()
        return Thovex(engine, battery, "good", engine_criteria, battery_criteria)
