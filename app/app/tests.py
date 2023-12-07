from django.test import SimpleTestCase
from app.calc import calculate

class CalcTest(SimpleTestCase):
    def test_add_number(self):
        res = calculate(5, 6)
        self.assertEquals(res,11)