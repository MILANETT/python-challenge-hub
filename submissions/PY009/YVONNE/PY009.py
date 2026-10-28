print("THE EQUIPMENT DESK")

# dictionary to store equipments available and their quantities
inventory = {
    "Projector": {"total": 4, "available": 4},
    "Laptop": {"total": 6, "available": 6},
    "Speaker": {"total": 3, "available": 3},
    "Microphone": {"total": 8, "available": 8},
    "Extention_Cable": {"total": 10, "available": 10}
}

#initialize an empty set to store the request ids..set does not allow duplicates
requests = {}



# Function to display available equipment types
def show_equipment_available():
    print("\nAvailable equipment:")

    for equipment_type in inventory:
        print("-", equipment_type)


# Function to register a new request
def register_request():
    #prompt user to input request id and strip the white spaces
    request_id = input("Enter a unique request ID: ").strip()

    #ensure request id is not left blank
    if  request_id == "":
        print("Request ID cannot be blank.")
        return
    
    #ensure that request id is unique and not in the request{}
    if request_id in requests:
        print("That request ID already exists.")
        return

    #prompt for requester name and strip white spaces
    requester = input("Enter requester name: ").strip()

    #ensure the requester name is not blank
    if requester == "":
        print("Requester name cannot be blank.")
        return

    #show the equipments available in the inventory so the user can choose from
    show_equipment_available()

    #prompt the requester to choose the equipment they want from the list of equipments
    equipment_type = input(
        "Enter equipment type exactly as listed: "
    ).strip()

    #ensure the equipment choosen is in the inventory
    if equipment_type not in inventory:
        print("Invalid equipment type.")
        return

    #if equipment choosen is in the inventory ask for the quantity needed
    quantity = int(input(
        "Enter how many equipments you need: "
    ))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return  

    # New requests begin in Pending status
    requests[request_id] = {
        "requester": requester,
        "equipment_type": equipment_type,
        "quantity": quantity,
        "status": "Pending"
    }

    print(f"Request {request_id} for {quantity} {equipment_type}s registered successfully.")


# Function to issue equipment against a request
def issue_equipment():
    request_id = input("Enter the request ID to issue: ").strip()

    #check if the request is registered already
    if request_id not in requests:
        print("Request not found.")
        return

    request = requests[request_id]

    #ensure that the requester had alsready made a request before issueing an equipment
    if request["status"] != "Pending":
        print("Only pending requests can be issued.")
        return

    #make comparison between the equipment quantity made by the requster to the equipment available
    equipment_type = request["equipment_type"]
    quantity = request["quantity"]

    if quantity > inventory[equipment_type]["available"]:
        print("Not enough equipment is available.")
        return

    # Reduce available equipment after issuing
    inventory[equipment_type]["available"] -= quantity

    request["status"] = "Issued"

    print(f"Request {request_id} for {quantity} {equipment_type} issued successfully.")


# Function to record returned equipment
def return_equipment():
    request_id = input("Enter the request ID to return: ").strip()

    if request_id not in requests:
        print("Request not found.")
        return

    request = requests[request_id]

    if request["status"] != "Issued":
        print("This request has no outstanding issue to return.")
        return

    equipment_type = request["equipment_type"]
    quantity = request["quantity"]

    # Restore the equipment that is returned
    inventory[equipment_type]["available"] += quantity

    request["status"] = "Returned"

    print(f"Equipment for request {request_id} returned successfully.")


# Function to cancel a request
def cancel_request():
    request_id = input("Enter the request ID to cancel: ").strip()

    if request_id not in requests:
        print("Request not found.")
        return

    request = requests[request_id]

    if request["status"] != "Pending":
        print("Only requests that have not been issued can be cancelled.")
        return

    # Cancelling a pending request which does not affect inventory
    request["status"] = "Cancelled"

    print(f"Request {request_id} cancelled successfully.")


# Function to display  request
def view_request(request_id):
    request = requests[request_id]

    print(f"Request ID: {request_id}")
    print(f"Requester: {request['requester']}")
    print(f"Equipment type: {request['equipment_type']}")
    print(f"Quantity: {request['quantity']}")
    print(f"Status: {request['status']}")


# Function to find requests by ID or requester name
def find_requests():
    if not requests:
        print("There are no registered requests.")
        return

    search_request = input(
        "Enter a request ID or requester name to search: "
    ).strip()

    if search_request == "":
        print("Search value cannot be blank.")
        return

    matches = []

    for request_id, request in requests.items():

        if (
            request_id.lower() == search_request.lower()
            or search_request.lower() in request["requester"].lower()
        ):
            matches.append(request_id)

    if not matches:
        print("No matching requests found.")
        return

    for request_id in matches:
        print("\n--- Request details ---")
        view_request(request_id)


# Function to generate the desk report
def desk_report():
    print("\n========== EQUIPMENT DESK REPORT ==========")

    print("\nInventory summary:")

    print(
        f"{'Equipment':<15}"
        f"{'Total':>10}"
        f"{'Available':>12}"
        f"{'Issued':>10}"
    )

    for equipment_type, stock in inventory.items():

        total = stock["total"]
        available = stock["available"]

        # Issued quantity is total stock minus available stock
        issued = total - available

        print(
            f"{equipment_type:<15}"
            f"{total:>10}"
            f"{available:>12}"
            f"{issued:>10}"
        )

    print("\nPending requests:")

    pending_found = False

    for request_id, request in requests.items():

        if request["status"] == "Pending":
            pending_found = True

            print(
                f"ID: {request_id} | "
                f"Requester: {request['requester']} | "
                f"Equipment: {request['equipment_type']} | "
                f"Quantity: {request['quantity']}"
            )

    if not pending_found:
        print("There are no pending requests.")

    print("\nAll request records:")

    if not requests:
        print("There are no registered requests.")

    else:
        for request_id in requests:
            print("\n---")
            view_request(request_id)

    print("\n===========================================")


# Main function containing the menu
def main():

    while True:

        print("\n===== EQUIPMENT REQUEST SYSTEM =====")
        print("1. Register a request")
        print("2. Issue equipment")
        print("3. Record a return")
        print("4. Cancel a request")
        print("5. Find and view requests")
        print("6. Produce desk report")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            register_request()

        elif choice == "2":
            issue_equipment()

        elif choice == "3":
            return_equipment()

        elif choice == "4":
            cancel_request()

        elif choice == "5":
            find_requests()

        elif choice == "6":
            desk_report()

        elif choice == "7":
            print("Exiting the equipment request system. Goodbye!")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 7.")


# Start the program
main()