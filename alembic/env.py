from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from app.core.config import settings
from app.db.database import Base

# IMPORT ALL MODELS - This is crucial for Alembic to detect them
from app.models.models import User, Cart, CartItem, Category, Product

config = context.config

config.set_main_option(
    "sqlalchemy.url",  f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}")

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

# Debug: Print detected tables
print("=== TARGET METADATA DEBUG ===")
print(f"Tables to create: {list(target_metadata.tables.keys())}")
print("================================")

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
    print("=== STARTING MIGRATIONS ===")
    
    # Debug: Print the connection URL (hide password)
    url = config.get_main_option("sqlalchemy.url")
    print(f"Database URL: {url.replace(':' + settings.db_password, ':****')}")
    
    try:
        connectable = engine_from_config(
            config.get_section(config.config_ini_section, {}),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )
        print("Database engine created successfully")

        with connectable.connect() as connection:
            print("Database connection established")
            
            context.configure(
                connection=connection, target_metadata=target_metadata
            )

            with context.begin_transaction():
                print("Running migrations...")
                context.run_migrations()
                print("Migrations completed")
                
    except Exception as e:
        print(f"Migration error: {e}")
        import traceback
        traceback.print_exc()
        raise

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()