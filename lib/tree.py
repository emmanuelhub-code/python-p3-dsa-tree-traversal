class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, element_id):
        """
        Depth-first search to find the node with the given id.
        Returns the node dict if found, else None.
        """
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)  # take the first node
            if node.get('id') == element_id:
                return node
            # Add children to the beginning for depth-first
            nodes_to_visit = node.get('children', []) + nodes_to_visit

        return None
