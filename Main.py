import random
from RedBlackTree import *


def test_tree():
    testing_array = []
    for i in range(100000):
        testing_array.append(random.randint(-100000000, 100000000))

    x = RedBlackTree()
    # print('\n')
    # print(f'Inserting root {testing_array[0]}')
    x.root = x.create_tree(x.root, testing_array[0])
    for j in range(1, len(testing_array)):
        x.create_tree(x.root, testing_array[j])

    return x.size


def test_delete():
    testing_delete_array = []
    for i in range(100000):
        testing_delete_array.append(random.randint(-100000000, 100000000))

    x = RedBlackTree()
    # print('\n')
    # print(f'Inserting root {testing_array[0]}')
    x.root = x.create_tree(x.root, testing_delete_array[0])
    for j in range(1, len(testing_delete_array)):
        x.create_tree(x.root, testing_delete_array[j])

    for k in range(len(testing_delete_array)):
        x.remove_element(x.root, testing_delete_array[k])
