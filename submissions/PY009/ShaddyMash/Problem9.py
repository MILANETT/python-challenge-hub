
# Store the total number of each equipment
# The inventory dictionary maps each equipment name to the total number owned.
inventory = {
    "Projector": 4,
    "Laptop": 6,
    "Speaker": 3,
    "Microphone": 8,
    "Extension cable": 10
}

# Each request is stored by its unique ID, with its requester, item, quantity,
# and current status (Requested, Issued, Returned, or Cancelled).
requests = {
    "EQ001": {"name": "Computing Club", "item": "Projector", "quantity": 2, "status": "Issued"},
    "EQ002": {"name": "Debate Society", "item": "Microphone", "quantity": 3, "status": "Requested"},
    "EQ003": {"name": "Media Team", "item": "Laptop", "quantity": 2, "status": "Issued"}
}


def available(item):
    # Calculate how many units of an item are not currently on loan.
    issued = 0

    # Count equipment that has been issued
    for request in requests.values():
        if request["item"] == item and request["status"] == "Issued":
            issued += request["quantity"]

    # Subtract issued items from total stock
    return inventory[item] - issued


def register_request():
    # Collect and validate the details before adding a new pending request.
    request_id = input("Request ID: ").strip().upper()

    # Check if ID is empty or already exists
    if not request_id or request_id in requests:
        print("Request ID is empty or already exists.")
        return

    name = input("Requester name: ").strip()

    # Prevent empty requester names
    if not name:
        print("Requester name cannot be blank.")
        return

    print("Equipment:", ", ".join(inventory))
    item = input("Equipment name: ").strip().capitalize()

    # Check whether the equipment exists
    if item not in inventory:
        print("Equipment not found.")
        return

    text = input("Quantity: ").strip()

    # Check if quantity is a positive whole number
    # before converting it to an integer
    if not text.isdecimal() or int(text) == 0:
        print("Enter a positive whole number.")
        return

    # Save the new request
    requests[request_id] = {
        "name": name,
        "item": item,
        "quantity": int(text),
        "status": "Requested"
    }

    print("Request registered successfully.")


def change_request(action):
    # Find the selected request, then apply the requested status transition.
    request_id = input("Request ID: ").strip().upper()

    # Check whether the request exists
    if request_id not in requests:
        print("Request not found.")
        return

    request = requests[request_id]

    # Issue equipment
    if action == "Issue":

        # Only pending requests can be issued
        if request["status"] != "Requested":
            print("Only pending requests can be issued.")
            return

        # Check if enough equipment is available
        if request["quantity"] > available(request["item"]):
            print("Not enough equipment available.")
            return

        request["status"] = "Issued"

    # Return equipment
    elif action == "Return":

        # Only issued equipment can be returned
        if request["status"] != "Issued":
            print("This request has no equipment to return.")
            return

        # Return all equipment in this request
        request["status"] = "Returned"

    # Cancel a request
    elif action == "Cancel":

        # Issued requests cannot be cancelled
        if request["status"] != "Requested":
            print("Only pending requests can be cancelled.")
            return

        # Cancelling does not affect available stock
        request["status"] = "Cancelled"

    print(action, "successful.")


def find_request():
    # Look up one request by ID and print all of its stored fields.
    request_id = input("Request ID: ").strip().upper()

    # Check if request exists
    if request_id not in requests:
        print("Request not found.")
        return

    # Display the request details
    print("Request ID:", request_id)

    for key, value in requests[request_id].items():
        print(key.title() + ":", value)


def desk_report():
    # Summarize stock levels, pending requests, and every request on record.
    print("\nEQUIPMENT REPORT")

    # Display total, available and issued quantities
    for item, total in inventory.items():
        remaining = available(item)

        print(item, "- Total:", total,
              "Available:", remaining,
              "Issued:", total - remaining)

    print("\nPENDING REQUESTS")

    found = False

    # Display requests waiting to be issued
    for request_id, request in requests.items():
        if request["status"] == "Requested":
            print(request_id, request["name"],
                  request["item"], request["quantity"])
            found = True

    if not found:
        print("None")

    print("\nALL REQUESTS")

    # Display all requests and their current statuses
    for request_id, request in requests.items():
        print(request_id, request["name"],
              request["item"], request["quantity"],
              request["status"])


# Repeatedly show the menu and dispatch the user's choice until they exit.
while True:

    print("\nEQUIPMENT DESK")
    print("1. Register request")
    print("2. Issue equipment")
    print("3. Return equipment")
    print("4. Cancel request")
    print("5. Find request")
    print("6. Desk report")
    print("0. Exit")

    choice = input("Choose: ").strip()

    # Match the menu choice to the corresponding operation.
    match choice:

        case "1":
            register_request()

        case "2":
            change_request("Issue")

        case "3":
            change_request("Return")

        case "4":
            change_request("Cancel")

        case "5":
            find_request()

        case "6":
            desk_report()

        case "0":
            print("Goodbye!")
            break  # Stop the loop and exit

        case _:
            print("Invalid choice. Try again.")
