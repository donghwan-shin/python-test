import unittest
from src.core import *


class TestCore(unittest.TestCase):
    def test_core_1(self):
        template = 'send <*> <*>'
        pattern = generate_pattern_from_template(template)
        m = re.match(pattern, 'send X Y')
        self.assertEqual(('X', 'Y'), m.groups())

    def test_core_2(self):
        template = 'send <*>'
        pattern = generate_pattern_from_template(template)
        m = re.match(pattern, 'send X Y')
        self.assertEqual(('X Y',), m.groups())