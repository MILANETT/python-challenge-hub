"""
PY009 — The Equipment Desk

Build your solution for the requirements in README.md.
Use CONCEPTS.md to check the programming concepts covered so far.

Keep your implementation understandable, test normal and rejected actions,
and add comments that explain important decisions.
"""

# Start your solution below.
# CAMPUS MEDIA UNIT BORROWING SYSTEM

#Equipment Inventory Storage
#A dictionary of lists and for each equipment there must be a total quantity in the corresponding index position
equip_inventory={
    "equipment":["Projector", "Laptop", "Speaker", "Microphone", "Extension cable"],
    #total quantity
    "total_qty":[4, 6, 3, 8, 10],
    #available quantity to facilitate borrowing
    "available_qty":[2, 4, 3, 8, 10]
}

#Requests Record Storage
#A dictionary of lists
req_record={
    "RequestID":["EQ001", "EQ002", "EQ003"],
    "Requester":["Computing Club", "Debate Society", "Media Team"],
    "Equipment":["Projector", "Microphone", "Laptop"],
    "Quantity":[2, 3, 2],
    "Status":["Issued", "Requested","Issued"]
}

#Functions
#Register function
def register_request(*,req_id,req_name,eqt_type,qty):
    '''

    :param req_id: takes the request id
    :param req_name: takes the requester name
    :param eqt_type:  take in the equipment type
    :param qty:  takes in the quantity of the equipment being borrowed
    '''

    #ID validation flag
    valid_id = False
    #Name validation flag
    valid_name = False
    #Equipment Availability validation flag
    valid_equipment = False
    #Quantity Available validation flag
    valid_quantity = False

    #Validating the id
    if req_id not in req_record["RequestID"]:
        valid_id = True
    #Validating the requester name
    if len(req_name) != 0:
        valid_name = True
    #Validating equipment's availability (case-insensitive check against inventory)
    matched_eqt = None
    for eq in equip_inventory["equipment"]:
        if eq.lower() == eqt_type.lower():
            matched_eqt = eq
            valid_equipment = True
            break

    #Validating quantity availability
    if qty.isdigit() and int(qty) > 0:
        valid_quantity = True

    # Once details are valid, add the request
    if valid_id and valid_name and valid_equipment and valid_quantity:
        req_record['RequestID'].append(req_id)
        req_record['Requester'].append(req_name)
        req_record['Equipment'].append(matched_eqt)
        req_record['Quantity'].append(int(qty))
        req_record['Status'].append('Requested')
        print(f"✅ Request {req_id} registered Successfully!!!")

    # In the case of an invalid id, already existing ID
    else:
        if not valid_id:
            print(f"Recent registered Request ID: {req_record['RequestID'][-1]}")
            print("❌ Enter a valid non-existent ID!!!")
        # In the case of a blank requester name
        if not valid_name:
            print("❌ Requester's name cannot be blank!!!")
        # In the of an inexistent equipment type
        if not valid_equipment:
            print("❌ The equipment does not exist!!!")
        # In the case of a negative quantity
        if not valid_quantity:
            print("❌ Quantity must be a positive whole number!!!")

#Issue function
def issue_equipment(req_id):
    #Request existence validation flag
    request_exists= False
    #Requested status validation flag
    valid_status = False
    #Equipment existence validation flag
    equipment_exists = False
    #Validating request's existence
    if req_id in req_record["RequestID"]:
        request_exists = True
        req_idx = req_record["RequestID"].index(req_id)
        #Validating status "Requested" state
        if req_record["Status"][req_idx] == "Requested":
            valid_status = True
            requested_eqt = req_record["Equipment"][req_idx]
            #Validating Equipment existence state with its quantity
            if requested_eqt in equip_inventory["equipment"]:
                eqt_idx = equip_inventory["equipment"].index(requested_eqt)
                req_qty = req_record["Quantity"][req_idx]
                if equip_inventory["available_qty"][eqt_idx] >= req_qty:
                    equipment_exists = True
                    #Deducting issued equipment to balance records
                    equip_inventory["available_qty"][eqt_idx] -= req_qty
                    #Updating status of request to "Issued"
                    req_record["Status"][req_idx] = "Issued"
                    print("✅ Issued Successfully!!!")

    # In the case of a request that does not exist
    if not request_exists:
        print("❌ Request has not been made!!!")

    # In the case of a status that is not "Requested"
    elif not valid_status:
        print("❌ Status must be 'Requested'!!!")

    # In the case of equipment with insufficient quantity
    elif not equipment_exists:
        print("❌ Equipment not enough!!!")


#Return Function
def return_equipment(req_id):
    # Request existence validation flag
    request_exists = False
    # Issued status validation flag
    valid_status = False
    # Validating request's existence
    if req_id in req_record["RequestID"]:
        request_exists = True
        req_idx = req_record["RequestID"].index(req_id)
        current_status = req_record["Status"][req_idx]

        # 1. Check if it was already returned
        if current_status == "Returned":
            print("❌ Request has already been returned!!!")
            return  # Stop execution here
        # Validating status "Issued" state
        elif current_status == "Issued":
            valid_status = True
            returned_eqt = req_record["Equipment"][req_idx]
            eqt_idx = equip_inventory["equipment"].index(returned_eqt)
            #Adding the equipment back and changing status to "Returned"
            # Adding the equipment back
            equip_inventory["available_qty"][eqt_idx] += req_record["Quantity"][req_idx]
            #changing status to "Returned"
            req_record["Status"][req_idx] = "Returned"
            print("✅ Returned Successfully!!!")

    # In the case of a request that does not exist
    if not request_exists:
        print("❌ Request has not been made!!!")
    # In the case of a status that is not "Issued"
    elif not valid_status:
        print("❌ Status must be 'Issued'!!!")

