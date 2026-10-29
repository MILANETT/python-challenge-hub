"""PY009 — The Equipment Desk: reference implementation.

Run with Python 3.10 or newer. Uses only built-in Python features.
The inventory's available quantity is derived from the requests currently
marked Issued, keeping the stock report consistent with request statuses.
"""


INVENTORY = {
    "Projector": 4,
    "Laptop": 6,
    "Speaker": 3,
    "Microphone": 8,
    "Extension cable": 10,
}

# The starting records supplied in the challenge.
requests = {
    "EQ001": {
        "requester": "Computing Club",
        "equipment": "Projector",
        "quantity": 2,
        "status": "Issued",
    },
    "EQ002": {
        "requester": "Debate Society",
        "equipment": "Microphone",
        "quantity": 3,
        "status": "Requested",
    },
    "EQ003": {
        "requester": "Media Team",
        "equipment": "Laptop",
        "quantity": 2,
        "status": "Issued",
    },
}


def find_equipment_name(user_text):
    """Return the inventory's canonical equipment name, or None if unknown."""
    cleaned_text = user_text.strip().casefold()

    for equipment_name in INVENTORY:
        if equipment_name.casefold() == cleaned_text:
            return equipment_name

    return None


def issued_quantity_for(equipment_name):
    """Return the total quantity of this equipment in outstanding issues."""
    quantity_issued = 0

    for request in requests.values():
        if (
            request["equipment"] == equipment_name
            and request["status"] == "Issued"
        ):
            quantity_issued += request["quantity"]

    return quantity_issued


def available_quantity_for(equipment_name):
    """Return total stock minus equipment currently issued."""
    return INVENTORY[equipment_name] - issued_quantity_for(equipment_name)


def register_request():
    """Collect, validate, and store one new request."""
    request_id = input("Request ID: ").strip().upper()

    if request_id == "":
        print("Request ID cannot be blank.")
        return

    if request_id in requests:
        print("That request ID already exists.")
        return

    requester = input("Requester name: ").strip()
    if requester == "":
        print("Requester name cannot be blank.")
        return

    print("Equipment options:")
    for equipment_name in INVENTORY:
        print(f"- {equipment_name}")

    equipment_name = find_equipment_name(input("Equipment type: "))
    if equipment_name is None:
        print("Unknown equipment type. Choose an item from the list.")
        return

    quantity_text = input("Quantity: ").strip()
    # Validate before converting; this challenge does not require try/except.
    if not quantity_text.isdigit():
        print("Quantity must be a positive whole number.")
        return

    quantity = int(quantity_text)
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    requests[request_id] = {
        "requester": requester,
        "equipment": equipment_name,
        "quantity": quantity,
        "status": "Requested",
    }
    print(f"Request {request_id} registered successfully.")


def issue_equipment():
    """Issue a requested item only when enough stock is available."""
    request_id = input("Request ID to issue: ").strip().upper()

    if request_id not in requests:
        print("Request not found.")
        return

    request = requests[request_id]
    if request["status"] != "Requested":
        print("Only requests with status Requested can be issued.")
        return

    equipment_name = request["equipment"]
    quantity_available = available_quantity_for(equipment_name)

    if request["quantity"] > quantity_available:
        print(
            f"Not enough {equipment_name} available. "
            f"Available quantity: {quantity_available}."
        )
        return

    request["status"] = "Issued"
    print(f"Request {request_id} issued successfully.")


def return_equipment():
    """Return equipment from a valid outstanding issue exactly once."""
    request_id = input("Request ID to return: ").strip().upper()

    if request_id not in requests:
        print("Request not found.")
        return

    request = requests[request_id]
    if request["status"] != "Issued":
        print("Only an issued request can be returned, and it can be returned once.")
        return

    # Marking it Returned means it is no longer counted as outstanding stock.
    request["status"] = "Returned"
    print(f"Equipment for request {request_id} returned successfully.")


def cancel_request():
    """Cancel a request only while it has not been issued."""
    request_id = input("Request ID to cancel: ").strip().upper()

    if request_id not in requests:
        print("Request not found.")
        return

    request = requests[request_id]
    if request["status"] != "Requested":
        print("Only a request that has not been issued can be cancelled.")
        return

    request["status"] = "Cancelled"
    print(f"Request {request_id} cancelled successfully.")


def view_request(request_id):
    """Display one request's details; return whether it was found."""
    if request_id not in requests:
        print("Request not found.")
        return False

    request = requests[request_id]
    print(f"Request ID: {request_id}")
    print(f"Requester: {request['requester']}")
    print(f"Equipment: {request['equipment']}")
    print(f"Quantity: {request['quantity']}")
    print(f"Status: {request['status']}")
    return True


def find_request():
    """Find and display a request by its unique ID."""
    request_id = input("Request ID to find: ").strip().upper()
    view_request(request_id)


def desk_report():
    """Display inventory totals, availability, outstanding requests, and records."""
    print("\n========== EQUIPMENT DESK REPORT ==========")
    print(f"{'Equipment':<20}{'Total':>8}{'Available':>12}{'Issued':>10}")

    for equipment_name, total_quantity in INVENTORY.items():
        quantity_issued = issued_quantity_for(equipment_name)
        quantity_available = total_quantity - quantity_issued
        print(
            f"{equipment_name:<20}{total_quantity:>8}"
            f"{quantity_available:>12}{quantity_issued:>10}"
        )

    print("\nPending requests:")
    found_pending = False

    for request_id, request in requests.items():
        if request["status"] == "Requested":
            found_pending = True
            print(
                f"{request_id} | {request['requester']} | "
                f"{request['equipment']} | Qty: {request['quantity']}"
            )

    if not found_pending:
        print("No pending requests.")

    print("\nAll request records:")
    if not requests:
        print("No requests have been registered.")
    else:
        for request_id in requests:
            print("\n---")
            view_request(request_id)

    print("\n===========================================")


def main():
    """Run the equipment desk menu until the user chooses to exit."""
    while True:
        print("\n===== CAMPUS MEDIA EQUIPMENT DESK =====")
        print("1. Register a request")
        print("2. Issue equipment")
        print("3. Record a return")
        print("4. Cancel a request")
        print("5. Find and view a request")
        print("6. Produce the desk report")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                register_request()
            case "2":
                issue_equipment()
            case "3":
                return_equipment()
            case "4":
                cancel_request()
            case "5":
                find_request()
            case "6":
                desk_report()
            case "0":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Choose an option from 0 to 6.")


if __name__ == "__main__":
    main()
