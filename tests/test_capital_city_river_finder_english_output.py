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
        expected_output = '{"river":"Vistula","capital":"Warsaw"}'
        actual_output = capital_river_finder("Rzeczpospolita Polska")
        self.assertExpectedJson(actual_output, expected_output)

    def test_france(self):
        expected_output = '{"river":"Seine","capital":"Paris"}'
        actual_output = capital_river_finder("Francja")
        self.assertExpectedJson(actual_output, expected_output)

    def test_germany(self):
        expected_output = '{"river":"Spree","capital":"Berlin"}'
        actual_output = capital_river_finder("Niemcy")
        self.assertExpectedJson(actual_output, expected_output)

    def test_italy(self):
        expected_output = '{"river":"Tiber","capital":"Rome"}'
        actual_output = capital_river_finder("Włochy")
        self.assertExpectedJson(actual_output, expected_output)

    def test_spain(self):
        expected_output = '{"river":"Manzanares","capital":"Madrid"}'
        actual_output = capital_river_finder("Hiszpania")
        self.assertExpectedJson(actual_output, expected_output)

    def test_united_kingdom(self):
        expected_output = '{"river":"Thames","capital":"London"}'
        actual_output = capital_river_finder("Wielka Brytania")
        self.assertExpectedJson(actual_output, expected_output)

    def test_netherlands(self):
        expected_output = '{"river":"Amstel","capital":"Amsterdam"}'
        actual_output = capital_river_finder("Holandia")
        self.assertExpectedJson(actual_output, expected_output)

    def test_belgium(self):
        expected_output = '{"river":"Senne","capital":"Brussels"}'
        actual_output = capital_river_finder("Belgia")
        self.assertExpectedJson(actual_output, expected_output)

    def test_czech_republic(self):
        expected_output = '{"river":"Vltava","capital":"Prague"}'
        actual_output = capital_river_finder("Czechy")
        self.assertExpectedJson(actual_output, expected_output)

    def test_greece(self):
        expected_output = '{"river":"Cephissus","capital":"Athens"}'
        actual_output = capital_river_finder("Grecja")
        self.assertExpectedJson(actual_output, expected_output)

    def test_norway(self):
        expected_output = '{"river":"Akerselva","capital":"Oslo"}'
        actual_output = capital_river_finder("Norwegia")
        self.assertExpectedJson(actual_output, expected_output)

    def test_sweden(self):
        expected_output = '{"river":"Norrström","capital":"Stockholm"}'
        actual_output = capital_river_finder("Szwecja")
        self.assertExpectedJson(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()