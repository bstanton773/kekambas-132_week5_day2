from whiteboard import solution
from unittest import TestCase, main


class TestWhiteboard(TestCase):
    def test_hello_world(self):
        self.assertEqual(solution("helloWorld"), "hello World")
    def test_uncamel(self):
        self.assertEqual(solution("uncamelThisCamel"), "uncamel This Camel")
    def test_camel(self):
        self.assertEqual(solution("camelCasing"), "camel Casing")
    def test_another_camel(self):
        self.assertEqual(solution("thisIsAnotherCamelCasing"), "this Is Another Camel Casing")
    def test_pangram(self):
        self.assertEqual(solution("theQuickBrownFoxJumpsOverTheLazyDog"), "the Quick Brown Fox Jumps Over The Lazy Dog")

if __name__ == "__main__":
    main()