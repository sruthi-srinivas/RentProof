# RentProof Database

## Overview

RentProof uses PostgreSQL as the database, SQLAlchemy as the ORM,
and Alembic for database migrations.

The database stores users, properties, tenancies, inspections,
AI analysis, issues, maintenance requests, documents,
notifications, and audit logs.

---

## Database Technology

- Database: PostgreSQL
- ORM: SQLAlchemy
- Migration Tool: Alembic
- Database Provider: Supabase PostgreSQL

---

## Database Tables

The RentProof database contains the following tables:

1. users
2. properties
3. floors
4. units
5. rooms
6. tenancies
7. inspections
8. inspection_photos
9. ai_analysis
10. issues
11. maintenance_requests
12. maintenance_updates
13. service_providers
14. documents
15. notifications
16. audit_logs

---

## Main Database Relationship

The main RentProof database flow is:

User
  ↓
Property
  ↓
Floor
  ↓
Unit
  ↓
Room
  ↓
Tenancy
  ↓
Inspection
  ↓
Inspection Photo
  ↓
AI Analysis
  ↓
Issue
  ↓
Maintenance Request
  ↓
Maintenance Update

Additional user-related tables:

User
  ├── Documents
  ├── Notifications
  └── Audit Logs

Service Providers is an independent table in the current implementation.

---

## Project Structure

```text
RENTPROOF/
│
├── schema/
│   ├── __init__.py
│   ├── users.py
│   ├── properties.py
│   ├── floors.py
│   ├── units.py
│   ├── rooms.py
│   ├── tenancies.py
│   ├── inspections.py
│   ├── inspection_photos.py
│   ├── ai_analysis.py
│   ├── issues.py
│   ├── maintenance_requests.py
│   ├── maintenance_updates.py
│   ├── service_providers.py
│   ├── documents.py
│   ├── notifications.py
│   └── audit_logs.py
│
├── migrations/
├── erd/
│   └── rentproof_erd.png
│
├── queries/
├── seed/
├── database/
├── README.md
├── .env
└── alembic.ini