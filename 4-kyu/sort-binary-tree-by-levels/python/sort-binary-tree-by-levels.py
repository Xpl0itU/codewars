def sort_node(node: Node):
    if node == None:
        return []
    queue = [node]
    final = []
    while len(queue) != 0:
        current_node = queue[0]
        queue.remove(current_node)
        final.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return final

def tree_by_levels(node: Node):
    if node == None:
        return []
    return sort_node(node)