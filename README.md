# Hierarchical 🌴⬆️

Hierarchical is an application that will automate analyzing and creating hierarchical trees for companies. 

Just like any typical hierarchical tree, users will be able to use this software to portray different people with different jobs and roles of a company really easily. With only one command, users can either view, add, remove, and even find a specific relationship of the person with the company, making it very time efficient and accessbile ⏳👋🏼

# Commands 🔮
    - `/add`: Adds a person to the tree
    - `/remove`: Removes a pereson from the tree
    - `/view`: Views the relationship of a specific person prompted with the company 
    - `/traverse`: Views the enitre tree as a whole 

     Some commands may prompt users to type names. 

    `first_name = str(input("Type in the first name of the person: "))
     last_name = str(input("Type in the last name of the person: "))`

    *For the `/add` command, users have to type the person's first name and the last name separately when prompted. 

    Otherwise, for other commands, writing the full name is necessary.
    `name = input('Type the name of the person you want to remove: ')`

    Then again, if the program does not take in a name, try typing the first name and last name together. For the current version, the name must be typed *exactly* the same as the way it is listed in the tree.

     


# More Information 🔬

Each Function takes `O(N)` time complexity and most helper functions (`.traverse()`, `.parent_finder()`, `.()checker`, `.add_before()`, and `.traverse()`) have `O(N)` space complexity. The rest of the functions have `O(1)` space complexity.

The `/view` command replicates the *Depth-First Search Algorithm*. This search algorithm is a recursive algorithm that will return the path right to the goal node. This algorithm takes `O(N)` complexity as well as we are searching each node `N`. 

To run the program as a whole, run `script.py`. The rest of the files are for the "backend". 

Made in Python 🐍
