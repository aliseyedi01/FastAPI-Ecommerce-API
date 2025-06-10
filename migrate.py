# migrate.py
import os
from alembic.config import Config
from alembic import command
from alembic.script import ScriptDirectory

def run_migrations():
    # Load Alembic configuration
    alembic_cfg = Config("alembic.ini")
    
    # Get the script directory (where migration files are stored)
    script = ScriptDirectory.from_config(alembic_cfg)
    
    # Check if any migration files exist
    versions_dir = script.versions
    migration_files = [f for f in os.listdir(versions_dir) if f.endswith('.py') and f != '__pycache__']
    
    print(f"Checking migrations in: {versions_dir}")
    print(f"Found {len(migration_files)} migration files")
    
    # If no migration files exist, create initial migration
    if not migration_files:
        print("No migration files found. Creating initial migration...")
        try:
            command.revision(alembic_cfg, autogenerate=True, message="Create initial tables")
            print("✓ Initial migration created successfully")
        except Exception as e:
            print(f"✗ Error creating initial migration: {e}")
            return False
    else:
        print("Migration files already exist:")
        for file in migration_files:
            print(f"  - {file}")
    
    # Run all pending migrations
    print("Running migrations...")
    try:
        command.upgrade(alembic_cfg, "head")
        print("✓ All migrations completed successfully")
        return True
    except Exception as e:
        print(f"✗ Error running migrations: {e}")
        return False

if __name__ == "__main__":
    print("=== Database Migration Script ===")
    success = run_migrations()
    if success:
        print("=== Migration process completed ===")
    else:
        print("=== Migration process failed ===")
        exit(1)