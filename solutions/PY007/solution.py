# PY007 — Inside and Outside: Understanding Scope
# Reference solution: Study Session Tracker

completed_sessions = 0
study_goal = "Understand Python scope"


def show_completed_sessions():
    """Display the global session count without changing it."""
    # Reading a global name is allowed when this function does not assign to it.
    print(f"Completed sessions: {completed_sessions}")


def demonstrate_local_scope():
    """Create and display a local variable inside this function."""
    local_note = "This note exists only inside demonstrate_local_scope()."
    print(local_note)

    # Experiment: uncomment the next line to see a NameError.
    # print(local_note)
    # The function's local variable is not available directly in the module scope.


def demonstrate_same_name():
    """Show that a local name can shadow a global name without replacing it."""
    study_goal = "Practise local variables"  # This assignment creates a local name.
    print(f"Inside function: {study_goal}")


def increment_completed_sessions():
    """Increase the global session counter by one."""
    global completed_sessions
    # 'global' tells Python that assignment targets the module-level variable.
    completed_sessions += 1


def updated_count(count, amount):
    """Return an updated count without changing the global counter."""
    return count + amount


def main():
    """Run the scope experiments in a clear, repeatable order."""
    global study_goal

    print("1. Read a global variable")
    show_completed_sessions()

    print("\n2. Create a local variable")
    demonstrate_local_scope()

    print("\n3. Use the same name in local and global scope")
    print(f"Before function call: {study_goal}")
    demonstrate_same_name()
    print(f"After function call:  {study_goal}")
    # The global value stays the same because the function assigned a local name.

    print("\n4. Modify global state")
    increment_completed_sessions()
    show_completed_sessions()
    increment_completed_sessions()
    show_completed_sessions()

    # Experiment: remove/comment out 'global completed_sessions' in the function.
    # The augmented assignment then treats the name as local, and Python raises
    # UnboundLocalError because it tries to read that local name before assigning it.

    print("\n5. Compare with parameters and return values")
    trial_count = 10
    new_count = updated_count(trial_count, 3)
    print(f"Original trial count: {trial_count}")
    print(f"Returned updated count: {new_count}")
    print(f"Global session count remains: {completed_sessions}")
    # Returning a result makes the dependency explicit and avoids hidden global changes.


if __name__ == "__main__":
    main()
