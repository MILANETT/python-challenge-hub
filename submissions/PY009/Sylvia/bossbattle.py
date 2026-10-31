inventoryNo=int(input("Enter the number of equipment to be stored: "))
inventory=[
        {"Equipment": "Projector", "Total quantity": 4, "Issued": 2},
        {"Equipment": "Laptop", "Total quantity": 6, "Issued": 2},
        {"Equipment": "Speaker", "Total quantity": 3, "Issued": 0},
        {"Equipment": "Microphone", "Total quantity": 8, "Issued": 0},
        {"Equipment": "Extension cable", "Total quantity": 10, "Issued": 0},
]

#this for loop is to add new information to the inventory
for x in range(inventoryNo):
    inventoryEquipment=input("Enter the item to be recorded: ").title()
    # Prevent duplicate equipment names
    while any(
        item["Equipment"].casefold() == inventoryEquipment.casefold()
        for item in inventory
    ):
        print("Equipment already exists.")
        inventoryEquipment = input(
            "Enter a different equipment name: "
        ).strip().title()

    inventoryQuantity=int(input("Enter the total quantity: "))
#this if..else statement is used to check whether the input quantity is a positive whole number
#If the conditions are fulfilled it proceeds.If otherwise,new input is required
    while not inventoryQuantity > 0:
        print("Quantity must be greater than zero.")
        inventoryQuantity=int(input("Enter the total quantity: "))
       
    inventory.append(
        {
        "Equipment":inventoryEquipment,
        "Total quantity":inventoryQuantity,
        "Issued":0
        }

    )
    print(inventory)

recordsNo=int(input("Enter the number of  borrowed equipment to be recorded: "))
requests = [
    {
            "RequestID": "EQ001",
            "Requester": "Computing Club",
            "Equipment": "Projector",
            "Quantity": 2,
            "Status": "Issued",
        },
        {
            "RequestID": "EQ002",
            "Requester": "Debate Society",
            "Equipment": "Microphone",
            "Quantity": 3,
            "Status": "Requested",
        },
        {
            "RequestID": "EQ003",
            "Requester": "Media Team",
            "Equipment": "Laptop",
            "Quantity": 2,
            "Status": "Issued",
        }
]

#this for loop is to add new information to the inventory
for x in range(recordsNo):
    requestID=input("Enter the requester ID: ").strip().upper()

    #this while loop is used to check whether a requestID is unique before input
    while any(request["RequestID"] == requestID for request in requests):
        print("Request ID already exists.")
        requestID=input("Enter the requester ID: ").strip().upper()
    else:
        print("Request ID is available.")
      
    requester_=input("Enter the requester's name: ").strip().title()
    #this while loop is used to ensure the requester name is not blank
    while not requester_:
        print("Requester name cannot be blank.")
        requester_ = input("Enter the requester's name: ").strip().title()


    equipment=input("Enter the borrowed equipment: ").title()
    while not any(
        item["Equipment"].casefold() == equipment.casefold()
        for item in inventory
    ):
        print("Equipment not found in inventory.")
        equipment = input("Enter a valid equipment type: ").strip().title()



    quantity=int(input("Enter the quantity borrowed: "))
#this if..else statement is used to check whether the input quantity is a positive whole number
#If the conditions are fulfilled it proceeds.If otherwise,new input is required
    while not quantity > 0:
            print("Quantity must be greater than zero.")
            inventoryQuantity=int(input("Enter the quantity borrowed: "))
        

#when one inputs the data it is appended into the requests list
#this creates a list of dictionaries
    requests.append(
        {
        "RequestID":requestID.upper(),
        "Requester":requester_,
        "Equipment":equipment,
        "Quantity":quantity,
        "Status":"Requested"
        }
    )
    print(requests)
#Find an equipment record by name.
def find_equipment(equipment):
    for equipment_record in inventory:
        if equipment_record["Equipment"].casefold() == equipment.casefold():
            return equipment_record
    return None

#Find an equipment record by name.
def find_request(requestId):
    for request_record in requests:
        if request_record["RequestID"] == requestId.strip().upper():
            return request_record
    return None


#Issue a pending request if enough equipment is available.
def issueRequest(requestId):
    request_record = find_request(requestId)
    if request_record is None:
        print("Request ID not found.")
        return
    if request_record["Status"] != "Requested":
        print("This request is not eligible for issuing.")
        return

    equipment_record = find_equipment(request_record["Equipment"])
    if equipment_record is None:
        print("Equipment not found in inventory.")
        return

    available = equipment_record["Total quantity"] - equipment_record["Issued"]
    if request_record["Quantity"] > available:
        print("Equipment is insufficient.")
        return

    equipment_record["Issued"] += request_record["Quantity"]
    request_record["Status"] = "Issued"
    print("Request issued.")


#Return equipment for an issued request.
def returnIssue(requestId):
    request_record = find_request(requestId)
    if request_record is None:
        print("Request ID not found.")
        return
    if request_record["Status"] != "Issued":
        print("This request has no issued equipment to return.")
        return

    equipment_record = find_equipment(request_record["Equipment"])
    if equipment_record is None:
        print("Equipment not found in inventory.")
        return

    equipment_record["Issued"] -= request_record["Quantity"]
    request_record["Status"] = "Returned"
    print("Equipment returned.")


#Cancel a pending request.
def cancelRequest(requestId):
    request_record = find_request(requestId)
    if request_record is None:
        print("Request ID not found.")
        return
    if request_record["Status"] != "Requested":
        print("Only pending requests can be cancelled.")
        return

    request_record["Status"] = "Cancelled"
    print("Request cancelled.")

#It gives the inventory report showing the quantities,statuses of equipment and the request

def inventoryReport():
    print("\n===== EQUIPMENT INVENTORY REPORT =====")
    print(f"{'Equipment':<20}{'Total':<10}{'Issued':<10}{'Available':<10}")

    for equipment_record in inventory:
        total = equipment_record["Total quantity"]
        issued = equipment_record["Issued"]
        available = total - issued
        print(f"{equipment_record['Equipment']:<20}{total:<10}{issued:<10}{available:<10}")


    print("\n===== PENDING REQUESTS =====")
    print(f"{'RequestID':<12}{'Requester':<20}{'Equipment':<20}{'Quantity':<10}{'Status':<12}")
    print("-" * 74)

    pending_found = False

    for request in requests:
        if request["Status"] == "Requested":
            print(
                f"{request['RequestID']:<12}"
                f"{request['Requester']:<20}"
                f"{request['Equipment']:<20}"
                f"{request['Quantity']:<10}"
                f"{request['Status']:<12}"
            )
            pending_found = True

    if not pending_found:
        print("No pending requests.")

inventoryReport()

def inventoryMenu():
    while True:
        print("\n1. Issue request")
        print("2. Return equipment")
        print("3. Cancel request")
        print("4. Inventory report")
        print("5. Exit")
        choice = input("Choose an operation: ").strip()

        if choice == "1":
            issueRequest(input("Enter the request ID: "))
        elif choice == "2":
            returnIssue(input("Enter the request ID: "))
        elif choice == "3":
            cancelRequest(input("Enter the request ID: "))
        elif choice == "4":
            inventoryReport()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Please choose an option from 1 to 5.")

inventoryMenu()


