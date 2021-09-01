import unittest
import Main


class TestTree(unittest.TestCase):
    def test_create(self):
        for _ in range(100):
            self.assertIsNotNone(Main.test_tree())

    def test_number_of_nodes(self):
        for _ in range(100):
            self.assertEqual(Main.test_tree(), 100000)

    def test_delete_nodes(self):
        for _ in range(100):
            self.assertIsNone(Main.test_delete())


if __name__ == '__main__':
    unittest.main()
