from controller.controller import SignalController
from signal.city_signal import CitySignal
from signal.highway_signal import HighWaySignal

from app_logger import logger

logger.info(f'Traffic Simulation Started...')

con = SignalController()

no_vehicle = int(input("Enter number of vehicles: "))
city_signal = CitySignal(no_vehicle)
highway_signal = HighWaySignal(no_vehicle)

con.operate(city_signal)
con.operate(highway_signal)

logger.info(f'Simulation Completed!')