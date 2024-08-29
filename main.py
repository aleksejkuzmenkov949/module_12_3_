# suite_12_3.py
import unittest

# Исходный класс Runner
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

# Класс тестирования Runner
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для управления заморозкой тестов

    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest('Тесты в этом кейсе заморожены')
            return func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)

# Класс Tournament
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

# Класс тестирования Tournament
class TournamentTest(unittest.TestCase):
    is_frozen = True  # Атрибут для управления заморозкой тестов

    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest('Тесты в этом кейсе заморожены')
            return func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertTrue(True)  # Например, тестовая проверка

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(True)  # Например, тестовая проверка

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertTrue(True)  # Например, тестовая проверка

# Создание тестового набора
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

    # Создаем объект класса TextTestRunner с аргументом verbosity=2
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)