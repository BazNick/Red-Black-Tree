class Node:
    __slots__ = '_value', '_left_tree', '_right_tree', '_black', '_parent_tree', '_is_left_child'

    def __init__(self, value, black=False, left_tree=None, right_tree=None,
                 parent_tree=None, is_left_child=False):
        self._value = value
        self._black = black
        self._left_tree = left_tree
        self._right_tree = right_tree
        self._parent_tree = parent_tree
        self._is_left_child = is_left_child

    def __repr__(self):
        return f'Node with _value = {self._value}, _left_tree = {self._left_tree}, ' \
               f'_right_tree = {self._right_tree}, _color = {self._black}'

    @property
    def node_left_tree(self):
        return self._left_tree

    @node_left_tree.setter
    def node_left_tree(self, new_ptr):
        self._left_tree = new_ptr

    @property
    def node_right_tree(self):
        return self._right_tree

    @node_right_tree.setter
    def node_right_tree(self, new_ptr):
        self._right_tree = new_ptr

    @property
    def node_black_color(self):
        return self._black

    @node_black_color.setter
    def node_black_color(self, new_color):
        self._black = new_color

    @property
    def node_value(self):
        return self._value

    @node_value.setter
    def node_value(self, new_value):
        self._value = new_value

    @property
    def node_parent(self):
        return self._parent_tree

    @node_parent.setter
    def node_parent(self, new_val):
        self._parent_tree = new_val

    @property
    def is_left_child(self):
        return self._is_left_child

    @is_left_child.setter
    def is_left_child(self, new_value):
        self._is_left_child = new_value
