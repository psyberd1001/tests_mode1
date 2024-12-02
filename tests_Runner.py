import logging
import unittest
from tests1 import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen == True, "Frozen test")
    def test_walk(self):
        try:
            runner = Runner.Runner('<NAME>')
            for i in range(10):
                runner.walk()
                runner_distance = runner.distance
            self.assertEqual(runner_distance, 50)
            logging.info('"test_walk" выполнен успешно!')
        except Exception as war:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen == True, "Frozen test")
    def test_run(self):
        try:
            runner1 = Runner.Runner('<NAME1>', True, bool)
            for i in range(10):
                runner1.run()
                runner1_distance = runner1.distance
            self.assertEqual(runner1_distance, 100)
            logging.info('"test_run" выполнен успешно!')
        except Exception as war:
            logging.warning('Неверный тип данныйх для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen == True, "Frozen test")
    def test_challenge(self):
        try:
            runner2 = Runner.Runner('<NAME2>', bool, type)
            runner3 = Runner.Runner('<NAME3>', list, 'dvorf')
            for i in range(10):
                runner2.run()
                runner2_distance = runner2.distance
            for i in range(10):
                runner3.walk()
                runner3_distance = runner3.distance
            self.assertNotEqual(runner2_distance, runner3_distance)
            logging.info('"test_challenge" выполнен успешно!')
        except Exception as war:
            logging.warning('Неверный тип данный для объекта Runner', exc_info=True)


logging.basicConfig(level=logging.INFO, filemode='w', filename='py1.log',
                    format='%(asctime)s | %(levelname)s | %(message)s', encoding='utf-8')
if __name__ == '__main__':
    unittest.main()
