from tree import TreeNode

def search_name(root_node, goal_value, path):
    path = path + (root_node,)

    if root_node.value == goal_value:
        return path 
    
    for child in root_node.children:
        path_found = dfs(child, goal_value, path)

        if not path_found == None:
            return path_found 
        
    
    return None