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
            string_2 = '|'
            print(string_1 + string2)
            nodes += current_node.children
            num += 1

    