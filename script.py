from tree import TreeNode
from dfs import search_name
import time


class Script:
    
    def __init__(self):
        database = TreeNode(None)
        print('-'*24)
        print('/add: Add a person to the tree ')
        print('/remove: Remove a person from the tree')
        print('/view: To view the relationship of a person with the company ')
        print('/traverse: To see the entire tree as a whole')
        print('-'*24)
        time.sleep(0.1)
        playing = True
        while playing:
            print('\n')
            prompt = input(':')

            if prompt == "/add":
                first_name = str(input("Type in the first name of the person: "))
                last_name = str(input("Type in the last name of the person: "))

                full_name = first_name + " "  + last_name 
                full_name = TreeNode(full_name)
                print()
                print('Current Tree: ')
                time.sleep(0.1)
                print('-'*24)
                print(database.traverse())
                print('-'*24 + '\n')
                output = True

                if len(database.children) == 0:
                    database.add_child(full_name)
                else:
                    parent = input('What person would you like to add this new person under: ')
                    output = database.add_before(full_name, parent)
                
                if output == True:
                    time.sleep(0.2)
                    print('{name} has been added to the tree '.format(name=full_name.value))
                    time.sleep(0.2)
                    print('-'*24)
                    print("You can type /traverse to see the newly updated tree")
                else:
                    print('-'*24)
                    print(output)
            
            elif prompt == "/traverse":
                time.sleep(0.2)
                print('-'*24)
                print(database.traverse())
                print('-'*24)




script = Script()

print(script)