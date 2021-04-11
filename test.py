import unittest

from AVL import AVL, height


class TestUM(unittest.TestCase):
    def setUp(self):
        self.a = AVL()

    def tearDown(self):
        pass

    def test_empty_tree(self, node=None):
        self.assertTrue(self.a.is_AVLTree(node))  # empty tree is AVL tree

        self.assertEqual(height(node), 0)  # height of empty tree equals 0

        node = self.a.delete(node, 5)  # removing not existing node should work

        self.assertEqual(height(node), 0)

    def test_for_single_node(self, node=None):
        key = 2
        node = self.a.insert(node, key)
        self.assertEqual(height(node), 1)  # height of single node equals 0

        node = self.a.delete(node, 5)
        self.assertEqual(node.key, key)  # removing not existing node
        self.assertTrue(self.a.is_AVLTree(node))  # must be AVL tree

        node = self.a.delete(node, key)
        self.assertEqual(height(node), 0)  # removing existing node
        self.assertEqual(node, None)  # node was deleted

    def test_insert_right(self, node=None):
        insertions_amount = 50
        for i in range(insertions_amount + 1):
            node = self.a.insert(node, i)
            self.assertTrue(self.a.is_AVLTree(node))

    def test_insert_left(self, node=None):
        insertions_amount = 50
        for i in range(insertions_amount - 1, -1, -1):
            node = self.a.insert(node, i)
            self.assertTrue(self.a.is_AVLTree(node))

    def test_insert_left_left(self, node=None):
        # right rotation 20

        node = self.a.insert(node, 20)
        node = self.a.insert(node, 10)
        node = self.a.insert(node, 21)
        node = self.a.insert(node, 5)
        node = self.a.insert(node, 19)
        node = self.a.insert(node, 1)
        node = self.a.insert(node, 7)

        self.assertTrue(self.a.is_AVLTree(node))

        self.assertEqual(height(node), 3)

        self.assertEqual(self.a.get_balance(node), 0)

    def test_insert_left_right(self, node=None):
        # left rotation 10, then right rotation 20

        node = self.a.insert(node, 20)
        node = self.a.insert(node, 10)
        node = self.a.insert(node, 21)
        node = self.a.insert(node, 1)
        node = self.a.insert(node, 5)
        node = self.a.insert(node, 7)
        node = self.a.insert(node, 19)

        self.assertTrue(self.a.is_AVLTree(node))

        self.assertEqual(height(node), 3)

        self.assertEqual(self.a.get_balance(node), 0)

    def test_insert_right_right(self, node=None):
        # left rotation 20

        node = self.a.insert(node, 20)
        node = self.a.insert(node, 5)
        node = self.a.insert(node, 10)
        node = self.a.insert(node, 7)
        node = self.a.insert(node, 5)
        node = self.a.insert(node, 19)
        node = self.a.insert(node, 21)

        self.assertTrue(self.a.is_AVLTree(node))

        self.assertEqual(height(node), 3)

        self.assertEqual(self.a.get_balance(node), 0)

    def test_insert_right_left(self, node=None):
        # right rotation 10, then left rotation 20

        node = self.a.insert(node, 20)
        node = self.a.insert(node, 1)
        node = self.a.insert(node, 10)
        node = self.a.insert(node, 5)
        node = self.a.insert(node, 21)
        node = self.a.insert(node, 7)
        node = self.a.insert(node, 19)

        self.assertTrue(self.a.is_AVLTree(node))

        self.assertEqual(height(node), 3)

        self.assertEqual(self.a.get_balance(node), 0)

    def test_example(self, node=None):
        node = self.a.insert(node, 2)
        node = self.a.insert(node, 5)
        node = self.a.insert(node, 3)

        self.assertTrue(self.a.exists(node, 2))

        self.assertFalse(self.a.exists(node, 4))

        self.assertEqual(self.a.next(4, node).key, 5)

        self.assertEqual(self.a.prev(4, node).key, 3)

        node = self.a.delete(node, 5)
        self.assertEqual(self.a.next(4, node), None)
        self.assertEqual(self.a.prev(4, node).key, 3)


if __name__ == '__main__':
    unittest.main()
