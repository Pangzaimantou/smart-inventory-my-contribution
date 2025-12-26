# Smart Inventory (Python CLI) — My Contribution Excerpt

This repository contains **only my personal contribution** in a 3-person team project.  
It is **not** the full team codebase.

## Context: What the Full Project Does
A Python command-line tool that simulates inventory management tasks:
- Load and save inventory (file-based)
- View product list and reports (summary / low stock)
- Search by ID, name, or category
- Add/edit/remove products, sell/restock — with input validation

## My Contribution
- **Menu Input Validation**  
  Standardized menu choices to accept only numeric input and validated ranges before executing actions.  
  This prevents invalid input from reaching the program logic and keeps the workflow predictable.

- **Search Enhancement**  
  Expanded search to support ID, name, and category (including partial matches), with clearer prompts and feedback.

- **Testing & Evidence**  
  Ran edge-case tests (invalid menu choice, insufficient stock, no results) and documented outputs in the test log and screenshots.

## Evidence Included
- `my_changes.diff` — patch showing exactly what I changed

## Notes
Shared for portfolio purposes to demonstrate my work on input validation, search usability, and test documentation.
