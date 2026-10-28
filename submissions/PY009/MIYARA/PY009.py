equipment = {  # Dictionary to store equipment items and their quantities
    "Projector": 4,
    "Laptop": 6,
    "Speaker": 3,
    "Microphone": 8,
    "Extension Cable": 10
}

desk = {  # Dictionary to store each request and their details
    "EQ001": {
        "Requester": "Computing Club",
        "Equipment": "Projector",
        "Quantity": 2,
        "Status": "Issued"
    },
    "EQ002": {
        "Requester": "Debate Society",
        "Equipment": "Microphone",
        "Quantity": 3,
        "Status": "Requested"
    },
    "EQ003": {
        "Requester": "Media Team",
        "Equipment": "Laptop",
        "Quantity": 2,
        "Status": "Issued"
    }
}


def register_request(equipment, desk):  # function to register a new request
    request_id = input("Enter the request ID:")
    while request_id in desk:  # Checks if the request Id is unique by checking if it already exists
        print("ID already exists!")
        # Prompts the user again to enter the Id incase the ID input matches one that already exists
        request_id = input("Enter the request ID:")

    requester_name = input("Enter the requester name:").strip().title()
    if requester_name == "":  # Checks if the user fails to input a requester name and returns the user back to the first/initial stage
        print("Requester name cannot be blank")
        return

    equip_type = input("Enter the equipment type:").title().strip()
    if equip_type not in equipment:  # Checks if the equipment type entered exists in the records
        print("Equipment not found!")
        return

    quantity_ = input("Enter the quantity:")
    if quantity_.isdigit():  # Returns true if the string is a digit
        quantity_int = int(quantity_)  # Converts the string into an integer
        if quantity_int <= 0:  # Checks if the number is a positive number
            print("Enter a number above 0")
            return
    else:
        print("Invalid input")
        return

    desk[request_id] = {  # Creates and saves a brand new record into the desk dictonary
        "Requester": requester_name,
        "Equipment": equip_type,
        "Quantity": quantity_int,
        "Status": "Requested"
    }
    print("Request successfully registered")


def issue_equip(equipment, desk):  # Funstion to issue a registered request
    req_id = input("Enter the request ID to issue:")
    if req_id not in desk:  # Checks if the request ID input exists in the records
        print("Request not found")
        return

    req = desk[req_id]  # Fetches a specific record in the dest dictionary
    if req["Status"] != "Requested":  # Checks if the status is requested so as to issue the equipment
        print(
            "Cannot issue a request that is not requested !Current status is:", req["Status"])
        return

    # Identifies the kind of equipment the user requested
    equi = req["Equipment"]
    # looks up the equipment dict to see the total quantity of the equipment
    total = equipment[equi]
    issued_quantity = 0  # A running counter for the issued equipment
    for details in desk.values():  # loops through the values in desk/ the nested dictionary in desk
        if details["Equipment"] == equi and details["Status"] == "Issued":
            # Counts the number of issued equipment
            issued_quantity += details["Quantity"]

    # Counts tthe number of available equipment
    available_quantity = total - issued_quantity

    # Checks if teh requested quantity is greater than the actual quantity in the records
    if req["Quantity"] > available_quantity:
        print("Quantity not available!")
    else:
        # Issues a request whose quantity does not exceed that which is available
        req["Status"] = "Issued"
        print("Equipment successfully issued!")


def record_return(desk):
    req_id = input("Enter request ID to return:")
    if req_id not in desk:  # Checks if the request ID input exists in the records
        print("Request ID not found!")
        return

    req = desk[req_id]
    if req["Status"] != "Issued":
        print("Equipment can't be returned if it wasn't issued")
    else:
        # Returns an equipment only if it passes a check that it had been issued
        req["Status"] = "Returned"
        print("Equipment successfully returned!")


def cancel_request(desk):
    req_id = input("Enter request ID to cancel:")
    if req_id not in desk:
        print("Request ID not found!")
        return

    req = desk[req_id]
    if req["Status"] != "Requested":
        print("Request can't be cancelled if it was not requested")
    else:
        # cancels a request if it had been requested and not issued
        req["Status"] = "Cancelled"
        print("Request cancelled successfully!")


def find_request(desk):
    req_id = input("Enter request ID to search: ").strip()
    if req_id in desk:  # Prints the details of the request if the request ID is in the desk dict
        details = desk[req_id]
        print("===============================")
        print("--------Request Details--------")
        print(f"Request ID : {req_id}")
        print(f"Requester : {details['Requester']}")
        print(f"Equipment : {details['Equipment']}")
        print(f"Quantity : {details['Quantity']}")
        print(f"Status : {details['Status']}")
    else:
        print("Request ID not found.")


def display_report(equipment, desk):  # Function to display the whole report
    print("\n===============================")
    print("DESK INVENTORY REPORT")
    for equi, number in equipment.items():
        issued_quantity = 0
        for details in desk.values():
            if details["Equipment"] == equi and details["Status"] == "Issued":
                issued_quantity += details["Quantity"]

        available_quantity = number - issued_quantity
        print(f"Equipment Name : {equi}")
        print(f"Total : {number}")
        print(f"Issued : {issued_quantity}")
        print(f"Available : {available_quantity}")
        print("-------------------------------")

    print("\n--- Pending & Active Requests ---")
    for r_id, details in desk.items():
        if details["Status"] in ["Requested", "Issued"]:
            print(
                f"ID: {r_id}  Requester: {details['Requester']}  Item: {details['Equipment']}  Qty: {details['Quantity']}  Status: {details['Status']}")


while True:  # Match case Menu for the program
    print("\n=== CAMPUS MEDIA EQUIPMENT DESK ===")
    print("1. Register a new request")
    print("2. Issue equipment against a request")
    print("3. Record a return")
    print("4. Cancel a request")
    print("5. Find and view request details")
    print("6. Produce desk report")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    match choice:
        case "1":
            register_request(equipment, desk)
        case "2":
            issue_equip(equipment, desk)
        case "3":
            record_return(desk)
        case "4":
            cancel_request(desk)
        case "5":
            find_request(desk)
        case "6":
            display_report(equipment, desk)
        case "7":
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please enter a number between 1 and 7.")
