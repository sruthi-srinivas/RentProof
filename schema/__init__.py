from sqlalchemy.orm import declarative_base

Base = declarative_base()
SCHEMA_ORDER = (
    "users",
    "properties",
    "floors",
    "units",
    "rooms",
    "tenancies",
    "inspections",
    "inspection_photos",
    "ai_analysis",
    "issues",
    "maintenance_requests",
    "maintenance_updates",
)