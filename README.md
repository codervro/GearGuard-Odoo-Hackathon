# GearGuard – Smart Equipment Maintenance Tracker

## Problem Understanding
In many organizations, equipment breakdowns are handled manually or through
unstructured communication, which leads to delayed repairs, unclear ownership,
and lack of visibility into maintenance status.

The goal of GearGuard is to bring structure to this process by providing a
simple and centralized way to track equipment and their maintenance lifecycle.

---

## Our Approach
Instead of trying to implement every advanced feature in limited time, we focused
on building a **stable core system** that represents how maintenance actually works
in real organizations.

Our solution is designed around three core concepts:
- Equipment
- Maintenance Requests
- Repair Status Workflow

This ensures clarity, usability, and scope control within the hackathon timeframe.

---

## Key Features Implemented

### 1. Equipment Management
- Create and store basic equipment details
- Link equipment with maintenance activities

### 2. Maintenance Requests
- Raise a maintenance request for a specific equipment
- Assign a technician to handle the issue


This helps track the current state of repairs at any point in time.

---

## Technical Implementation
- Backend logic is implemented using **Python (Odoo ORM)**
- User interface is built using **XML views**
- Modular structure is followed as per Odoo standards

The project is structured to be easily extendable in future phases.

---

## What We Prioritized
- Correct Odoo module structure
- Clear data relationships
- Working core functionality
- Readable and maintainable code

We intentionally avoided overengineering to ensure stability and correctness.

---

## Future Enhancements
If extended further, this system can support:
- Preventive maintenance scheduling
- Calendar and reporting views
- Maintenance history analytics
- Spare parts tracking

---

## Team
- **Team Leader:** Vala Nirav  
- **Team Member:** Shruti  

---

## Hackathon Note
This project was built as part of the **Odoo x Adani University Hackathon – Phase 1**,
with a focus on problem understanding, clean implementation, and practical design.

### 3. Request Lifecycle Tracking
Each maintenance request follows a clear workflow:

New → In Progress → Repaired
