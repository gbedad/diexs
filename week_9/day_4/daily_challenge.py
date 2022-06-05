class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node.value
        return self.left

    def set_right(self, node):
        self.right = node.value
        return self.right

    def set_value(self, value):
        self.value = value
        return self.value

    def get_value(self):
        return self.value

    def add_node(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add_node(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.add_node(value)
        else:
            self.value = value

    def binary_search(self, data):
        if self.value > data:
            if self.left is None:
                return str(data) + " Not Found"
            return self.left.binary_search(data)
        elif self.value < data:
            if self.right is None:
                return str(data) + " Not Found"
            return self.right.binary_search(data)
        else:
            print(str(self.value) + ' is found')



# def add_node(node):
#     if node.value < self.value and not self.left:
#         self.set_left(node)
#     elif node.value > self.value and not self.right:
#         self.set_right(node)
#     else:
#         return print(f"Node {self.value} has already this children nodes left {self.get_left()} and right {self.get_right()}")

    # def search(self, a):
    #     if self.value < a.value:
    #         return search(self.value, a.right)
    #     elif self.value > a.value:

    #         return search(self.value, a.left)
    #     else:
    #         return True


# def add_node(x, node):
#     if node is None:
#         return Node(x, None, None)
#     if x < node.value:
#         return Node(node.value, add_node(x, node.left), node.right)
#     else:
#         return Node(node.value, node.left, add_node(x, node.right))


# def add_node(node, value):
#     if node is None:
#         return Node(value)
#     else:
#         if node.value == value:
#             return node
#         elif node.value < value:
#             node.right = add_node(node.right, value)
#         else:
#             node.left = add_node(node.left, value)
#     return node


# def binary_search(value):
#     current_node = root
#     found = False
#     while current_node:
#         if current_node.value > value:
#             current_node = current_node.left
#         elif current_node.value < value:
#             current_node = current_node.right
#         else:
#             found = True
#             break
#
#     return found


root = Node(value=42)

root.add_node(41)

root.add_node(10)

root.add_node(40)
root.add_node(43)
root.add_node(50)
root.add_node(75)
root.add_node(45)

root.add_node(57)
root.add_node(79)
root.add_node(35)
root.add_node(32)
root.add_node(120)
root.add_node(134)
root.add_node(3)
root.add_node(99)
root.add_node(17)
root.add_node(23)
root.add_node(87)
root.print_tree()

# print(root.left.right.left.left.value)
# print(root.get_left().value)
# root = add_node(root, 10)
# root = add_node(root, 4)
# root = add_node(a, 1)

print(root.binary_search(99))

# ten = Node(10)
# one = Node(1)
# six = Node(6)
# fourteen = Node(14)
# four = Node(4)
# seven = Node(7)
# thirteen = Node(13)
# eight.set_left(three)
# eight.set_right(ten)
# three.set_right(six)
# three.set_left(one)
# six.set_left(four)
# six.set_right(seven)
# ten.set_right(fourteen)
# fourteen.set_left(thirteen)
# eight.add_node(ten)
# print(eight.right)
# eight.add_node(fourteen)
# eight.add_node(three)


# print(eight.left, eight.right)
#
# print(three.get_left())

# root = Node(8)
# n = root.add_node(3)
# print(root.left)

