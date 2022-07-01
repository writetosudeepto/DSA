class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, tree_node):
        self.children.append(tree_node)
    
        
tree = TreeNode("Drinks",[])
cold = TreeNode("Cold",[])
tree.add_child(cold)
hot = TreeNode("Hot",[])
tree.add_child(hot)
tea = TreeNode("Tea",[])
hot.add_child(tea)
coffee = TreeNode("Coffee",[])
hot.add_child(coffee)
coke = TreeNode("Coke",[])
cold.add_child(coke)
beer = TreeNode("Beer",[])
cold.add_child(beer)


print(tree)