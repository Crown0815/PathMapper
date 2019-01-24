class Path:

    def __init__(self, successor = None):
        self.successor = successor


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
        if isinstance(start, Path):
            for sub_path in self.map(start.successor, paths):
                results.append(sub_path)
        else:
            paths.append(start)
            for successor in start.successors:
                path = paths.copy()
                for sub_path in self.map(successor, path):
                    results.append(sub_path)
        if len(results) == 0:
            results.append(paths)
        return results


# Test class

my_tree = SplitPath()
sub_tree0 = SplitPath()
sub_tree1 = SplitPath()
sub_tree2 = SplitPath()
sub_tree3 = SplitPath()
sub_tree4 = SplitPath()
sub_tree5 = SplitPath()

linear0 = Path();
linear1 = Path();
linear2 = Path();
linear3 = Path();

my_tree.add_successor(sub_tree0)
my_tree.add_successor(sub_tree1)

sub_tree0.add_successor(linear0)
linear0.successor = linear3
linear3.successor = sub_tree2
sub_tree0.add_successor(linear1)
linear1.successor = linear2
linear2.successor = sub_tree3
sub_tree1.add_successor(sub_tree2)
sub_tree1.add_successor(sub_tree3)
sub_tree2.add_successor(sub_tree4)
sub_tree2.add_successor(sub_tree5)

mapper = PathMapper();
result = mapper.map(my_tree, list())

for subresults in result:
    print(subresults)


