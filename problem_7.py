
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, path_list, handler):
        current_node = self.root
        for path_part in path_list:
            current_node = current_node.insert(path_part)

        current_node.handler = handler

    def find(self, path_list):
        current_node = self.root

        for path_part in path_list:
            current_node = current_node.insert(path_part)

        return current_node


class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}

    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()
        return self.children[path_part]


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.trie = RouteTrie()
        root = self.trie.root
        root.handler = root_handler
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        if path is None:
            return

        path_list = self.split_path(path)
        self.trie.insert(path_list, handler)

    def lookup(self, path):
        if path is None or path.strip() == "":
            return self.not_found_handler

        path_list = self.split_path(path)
        node = self.trie.find(path_list)
        if node is not None and node.handler is not None:
            return node.handler
        else:
            return self.not_found_handler

    def split_path(self, path):
        path_parts = path.split("/")
        # filter out extra spaces
        path_parts = map(lambda x: x.strip(), path_parts)
        path_parts = filter(lambda x: x != "" ,path_parts)
        return list(path_parts)


root_handler = "root handler"
not_found_handler = "not found"

router = Router(root_handler, not_found_handler)
router.add_handler("/home/about", "about handler")

index_handler = router.lookup("/")
# expect root handler
print(index_handler)


not_home_handler = router.lookup("/home")
# expect not found
print(not_home_handler)

about_handler = router.lookup("/home/about")
# expect about handler
print(about_handler)


about_handler_with_slash = router.lookup("/home/about/")
# expect about handler
print(about_handler)

none_handler = router.lookup(None)
# expect not found
print(none_handler)

me_handler = router.lookup("/home/about/me")
# expect not found
print(me_handler)

extra_slashes_handler = router.lookup("/home/about//")
# expect about handler
print(extra_slashes_handler)

spaces_in_path_handler = router.lookup("/home/about/ /")
# expect about handler
print(spaces_in_path_handler)



