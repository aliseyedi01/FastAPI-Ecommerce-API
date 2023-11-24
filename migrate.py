# migrate.py
from alembic.config import Config
from alembic import command

alembic_cfg = Config("alembic.ini")  # adjust if alembic.ini is in a different location
command.upgrade(alembic_cfg, "head")
