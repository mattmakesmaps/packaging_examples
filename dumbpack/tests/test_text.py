from unittest import TestCase

import dumbpack

class TestText(TestCase):
    def test_is_string(self):
        val = dumbpack.sayHello()
        self.assertTrue(isinstance(val, basestring))
