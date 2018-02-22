#pylint: skip-file
import unittest

from pylint_badge import generate_from_rate
import os


def load_file():
    """Load file filename and return contents"""
    with open('rating.svg', 'r') as f:
        file_contents = f.read()
    return file_contents


class PylintBadgeGeneratorTest(unittest.TestCase):

    def test_report_generated(self):
        generate_from_rate('9.5')
        self.assertTrue(os.path.exists('rating.svg'))
        self.assertTrue('9.5' in load_file())

    def test_rating_greater_than_9_generates_green_badge(self):
        generate_from_rate('9')
        self.assertTrue('44cc11' in load_file())

    def test_rating_greater_than_7_generates_orange_badge(self):
        generate_from_rate('7')
        self.assertTrue('f89406' in load_file())

    def test_rating_less_than_7_generates_red_badge(self):
        generate_from_rate('6')
        self.assertTrue('b94947' in load_file())

    def test_rating_less_than_0_generates_grey_badge(self):
        generate_from_rate('-1')
        self.assertTrue('9d9d9d' in load_file())

    def test_rating_greater_than_10_generates_grey_badge(self):
        generate_from_rate('11')
        self.assertTrue('9d9d9d' in load_file())

    def tearDown(self):
        os.remove('rating.svg')