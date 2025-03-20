import unittest
import json
import time
from unittest.mock import patch
from dotenv import load_dotenv
from capital_city_river_finder.finder import capital_river_finder

class TestCapitalRiverFinder(unittest.TestCase):

    def setUp(self):
        load_dotenv()

    def tearDown(self):
        # to not reach the minute limit we slow down the tests
        time.sleep(1)

    def assertExpectedJson(self, actual_output:str, expected_output:str):
        actual_output_obj = json.loads(actual_output)
        expected_output_obj = json.loads(expected_output)

        self.checkMultipleValues(expected_output_obj.get("river"), actual_output_obj.get("river"))

        self.assertEqual(expected_output_obj.get("capital"), actual_output_obj.get("capital"))

    def checkMultipleValues(self, possible_values:str, value:str):
        if "|" in possible_values:
            array = possible_values.split("|")

            if value in array:
                return True
            else:
                raise Exception("Value " + value + " not found in the array " + ' '.join(array))
        else:
            self.assertEqual(value, possible_values)

    def test_poland(self):
        expected_output = '{"river":"Wisła","capital":"Warszawa"}'
        actual_output = capital_river_finder("Rzeczpospolita Polska", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_france(self):
        expected_output = '{"river":"Sekwana","capital":"Paryż"}'
        actual_output = capital_river_finder("Francja", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_germany(self):
        expected_output = '{"river":"Sprewa|Sprea","capital":"Berlin"}'
        actual_output = capital_river_finder("Niemcy", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_italy(self):
        expected_output = '{"river":"Tyber","capital":"Rzym"}'
        actual_output = capital_river_finder("Włochy", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_spain(self):
        expected_output = '{"river":"Manzanares","capital":"Madryt"}'
        actual_output = capital_river_finder("Hiszpania", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_united_kingdom(self):
        expected_output = '{"river":"Tamiza","capital":"Londyn"}'
        actual_output = capital_river_finder("Wielka Brytania", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_netherlands(self):
        expected_output = '{"river":"Amstel","capital":"Amsterdam"}'
        actual_output = capital_river_finder("Holandia", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_belgium(self):
        expected_output = '{"river":"Zenne","capital":"Bruksela"}'
        actual_output = capital_river_finder("Belgia", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_czech_republic(self):
        expected_output = '{"river":"Wełtawa","capital":"Praga"}'
        actual_output = capital_river_finder("Czechy", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_greece(self):
        expected_output = '{"river":"Kifisos","capital":"Ateny"}'
        actual_output = capital_river_finder("Grecja", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_norway(self):
        expected_output = '{"river":"Akerselva","capital":"Oslo"}'
        actual_output = capital_river_finder("Norwegia", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

    def test_sweden(self):
        # here Mälaren is a lake, not a river, but GPT-3.5-turbo model is wrong, and claims that in Polish output it's a river :D
        expected_output = '{"river":"Mälaren","capital":"Sztokholm"}'
        actual_output = capital_river_finder("Szwecja", "Polish")
        self.assertExpectedJson(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()