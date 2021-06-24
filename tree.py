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
        self.children = [i for i in self.children if i.value != child_node]
        
    
    def traverse(self):
        nodes = [self]
        num = 0
        while len(nodes) > 0:
            current_node = nodes.pop()
            
            string_1 = ' ' * num 
            string_2 = '|' + str(current_node.value)

            
            nodes += current_node.children
            if len(current_node.children) == 0:
                continue
            else:
                for i in range(len(current_node.children)):
                    string_2 += ' --> ' + str(current_node.children[i].value)
                print(string_1 + string_2)

            num += 1

    def add_before(self, child_node, goal_value):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            #print(current_node.value)
            
            if current_node.value == goal_value:
                current_node.add_child(child_node)
                return True
            else:
                nodes += current_node.children
        
        return "{goal_value} not found in the tree".format(goal_value=goal_value)

    def checker(self, child_node):
        nodes = [self]
        verif = False 

        while len(nodes) > 0:
            current_node = nodes.pop()
            if current_node.value == child_node:
                verif = True 
            else:
                nodes += current_node.children 
        
        return verif 

# Test Inputs 

test1 = TreeNode(1)
test2 = TreeNode(2)
test3 = TreeNode(3)
test4 = TreeNode(4)

test1.add_child(test2)
test2.add_child(test3)
test2.add_child(test4)

print(test1.traverse())
    