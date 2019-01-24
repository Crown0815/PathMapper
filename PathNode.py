class Path:

    def __init__(self, successor):
        self.successor = successor

    def __next__(self):
        return self.successor


class SplitPath:

    def __init__(self):
        self.successors = []

    def add_successor(self, successor):
        self.successors.append(successor)

    def successors(self):
        return self.successors


class PathMapper:

    def map(self, start, paths):
        results = list()
        paths.append(start)
        for successor in start.successors:
            path = paths.copy()
            for subpath in self.map(successor, path):
                results.append(subpath)
        if len(results) == 0:
            results.append(paths)
        return results


my_tree = SplitPath()
sub_tree0 = SplitPath()
sub_tree1 = SplitPath()
sub_tree2 = SplitPath()
sub_tree3 = SplitPath()
sub_tree4 = SplitPath()
sub_tree5 = SplitPath()
my_tree.add_successor(sub_tree0)
my_tree.add_successor(sub_tree1)
sub_tree0.add_successor(sub_tree2)
sub_tree0.add_successor(sub_tree3)
sub_tree1.add_successor(sub_tree2)
sub_tree1.add_successor(sub_tree3)
sub_tree2.add_successor(sub_tree4)
sub_tree2.add_successor(sub_tree5)

mapper = PathMapper();
result = mapper.map(my_tree, list())

for subresults in result:
    print(subresults)


