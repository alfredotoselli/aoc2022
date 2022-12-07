# Build a tree DS from the input file
# Node is a directory. Data is a list of files. Children a list of directories

# ** Wrong result **


class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.file_values = []
        self.children_dirs = []
        self.parent = None

    def add_file_value(self, value):
        self.file_values.append(value)

    def add_child_dir(self, dir):
        # self.dir = dir
        self.children_dirs.append(dir)
        dir.parent = self

    def get_depth(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def traverse(self, dir_values_100000):
        print("  " * self.get_depth() + "|-- ", end="")
        print(self.name, "-->", end="")
        print(self.file_values)

        if sum(self.file_values) <= 100000:
            dir_values_100000.append(sum(self.file_values))

        if self.children_dirs:
            for dir in self.children_dirs:
                dir.traverse(dir_values_100000)

    def set_root(self):
        if self.parent is None:
            print(self.name)
            return self
        self = self.parent
        return self.set_root()


def run():

    with open("7_input.txt") as file:
        commands = [line.strip() for line in file.readlines()]

    root = DirectoryNode(commands[0].split()[2])
    current_dir = root
    for cmd_line in commands[1:]:
        cmd_list = cmd_line.split()

        if cmd_list[0] == "$" and cmd_list[1] == "cd":
            if cmd_list[2] == "..":
                current_dir = current_dir.parent
            else:
                if cmd_list[2] not in current_dir.children_dirs:
                    current_dir.add_child_dir(DirectoryNode(cmd_list[2]))
                for child_dir in current_dir.children_dirs:
                    if child_dir.name == cmd_list[2]:
                        current_dir = child_dir
                        break

        elif cmd_list[0] == "dir":
            current_dir.add_child_dir(DirectoryNode(cmd_list[1]))

        elif cmd_list[0].isdigit():
            current_dir.add_file_value(int(cmd_list[0]))

    dir_values_100000 = []
    root.traverse(dir_values_100000)
    print(sum(dir_values_100000))


if __name__ == "__main__":
    run()
