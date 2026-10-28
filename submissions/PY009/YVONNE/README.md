MY APPROACH FOR THE CHALLENGE 009 
---
I created a dictionary inventory that contained all available equipments and the quantity available.  
I initialized an empty set requests to store the request IDs .I then created a function show_equipment_available()that displays all equipments available in the inventory.  


I created a function register_request() that prompts user for request id,the requester name,equipment type the requester wants ,quantity.It ensures the the request ID is not left blank and is not already registered in the requests(unique).It ensures the requester name is not left blank .It then shows the requester what equipment are available to choose from.It then asks the requester to enter the equipment they need and the validates that the equipment is available,it asks for the quantity they need and the quantity should be an integer and not less than 0.  


issue_equipment() function issues an equipment when a request is made and also compares if equipment quantity made by the requester to the equipment available and reduces the equipment available after issuing.  


return_equipment() records a returned equipment and updates the inventory.

cancel_request() cancels a requests while its pending.

view_requests() displays request.

find_request() searches to see if a request using ID or requester name.

desk_report() generates the equipment desk report.

main() function creates choices for a user to choose from whatever they want to do and according to their choice the respective function is called.
