from logging.config import fileConfig
from sqlalchemy import engine_from_config
import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import pool
from alembic import context
from schema import Base
# Import all models so Alembic can detect them
from schema.users import User
from schema.properties import Property
from schema.floors import Floor
from schema.units import Unit
from schema.rooms import Room
from schema.tenancies import Tenancy
from schema.inspections import Inspection
from schema.inspection_photos import InspectionPhoto
from schema.ai_analysis import AIAnalysis
from schema.issues import Issue
from schema.maintenance_requests import MaintenanceRequest
from schema.maintenance_updates import MaintenanceUpdate
from schema.service_providers import ServiceProvider
from schema.documents import Document
from schema.notifications import Notification
from schema.audit_logs import AuditLog


config = context.config
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()