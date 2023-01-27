import unittest
from calculator import Calculator

class AdditionTests(unittest.TestCase):
    # "3 + 8 =" 을 입력하고 결과를 확인합니다.
    def test_add_two_numbers(self):
        calculator = Calculator()
        calculator.press_digit(3)
        calculator.press_operator('+')
        calculator.press_digit(8)
        calculator.press_equal()
        self.assertEqual(calculator.current_number, 3 + 8)
    
    # "13 + 24 + 37 =" 을 입력하고 결과를 확인합니다.
    # 위의 코드를 참고해 테스트 코드를 완성하세요.
    def test_add_two_2_digit_numbers(self):
        calculator = Calculator()
        calculator.press_digit(1)
        calculator.press_digit(3)
        calculator.press_operator('+')
        calculator.press_digit(2)
        calculator.press_digit(4)
        calculator.press_operator('+')
        calculator.press_digit(3)
        calculator.press_digit(7)
        calculator.press_equal()
        self.assertEqual(calculator.current_number, 13 + 24 + 37)


class SubtractionTests(unittest.TestCase):
    # "99 - 37 =" 을 입력하고 결과를 확인합니다.
    # 위의 코드를 참고해 테스트 코드를 완성하세요.
    def test_subtract_two_numbers(self):
        calculator = Calculator()
        calculator.press_di
        self.assertEqual(calculator.current_number, 99 - 37)
    
    # "37 - 24 + 17 =" 을 입력하고 결과를 확인합니다.
    # 위의 코드를 참고해 테스트 코드를 완성하세요.
    def test_subtract_three_numbers(self):
        calculator = Calculator()
        pass
        self.assertEqual(calculator.current_number, 37 - 24 + 17)


class ClearTests(unittest.TestCase):
    # "9 C 8 + 7 =" 을 입력하고 결과를 확인합니다. (C는 clear)
    def test_clear_between_numbers(self):
        calculator = Calculator()
        calculator.press_digit(9)
        calculator.press_clear()
        calculator.press_digit(8)
        calculator.press_operator('+')
        calculator.press_digit(7)
        calculator.press_equal()
        self.assertEqual(calculator.current_number, 8 + 7)
    
    # "9 + 8 = C 1 + 1 =" 을 입력하고 결과를 확인합니다. (C는 clear)
    # 위의 코드를 참고해 테스트 코드를 완성하세요.
    def test_clear_between_operations(self):
        calculator = Calculator()
        pass
        self.assertEqual(calculator.current_number, 1 + 1)

unittest.main()
