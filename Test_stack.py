# test_stack.py

from undo_Stack import Stack

def test_stack():
    print("Running Stack tests...")

    # Create a new stack
    stack = Stack()

    # Test is_empty on new stack
    assert stack.is_empty() == True, "Stack should be empty initially"

    # Push actions
    stack.push("add Task 1")
    stack.push("delete Task 2")

    assert stack.is_empty() == False, "Stack should not be empty after pushes"

    # Pop and check values
    assert stack.pop() == "delete Task 2", "Should return last pushed action"
    assert stack.pop() == "add Task 1", "Should return previous action"
    assert stack.pop() == None, "Should return None when popping empty stack"

    # Final empty check
    assert stack.is_empty() == True, "Stack should be empty again"

    print("✅ All stack tests passed!")

if __name__ == "__main__":
    test_stack()
