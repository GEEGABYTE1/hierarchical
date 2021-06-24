class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []

    def add_child(self, child_node):
        if not child_node in self.children:
            self.children.append(child_node)
        else:
            print("Someone named \"{}\" is already listed ".format(child_node.value))

    def remove_child(self, child_node):
        if child_node in self.children:
            self.children = [i for i in self.children if not i == child_node]
        else:
            print("\"{}\" is not found! ".format(child_node.value))
    
    def traverse(self):
        nodes = [self]
        num = 0
        while len(nodes) > 0:
            current_node = nodes.pop()
            
            string_1 = ' ' * num 
            string_2 = '|' + str(current_node.value)

            
            nodes += current_node.children
            for i in current_node.children:
                string_2 += ' ' + str(i.value)
            print(string_1 + string_2)

            num += 1

# Test Inputs 

test1 = TreeNode(1)
test2 = TreeNode(2)
test3 = TreeNode(3)
test4 = TreeNode(4)

test1.add_child(test2)
test2.add_child(test3)
test2.add_child(test4)

print(test1.traverse())
    