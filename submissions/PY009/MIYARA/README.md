MY APPROACH
I started by storing the equipment details in a dictionary "equipment" and the request details in the dictionary "desk". I then created functions for each task to be carried out.

I created function request_register used for registering requests and passed the two dictionaries (equipment and desk)as parameters. In the function I prompted the user for a request ID and checked if the ID is unique. I also prompted the user for a request_name , equipment_type and the quantity while making sure that the requester_name isn't blank and the equipment_type already exists and the quantity is aa positive number and added the details entered back into the desk dictionary.

I created function issue_equip and passed equipment and desk as the parameters and asked the user for the request ID to check whether such a request existed. I checked if the status key in the dictionary had the value requested so that an equipment can only be issued if and only if it had been requested. I then instantiated the issued_quantity to 0 and created a for loop that counts every equipment that is issued and reassigns the issue_quantity value.I also calculated the available_quantity and added a check to see whether the quantity requested didn't exceed the available_quantity.

I created function record_return and passed the parameter desk.I asked the user for the request ID to check whether such a request existed . I checked if the status of the request was issued to ascertain that an equipment can only be returned if only it was issued.


I created function find_request that once a user enter a valid request_id it prints out the details of the request ID.

I created function display_report and passed the parameters equipment and desk that printed the details of all Equpiment through the for loop.

I then created a match case for the program so as to run each task from simple inputs.




