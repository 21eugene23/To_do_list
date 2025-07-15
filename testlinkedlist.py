from linked_list import LinkedList

def test_linked_list():
    tasks = LinkedList()

    # Add tasks
    tasks.add_task(1, "Morning meeting")
    tasks.add_task(2, "Write report")
    tasks.add_task(3, "Review emails")

    print("Tasks after adding:")
    for tid, name in tasks.get_tasks():
        print(f"ID: {tid}, Name: {name}")

    # Get a task name
    print("\nGet task name with ID 2:")
    print(tasks.get_task_name(2))

    # Delete a task
    deleted_name = tasks.delete_task(2)
    print(f"\nDeleted task with ID 2 (name: {deleted_name})")

    # Show remaining tasks
    print("\nTasks after deletion:")
    for tid, name in tasks.get_tasks():
        print(f"ID: {tid}, Name: {name}")

if __name__ == "__main__":
    test_linked_list()
