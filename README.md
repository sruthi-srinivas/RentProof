# RENTPROOF 

## AI-Assisted Rental Inspection & Maintenance Platform

RentProof is a web-based rental property documentation and maintenance platform designed to maintain a centralized digital record of a property's condition throughout the tenancy.

The system records property inspections, photographs, identified issues, maintenance requests, repair updates, and historical records in one place. Vision AI is used to analyze property photographs and identify possible visible issues, while users can review and confirm the AI-generated findings.

---

## Problem Statement

When tenants move into a rented property, there is often no centralized and time-stamped record of the property's condition, existing damages, reported issues, or maintenance activities.

Evidence such as photos, videos, complaints, and repair details may be scattered across phones, WhatsApp chats, and paper records.

This can create disputes between tenants and landlords regarding:

- Whether a particular damage already existed
- When the damage occurred
- When an issue was reported
- Who was responsible for resolving the issue
- Whether the repair was completed

RentProof aims to solve this problem by maintaining a structured and verifiable digital history of the rental property.

---

##  Proposed Solution

RentProof connects the complete rental property inspection and maintenance process in one platform.

### Main Workflow

Property / Room
↓
Inspection
↓
Upload Photos & Record Observations
↓
Image Processing
↓
Vision AI Analysis
↓
Issue Detection & Categorization
↓
Condition Report
↓
Maintenance Request
↓
Assignment & Scheduling
↓
Repair Updates
↓
Completed / Closed
↓
Permanent Property Maintenance History

---

## Key Features

### Property Management
- Add and manage rental properties
- Maintain room-level information
- Connect tenants with properties

###  Property Inspection
- Create inspection records
- Record property and room conditions
- Upload inspection photographs
- Maintain inspection history

### Photo & Evidence Management
- Upload property photographs
- Validate and process images
- Store original images securely
- Generate thumbnails for faster viewing

### AI-Based Issue Detection
- Analyze property photographs using Vision AI
- Identify possible visible property conditions
- Categorize potential issues
- Allow users to review and confirm AI findings

###  Maintenance Management
- Create maintenance requests
- Assign maintenance work
- Schedule repairs
- Track repair progress
- Close completed maintenance requests

### Notifications
- Provide notifications for relevant system activities
- Support maintenance and repair updates

### Audit History
- Record important system activities
- Maintain timestamps for important actions
- Preserve the property's maintenance history

---

##  User Roles

RentProof supports role-based access for different users:

- **Tenant**
- **Landlord**
- **Property Manager**
- **Administrator**
- **Service Worker**

Role-Based Access Control (RBAC) is used to manage permissions for different users.

---

##  Technology Stack

| Technology | Purpose |
|------------|---------|
| React.js | Frontend / Web Application |
| Python + FastAPI | Backend / REST API |
| PostgreSQL | Database |
| Vision AI + LLM API | AI analysis and natural-language features |
| OpenCV / Pillow | Image processing |
| AWS S3 / Supabase Storage | Image and file storage |
| Celery + Redis | Background and asynchronous processing |
| JWT + RBAC | Authentication and role-based access control |
| Docker | Deployment and reproducible environments |

---

## System Architecture

```text
                    React.js Web Application
                              │
                              ↓
                     HTTPS / REST API
                              │
                              ↓
                  FastAPI Backend
                  Authentication
                         + RBAC
                              │
                              ↓
                  Application Services
                  ┌───────────┼───────────┐
                  ↓           ↓           ↓
             Inspection   Maintenance   AI/Search
               Service      Service    Orchestrator
                  │           │           │
                  └───────────┼───────────┘
                              ↓
                       PostgreSQL
                              │
                              ↓
                    Object Storage
                 AWS S3 / Supabase
                              │
                              ↓
                      Celery + Redis
                              │
                              ↓
                    Vision AI / LLM API
