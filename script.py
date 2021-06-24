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

            elif prompt == "/remove":
                if len(database.children) == 0:
                    print('The tree is empty, there is nothing to look at')
                    time.sleep(0.1)
                    print
                else:
                    name = input('Type the name of the person you want to remove: ')

                    validation = database.checker(name)

                    if validation == False:
                        print('Looks like the name you have entered does not seem to be in the tree ')
                    else:
                        time.sleep(0.1)
                        print('Removing {} from tree'.format(name))
                        for i in range(3):
                            print()
                            print('...')
                            time.sleep(0.2)


                        parent = database.parent_finder(name)

                        print()
                        parent.remove_child(name)
                        time.sleep(0.3)
                        print('{name} has been successfully removed '.format(name=name))
                        time.sleep(0.1)
                        print('You can type /traverse to view your updated tree. ')
                    
            elif prompt == "/view":
                if len(database.children) == 0:
                    print('The tree is empty, there is nothing to look at')
                    time.sleep(0.1)
                    print("Type /add to add your first person to the tree")
                else:

                    name = input("Type the name of the person you would like to view the relationship of: ")

                    validation = database.checker(name)
                    if validation == False:
                        print('{} does not seem to be in the tree'.format(name))
                    else:
                        print("Finding Path ")
                        for i in range(3):
                            print()
                            print('...')
                            time.sleep(0.2)
                        
                        print('Path found: ')
                        print('-'*24)
                        returned_path = search_name(database, name)
                        for i in returned_path:
                            print(i.value)
                        print('-'*24)
            else:
                print('That command does not seem to be valid ')
                time.sleep(0.1)
                

                        





script = Script()

print(script)