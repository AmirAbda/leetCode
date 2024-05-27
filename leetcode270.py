class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def closest_Binary_Search(root, target):
        stack = [root]
        closest_value = root.val  # Initialize closest_value
        diff_min = abs(root.val - target)

        while stack:
            node = stack.pop()
            difference = abs(node.val - target)
            if difference < diff_min:
                closest_value = node.val  
                diff_min = difference

            if node.val > target:
                if node.left:
                    stack.append(node.left)
            else:
                if node.right:
                    stack.append(node.right)

        return closest_value  
# Example Usage
solution = TreeNode
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
target = 3.714286
print(solution.closest_Binary_Search(root, target))  