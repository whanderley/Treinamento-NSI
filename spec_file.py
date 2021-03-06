#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from should_dsl import should
from ex1 import Ball
from ex2 import Square
from ex3 import Rectangle
from ex4 import Person
from ex5 import Television
from ex6 import CurrentAccount
from ex7 import GasolinePump
from ex8 import Rectangle2
from ex9 import Carnivorous
from ex10 import ComplexNumber
from ex11 import RacionalNumber
from ex12 import Number

class TestEx1(unittest.TestCase):

    def setUp(self):
        self.ball = Ball('green')

    def test_color_from_ball_is_green(self):
        self.ball.color |should| equal_to('green')

    def test_change_color_from_ball_for_red(self):
        self.ball.color = 'red'
        self.ball.color |should| equal_to('red')


class TestEx2(unittest.TestCase):

    def setUp(self):
        self.square = Square(20)

    def test_if_side_from_square_is_20(self):
        self.square.side |should| equal_to(20)

    def test_change_the_side_value_from_square(self):
        self.square.side = 5
        self.square.side |should| equal_to(5)

    def test_get_area_of_one_square_with_side_equal_to_4(self):
        self.square.side = 4
        self.square.area |should| equal_to(16)


class TestEx3(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(2, 4)

    def test_base_and_height_are_2_and_4(self):
        self.rectangle.base |should| equal_to(2)
        self.rectangle.height |should| equal_to(4)

    def test_change_base_and_height(self):
        self.rectangle.base = 3
        self.rectangle.height = 6
        self.rectangle.base |should| equal_to(3)
        self.rectangle.height |should| equal_to(6)

    def test_get_area(self):
        self.rectangle.base = 4
        self.rectangle.height = 4
        self.rectangle.area |should| equal_to(16)

    def test_get_perimeter(self):
        self.rectangle.base = 3
        self.rectangle.height = 6
        self.rectangle.perimeter |should| equal_to(18)


class TestEx4(unittest.TestCase):

    def setUp(self):
        self.person = Person(12, 53, 160)

    def test_age_weight_and_height(self):
        self.person.age |should| equal_to(12)
        self.person.weight |should| equal_to(53)
        self.person.height |should| equal_to(160)

    def test_get_old(self):
        self.person.age = 10
        self.person.get_old() 
        self.person.age |should| equal_to(11)
        self.person.height |should| equal_to(161.5)
        self.person.age = 21
        self.person.height = 170
        self.person.get_old() 
        self.person.age |should| equal_to(22)
        self.person.height |should| equal_to(170)

    def test_fatten(self):
        self.person.weight = 30
        self.person.fatten(5) 
        self.person.weight |should| equal_to(35)

    def test_weight_loss(self):
        self.person.weight = 30
        self.person.weight_loss(4) 
        self.person.weight |should| equal_to(26)

class TestEx5(unittest.TestCase):

    def setUp(self):
        self.television = Television(30, 25)

    def test_press_power_button(self):
        self.television.status = 'on'
        self.television.press_power_button() |should| equal_to('off')

    def test_set_up_channel_from_23_should_return_24(self):
        self.television.status = 'on'
        self.television.channel = 23
        self.television.set_up_channel() 
        self.television.channel |should| equal_to(24)
        self.television.status = 'off'
        self.television.set_up_channel() 
        self.television.channel |should| equal_to(24)
 
    def test_set_up_channel_from_30_should_return_30(self):
        self.television.channel = 30
        self.television.status = 'on'
        self.television.set_up_channel() 
        self.television.channel |should| equal_to(30)

    def test_set_down_channel_from_30_should_return_29(self):
        self.television.status = 'on'
        self.television.channel = 30
        self.television.set_down_channel() 
        self.television.channel |should| equal_to(29)
        self.television.status = 'off'
        self.television.set_down_channel()
        self.television.channel |should| equal_to(29)

    def test_set_down_channel_from_1_should_return_1(self):
        self.television.status = 'on'
        self.television.channel = 1
        self.television.set_down_channel() 
        self.television.channel |should| equal_to(1)

    def test_set_up_volume_from_14_should_return_15(self):
        self.television.status = 'on'
        self.television.volume = 14
        self.television.set_up_volume() 
        self.television.volume |should| equal_to(15)
        self.television.status = 'off'
        self.television.set_up_volume() 
        self.television.volume |should| equal_to(15)

    def test_set_up_volume_from_25_should_return_25(self):
        self.television.status = 'on'
        self.television.volume = 25
        self.television.set_up_volume()
        self.television.volume |should| equal_to(25)

    def test_set_down_volume_from_12_should_return_11(self):
        self.television.status = 'on'
        self.television.volume = 12
        self.television.set_down_volume() 
        self.television.volume |should| equal_to(11)
        self.television.status = 'off'
        self.television.set_down_volume() 
        self.television.volume |should| equal_to(11)

    def test_set_down_volume_from_0_should_return_0(self):
        self.television.status = 'off' 
        self.television.volume = 0
        self.television.set_down_volume() 
        self.television.volume |should| equal_to(0)


class TestEx6(unittest.TestCase):

    def setUp(self):
        self.current_account = CurrentAccount("jumento juvenal", "123.345-9")

    def test_consult_leftover(self):
        self.current_account.leftover = 23
        self.current_account.leftover |should| equal_to(23)

    def test_deposit_20_in_account_with_10_should_return_30(self):
        self.current_account.leftover = 10
        self.current_account.deposit(20) |should| equal_to(30)

    def test_retire_10_in_account_with_50_should_return_40(self):
        self.current_account.leftover = 50
        self.current_account.retire(10) |should| equal_to(40)

    def test_retire_20_in_account_with_10_should_return_not_enough_money(self):
        self.current_account.leftover = 10
        self.current_account.retire(20) |should| equal_to("not enough money")
        self.current_account.leftover |should| equal_to(10)


class TestEx7(unittest.TestCase):

    def setUp(self):
        self.gasoline_pump = GasolinePump(400, 3.00)

    def test_get_pump_volume(self):
        self.gasoline_pump.volume |should| equal_to(400)

    def test_fill_pump(self):
        self.gasoline_pump.fill() |should| equal_to(400)

    def test_supply_60_by_value_should_return_20(self):
        self.gasoline_pump.supply_by_value(60) |should| equal_to(20)

    def test_supply_by_value_in_pump_with_insufficient_volume(self):
        self.gasoline_pump.volume = 20
        self.gasoline_pump.supply_by_value(90) |should| \
          equal_to('volume unavailable')
        self.gasoline_pump.volume |should| equal_to(20)

    def test_supply_by_number_of_liters_20_should_return_60(self):
        self.gasoline_pump.supply_by_number_of_liters(20) |should| equal_to(60)

    def test_supply_by_number_of_liters_with_insufficient_volume(self):
        self.gasoline_pump.volume = 20
        self.gasoline_pump.supply_by_number_of_liters(30) |should| \
        equal_to('volume unavailable')
        self.gasoline_pump.volume |should| equal_to(20)


class TestEx8(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle2(100, 40)

    def test_query_coordinate_from_center(self):
        self.rectangle.center |should| equal_to([50, 20])

    def test_change_center(self):
        self.rectangle.redefine_center(200, 40) |should| equal_to([200, 40])
        self.rectangle.vertice1.x |should| equal_to(150)
        self.rectangle.vertice2.x |should| equal_to(150)

    def test_get_area_from_rectangle(self):
        self.rectangle.area |should| equal_to(4000)

    def test_get_perimeter_from_rectangle(self):
        self.rectangle.perimeter |should| equal_to(280)

    def test_is_square(self):
        self.rectangle.base = 100
        self.rectangle.height = 100
        self.rectangle.is_square() |should| equal_to(True)
        self.rectangle.base = 20
        self.rectangle.height = 10
        self.rectangle.is_square() |should| equal_to(False)


class TestEx9(unittest.TestCase):

    def setUp(self):
        self.carnivorous = Carnivorous()

    def test_eat_anything(self):
        rectangle = Rectangle(20, 10)
        self.carnivorous.eat(1) |should| equal_to([1])
        self.carnivorous.eat('a') |should| equal_to([1, 'a'])
        self.carnivorous.eat(rectangle) |should| equal_to([1, 'a', rectangle])

    def test_digest(self):
        rectangle = Rectangle(20, 10)
        self.carnivorous.eat(1) |should| equal_to([1])
        self.carnivorous.eat('a') |should| equal_to([1, 'a'])
        self.carnivorous.eat(rectangle) |should| equal_to([1, 'a', rectangle])
        self.carnivorous.digest() |should| equal_to(1)
        self.carnivorous.digest() |should| equal_to('a')
        self.carnivorous.stomach |should| equal_to([rectangle])


class TestEx10(unittest.TestCase):

    def setUp(self):
        self.complex_number1 = ComplexNumber(2, 3)
        self.complex_number2 = ComplexNumber(4, -6)

    def test_addition(self):
        self.complex_number1 + self.complex_number2 |should| \
         equal_to(ComplexNumber(6, -3))

    def test_subtraction(self):
        self.complex_number1 - self.complex_number2 |should| \
         equal_to(ComplexNumber(-2, 9))

    def test_multiplication(self):
        self.complex_number1 * self.complex_number2 |should| \
         equal_to(ComplexNumber(26, 0))

    def test_parse_to_string(self):
        self.complex_number1.parse_to_string() |should| equal_to('2 + 3i')

class TestEx11(unittest.TestCase):

    def setUp(self):
        self.racional_number1 = RacionalNumber(3, 4)
        self.racional_number2 = RacionalNumber(4, 2)

    def test_consult_denominator_and_numerator_from_racional_number1(self):
        self.racional_number1.numerator |should| equal_to(3)
        self.racional_number1.denominator |should| equal_to(4)

    def test_consult_denominator_and_numerator_from_racional_number2(self):
        self.racional_number2.numerator |should| equal_to(2)
        self.racional_number2.denominator |should| equal_to(1)

    def test_addition(self):
        self.racional_number1 + self.racional_number2 |should| \
         equal_to(RacionalNumber(11, 4))

    def test_subtraction(self):
        self.racional_number1 - self.racional_number2 |should| \
         equal_to(RacionalNumber(-5, 4))

    def test_multiplication(self):
        self.racional_number1 * self.racional_number2 |should| \
         equal_to(RacionalNumber(3, 2))

    def test_division(self):
        self.racional_number1 / self.racional_number2 |should| \
         equal_to(RacionalNumber(6, 16))

    def test_parse_to_string(self):
        self.racional_number1.string |should| equal_to('3/4')

    def test_parse_to_float_string(self):
        self.racional_number1.float_string(3) |should| equal_to('0.75')


class TestEx12(unittest.TestCase):

        def setUp(self):
            self.number = Number(5)

        def test_get_number_value(self):
            self.number.value |should| equal_to(5)

        def test_is_pair_should_return_false(self):
            self.number.is_pair |should| equal_to(False)

        def test_is_odd_should_return_true(self):
            self.number.is_odd |should| equal_to(True)

        def test_romam(self):
            self.number.romam |should| equal_to('V')
            self.number.value = 35
            self.number.romam |should| equal_to('XXXV')

        def test_fibonacci(self):
            self.number.fibonacci |should| equal_to(5)
            self.number.value = 4
            self.number.fibonacci |should| equal_to('nao pertence')

        def test_loop_fatorial(self):
            self.number.loop_fatorial |should| equal_to(120)
            self.number.value = 4
            self.number.loop_fatorial |should| equal_to(24)

        def test_recursive_fatorial(self):
            self.number.recursive_fatorial |should| equal_to(120)
          #  self.number.value = 4
           # self.number.recursive_fatorial |should| equal_to(24)

        def test_functional_fatorial(self):
            self.number.functional_fatorial |should| equal_to(120)
            self.number.value = 0
            self.number.functional_fatorial |should| equal_to(1)
            self.number.value = 1
            self.number.functional_fatorial |should| equal_to(1)
