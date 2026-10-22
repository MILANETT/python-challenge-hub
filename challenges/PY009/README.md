# 🐍 PY009 — The Equipment Desk

**Phase:** Phase 4 — Boss Battle  
**Difficulty:** Cumulative  
**Estimated time:** 90–120 minutes  
**Deadline:** Sunday, 25 October 2026, at 8:00 PM EAT

The campus media unit has been struggling to manage equipment borrowed by student clubs and departments. Requests are recorded inconsistently, staff sometimes issue equipment that is unavailable, and nobody can quickly tell what is still out or how much equipment remains.

The unit has asked you to develop a small program that can manage its equipment desk and give staff a reliable picture of what is happening.

## Equipment inventory

Start with the following equipment and quantities:

| Equipment | Total quantity |
|---|---:|
| Projector | 4 |
| Laptop | 6 |
| Speaker | 3 |
| Microphone | 8 |
| Extension cable | 10 |

The desk already has these requests on record:

| Request ID | Requester | Equipment | Quantity | Status |
|---|---|---|---:|---|
| EQ001 | Computing Club | Projector | 2 | Issued |
| EQ002 | Debate Society | Microphone | 3 | Requested |
| EQ003 | Media Team | Laptop | 2 | Issued |

## What the unit needs

Staff should be able to use the program to:

- Register a request with a unique request ID, requester name, equipment type, and quantity.
- Issue equipment against a request when the request is eligible and enough equipment is available.
- Record a return against an outstanding issue.
- Cancel a request that has not yet been issued.
- Find and view request records and their current statuses.
- Produce a desk report showing each equipment type's total quantity, available quantity, and quantity currently issued, along with pending requests and useful request details.
- Perform multiple operations in one run.

## Operating rules

- Request IDs must be unique.
- Requester names must not be blank.
- The equipment type must match one of the listed inventory items.
- The quantity must be a positive whole number.
- The program must not issue more equipment than is available.
- Equipment may only be returned against a valid request that has been issued and not yet returned.
- A request must not be returned more than once.
- Only a request that has not been issued may be cancelled. Issued equipment must be returned through the return process.
- A cancelled request must not affect inventory quantities.
- Invalid choices or requests should be rejected with a clear message. Validate quantity text before converting it to an integer so non-numeric input can be handled without relying on exception handling.
- The inventory must remain consistent as requests are issued and equipment is returned.

You may make reasonable additional decisions where the requirements leave room for interpretation. Explain important assumptions in comments.

## What to submit

Submit your Python program and testing evidence that demonstrates normal operations and rejected actions. Your code should be readable, use meaningful names, and include comments that explain important decisions or non-obvious logic.

Your program should be runnable from the terminal using Python 3.10 or newer. Use built-in Python features only; do not use external libraries, classes, file storage, or concepts beyond those covered in PY001–PY008. You do not need to force every previously learned technique into the program. Choose approaches that make sense for the work.

Use [CONCEPTS.md](CONCEPTS.md) as the boundary for the programming knowledge expected in this challenge. It lists the concepts already covered; it does not tell you which ones to use for each requirement.

## Challenge workflow

- For the first **30 minutes**, work independently. Do not use AI, solution searches, or copied code. Your own notes, previous challenges, official Python documentation, print debugging, and your debugger are allowed.
- After 30 minutes, AI or online research is allowed if you understand, adapt, and can explain anything you use. Disclose AI assistance as required.
- When finished, send **✅ Solved** in the group before the deadline; do not post your code prematurely.
- After the deadline, be prepared to explain your decisions, tests, and how you kept the inventory consistent.

The aim is not to produce the longest program. It is to build a dependable solution that another person can understand and use. 🐍
