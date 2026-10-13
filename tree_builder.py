class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name    # Employee's name
        self.left = None    # Left direct report (starts empty)
        self.right = None   # Right direct report (starts empty)


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''

    def __init__(self):
        self.root = None    # The team lead (top of the tree)

    def insert(self, manager_name, employee_name, side, current_node=None):
        '''
        Recursively searches for manager_name and adds employee_name
        on the given side ("left" or "right").
        Returns True if the manager was found (even if the insert failed
        because the side was invalid or taken), False if it was not found.
        '''
        # Remember if this is the first (outermost) call
        is_top_level = current_node is None

        # Step 1: if no node was given, start at the root
        if current_node is None:
            current_node = self.root

        # Error: the tree is empty
        if current_node is None:
            print("❌ Error: there is no team lead yet. Add a team lead first.")
            return False

        side = side.lower().strip()

        # Step 2: this node is the manager we are looking for
        if current_node.name == manager_name:
            if side not in ("left", "right"):
                print("❌ Error: side must be 'left' or 'right'.")
                return True   # Manager was found, so stop searching

            # Check that the chosen side is free
            if getattr(current_node, side) is not None:
                print(f"❌ Error: the {side.upper()} side of {manager_name} is already taken.")
                return True   # Manager was found, so stop searching

            # Create the new employee on the open side
            setattr(current_node, side, EmployeeNode(employee_name))
            print(f"✅ {employee_name} added to the {side.upper()} of {manager_name}")
            return True

        # Step 3: not the manager, so search both sides recursively.
        # We only recurse into children that exist (a None child would
        # make the method restart at the root and loop forever).
        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True
        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        # Only print "not found" once, after the whole tree was searched
        if is_top_level:
            print(f"❌ Error: manager '{manager_name}' was not found.")
        return False

    def print_tree(self, node=None, level=0):
        '''
        Recursively prints the team structure with indentation.
        '''
        # Start at the root on the first call
        if node is None and level == 0:
            node = self.root

        # Reached the child of a leaf (or the tree is empty): stop
        if node is None:
            return

        # Indent two spaces per level
        print("  " * level + "- " + node.name)

        # Go one level deeper for each side
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here
test_directory = TeamTree()
test_directory.root = EmployeeNode("Jordan")
test_directory.insert("Jordan", "Taylor", "right")
test_directory.insert("Jordan", "Riley", "left")
test_directory.insert("Riley", "Dana", "right")
test_directory.insert("Riley", "Morgan", "left")
test_directory.insert("Riley", "Extra", "left")    # Error: side already taken
test_directory.insert("Nobody", "Extra", "left")   # Error: manager not found
test_directory.print_tree()
# Expected:
# - Jordan
#   - Riley
#     - Morgan
#     - Dana
#   - Taylor


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print(" Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f" {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    company_directory()


"""
MEMO

In this assignment, I learned how to use a binary tree to organize employees 
in a company. Something I really like about trees is how organized they are and
how they can help solve many different problems in programming. Instead of having
all the information in one long list, a tree helps us see how everything is 
connected. I think that makes it easier to understand.The recursive insertion works 
by starting at the root and looking for the manager where we want to add a new employee.
If the program finds the manager, it checks if the left or right side is empty. 
If there is space, it adds the new employee.If not, it shows an error message. If 
the manager is not found, the program keeps searching through the other branches 
until it finds the person or reaches the end.
One thing I found challenging was understanding how recursion works and how the 
program knows when to stop searching. At first, I was confused about the different
levels and how the program moves between them. After practicing, I understood that
when the program reaches None, there is nothing else to search in that branch. I 
think trees are useful for many things in real life, like organizing employees, 
computer folders, and websites. Overall, I enjoyed learning about trees because they
keep information organized and make complicated problems easier to understand.
"""