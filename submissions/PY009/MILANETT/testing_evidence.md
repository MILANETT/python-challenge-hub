# 🧪 Testing Evidence: PY009 — The Equipment Desk

**System:** Campus Media Unit Borrowing System  
**Execution Environment:** Python 3.10+ (`uv run python PY009.py`)  
**Status:** ✅ All Test Cases Passing  

---

## 📜 Execution Session Output Log

```text
==============================

CAMPUS MEDIA UNIT BORROWING SYSTEM

==============================
Here is the Menu:
1. Register a Request
2. Issue Equipment
3. Record a Return
4. Cancel a Request
5. View a Request
6. Produce a Desk Report
7. Exit

Enter a borrowing operation number(1 - 7):
1
---Register a request---
Recent registered Request ID: EQ003
Request ID: EQ004
Requester Name: Wendy
Equipment Type: speaker
Quantity: 1
✅ Request EQ004 registered Successfully!!!

Enter a borrowing operation number(1 - 7):
1
---Register a request---
Recent registered Request ID: EQ004
Request ID: eq003
Requester Name: Willy
Equipment Type: laptop
Quantity: 1
Recent registered Request ID: EQ004
❌ Enter a valid non-existent ID!!!

Enter a borrowing operation number(1 - 7):
1
---Register a request---
Recent registered Request ID: EQ004
Request ID: eq005
Requester Name: 
Equipment Type: microphone
Quantity: 2
❌ Requester's name cannot be blank!!!

Enter a borrowing operation number(1 - 7):
1
---Register a request---
Recent registered Request ID: EQ004
Request ID: eq005
Requester Name: Willy
Equipment Type: stylus
Quantity: 3
❌ The equipment does not exist!!!

Enter a borrowing operation number(1 - 7):
1
---Register a request---
Recent registered Request ID: EQ004
Request ID: eq005
Requester Name: Willy
Equipment Type: laptop
Quantity: 3
✅ Request EQ005 registered Successfully!!!

Enter a borrowing operation number(1 - 7):
1
---Register a request---
Recent registered Request ID: EQ005
Request ID: eq006
Requester Name: Wonka
Equipment Type: laptop
Quantity: -9
❌ Quantity must be a positive whole number!!!

Enter a borrowing operation number(1 - 7):
2
---Issue Equipment---
Request ID: eq005
✅ Issued Successfully!!!

Enter a borrowing operation number(1 - 7):
2
---Issue Equipment---
Request ID: eq009
❌ Request has not been made!!!

Enter a borrowing operation number(1 - 7):
2
---Issue Equipment---
Request ID: eq005
❌ Status must be 'Requested'!!! Current status: 'Issued'

Enter a borrowing operation number(1 - 7):
1
---Register a request---
Recent registered Request ID: EQ005
Request ID: eq006
Requester Name: Wonka
Equipment Type: laptop
Quantity: 10
✅ Request EQ006 registered Successfully!!!

Enter a borrowing operation number(1 - 7):
2
---Issue Equipment---
Request ID: eq006
❌ Equipment not enough!!! Required: 10, Available: 1

Enter a borrowing operation number(1 - 7):
3
---Record a Return---
Request ID: eq005
✅ Returned Successfully!!!

Enter a borrowing operation number(1 - 7):
3
---Record a Return---
Request ID: eq010
❌ Request has not been made!!!

Enter a borrowing operation number(1 - 7):
3
---Record a Return---
Request ID: eq002
❌ Status must be 'Issued' to record return!!! Current status: 'Requested'

Enter a borrowing operation number(1 - 7):
3
---Record a Return---
Request ID: eq005
❌ Request has already been returned!!!

Enter a borrowing operation number(1 - 7):
4
---Cancel a Request---
Request ID: eq002
✅ Cancelled Successfully!!!

Enter a borrowing operation number(1 - 7):
4
---Cancel a Request---
Request ID: eq010
❌ Request has not been made!!!

Enter a borrowing operation number(1 - 7):
5
---View a Request---
Request ID: eq001
Request ID: EQ001
Requester Name: Computing Club
Equipment Type: Projector
Quantity: 2
Status: Issued

Enter a borrowing operation number(1 - 7):
5
---View a Request---
Request ID: eq010
❌ Request has not been made!!!

Enter a borrowing operation number(1 - 7):
6
---Desk Report---

---Equipment Details---
Projector        | Total Quantity: 4  | Available Quantity: 2  | Quantity Currently Issued: 2 
Laptop           | Total Quantity: 6  | Available Quantity: 4  | Quantity Currently Issued: 2 
Speaker          | Total Quantity: 3  | Available Quantity: 3  | Quantity Currently Issued: 0 
Microphone       | Total Quantity: 8  | Available Quantity: 8  | Quantity Currently Issued: 0 
Extension cable  | Total Quantity: 10 | Available Quantity: 10 | Quantity Currently Issued: 0 

---Pending Requests---
Request ID: EQ004 | Requester: Wendy | Equipment: Speaker | Qty: 1
Request ID: EQ006 | Requester: Wonka | Equipment: Laptop | Qty: 10

Enter a borrowing operation number(1 - 7):
7
Exited the program successfully