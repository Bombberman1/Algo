import unittest
from lab5.src.find_road import find_bad_road


class BadRoadTests(unittest.TestCase):
    def test_no_access1(self):
        gas_list = ["Gas1", "Gas2"]
        towns_list = ["Lviv", "Stryi", "Kyiv", "Sambir", "Dolyna", "Volyn", "Chernihiv"]
        available_connections = [
            ["Sambir", "Dolyna"],
            ["Lviv", "Stryi"],
            ["Dolyna", "Gas1"],
            ["Gas1", "Lviv"],
            ["Stryi", "Kyiv"],
            ["Volyn", "Gas1"],
            ["Gas2", "Chernihiv"],
            ["Chernihiv", "Volyn"],
        ]
        expected = [
            ["Gas1", ["Sambir", "Dolyna", "Volyn", "Chernihiv"]],
            ["Gas2", ["Lviv", "Stryi", "Kyiv", "Sambir", "Dolyna"]],
        ]
        actual = find_bad_road(gas_list, towns_list, available_connections)
        self.assertEqual(expected, actual)

    def test_no_access2(self):
        gas_list = ["Gas1", "Gas2"]
        towns_list = [
            "Town1",
            "Town2",
            "Town3",
            "Town4",
            "Town5",
            "Town6",
            "Town7",
            "Town8",
            "Town9",
        ]
        available_connections = [
            ["Gas1", "Town1"],
            ["Town1", "Town2"],
            ["Town3", "Town4"],
            ["Town2", "Town3"],
            ["Town4", "Town5"],
            ["Gas2", "Town6"],
            ["Town7", "Town8"],
            ["Town8", "Town9"],
            ["Town6", "Town7"],
            ["Town9", "Town3"],
        ]
        expected = [
            ["Gas1", ["Town6", "Town7", "Town8", "Town9"]],
            ["Gas2", ["Town1", "Town2"]],
        ]
        actual = find_bad_road(gas_list, towns_list, available_connections)
        self.assertEqual(expected, actual)

    def test_no_access_double_gas(self):
        gas_list = ["Gas1", "Gas2"]
        towns_list = ["Lviv", "Stryi", "Kyiv"]
        available_connections = [
            ["Lviv", "Stryi"],
            ["Gas1", "Lviv"],
            ["Stryi", "Kyiv"],
            ["Gas2", "Gas1"],
        ]
        expected = [["Gas2", ["Lviv", "Stryi", "Kyiv"]]]
        actual = find_bad_road(gas_list, towns_list, available_connections)
        self.assertEqual(expected, actual)

    def test_access_good(self):
        gas_list = ["Gas1"]
        towns_list = ["Lviv", "Stryi", "Kyiv", "Odesa", "Dnipro"]
        available_connections = [
            ["Dnipro", "Odesa"],
            ["Gas1", "Dnipro"],
            ["Lviv", "Stryi"],
            ["Kyiv", "Lviv"],
            ["Odesa", "Kyiv"],
        ]
        expected = []
        actual = find_bad_road(gas_list, towns_list, available_connections)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