#Cancel Function
def cancel_request(req_id):
    # Request existence validation flag
    request_exists = False
    # Requested status validation flag
    valid_status = False
    # Validating request's existence
    if req_id in req_record["RequestID"]:
        request_exists = True
        req_idx = req_record["RequestID"].index(req_id)
        current_status = req_record["Status"][req_idx]

        if current_status == "Cancelled":
            print("❌ Request has already been cancelled!!!")
            return
        #Validating status "Requested" state
        elif current_status == "Requested":
            valid_status = True
            #Changing the status to "Cancelled"
            req_record["Status"][req_idx] = "Cancelled"
            print("✅ Cancelled Successfully!!!")

    # In the case of a request that does not exist
    if not request_exists:
        print("❌ Request has not been made!!!")
    # In the case of a status that is not "Requested"
    elif not valid_status:
        print("❌ Status must be 'Requested'!!!")

#View Function
def view_request(req_id):
    # Request existence validation flag
    request_exists = False
    # Validating request's existence
    if req_id in req_record["RequestID"]:
        request_exists = True
        #Saving the index to help retrieve correct details
        req_idx = req_record["RequestID"].index(req_id)
        #Displaying the details
        print(f"Request ID: {req_record['RequestID'][req_idx]}")
        print(f"Requester Name: {req_record['Requester'][req_idx]}")
        print(f"Equipment Type: {req_record['Equipment'][req_idx]}")
        print(f"Quantity: {req_record['Quantity'][req_idx]}")
        print(f"Status: {req_record['Status'][req_idx]}")

    # In the case of a request that does not exist
    if not request_exists:
        print("❌ Request has not been made!!!")

#Report Function
def desk_report():
    print("---Equipment Details---")
    for i in range(len(equip_inventory["equipment"])):
        eqp = equip_inventory["equipment"][i]
        qty = equip_inventory["total_qty"][i]
        av_qty = equip_inventory["available_qty"][i]
        issued_qty = qty - av_qty
        #AI helped me to organize my display by inclusion of mandatory whitespaces using <
        print(f"{eqp:<16} | Total Quantity: {qty:<2} | Available Quantity: {av_qty:<2} | Quantity Currently Issued: {issued_qty:<2}")
    print("---Pending Requests---")
    has_pending = False
    for i in range(len(req_record["RequestID"])):
        if req_record["Status"][i] == "Requested":
            has_pending = True
            print(
                f"Request ID: {req_record['RequestID'][i]} | Requester: {req_record['Requester'][i]} | Equipment: {req_record['Equipment'][i]} | Qty: {req_record['Quantity'][i]}")

    if not has_pending:
        print("(No pending requests)")

#Available equipment function
def available_equip():
    print("---Available Equipment---")
    for i in range(len(equip_inventory["equipment"])):
        eqp = equip_inventory["equipment"][i]
        av_qty = equip_inventory["available_qty"][i]
        # AI helped me to organize my display by inclusion of mandatory whitespaces using <
        print(f"{eqp:<16} | Available Quantity: {av_qty:<2} ")


#Program
#Welcome Message
print("="*30)
print("\nCAMPUS MEDIA UNIT BORROWING SYSTEM\n")
print("="*30)
#The Menu
print("Here is the Menu:")
print("1. Register a Request")
print("2. Issue Equipment")
print("3. Record a Return")
print("4. Cancel a Request")
print("5. View a Request")
print("6. Produce a Desk Report")
print("7. Exit")

while True:
    choice=input("Enter a borrowing operation number(1 - 7):\n").strip()
    match choice:
        case "1":
            #Register a request
            # print last Request ID to hint the staff what ID should be next
            print("---Register a request---")
            print(f"Recent registered Request ID: {req_record['RequestID'][-1]}")
            new_request_ID = input("Request ID: ").strip().upper()
            new_requester_name = input("Requester Name: ").strip().capitalize()
            available_equip()
            new_equipment_type = input("Equipment Type: ").strip().capitalize()
            new_quantity = input("Quantity: ")
            register_request(req_id = new_request_ID, req_name = new_requester_name, eqt_type = new_equipment_type, qty = new_quantity)

        case "2":
            #Issue Equipment
            print("---Issue Equipment---")
            request_id = input("Request ID: ").strip().upper()
            issue_equipment(request_id)

        case "3":
            #Record a Return
            print("---Record a Return---")
            request_id = input("Request ID: ").strip().upper()
            return_equipment(request_id)

        case "4":
            #Cancel a Request
            print("---Cancel a Request---")
            request_id = input("Request ID: ").strip().upper()
            cancel_request(request_id)

        case "5":
            #View a request
            print("---View a Request---")
            request_id = input("Request ID: ").strip().upper()
            view_request(request_id)

        case "6":
            #Produce a Desk Report
            print("---Desk Report---")
            desk_report()

        case "7":
            #Exit
            print("Exited the program successfully")
            break

        case _:
            print("Enter a valid choice between 1 and 7")
            continue