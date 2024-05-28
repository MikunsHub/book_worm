"""add user table

Revision ID: 8bc59ccbc2cd
Revises:
Create Date: 2024-05-28 06:32:05.755329

"""

from typing import Sequence, Union

from alembic import op

revision: str = "8bc59ccbc2cd"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql = """
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        email VARCHAR UNIQUE NOT NULL,
        password VARCHAR NOT NULL,
        firstname VARCHAR,
        lastname VARCHAR,
        is_active BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT now(),
        updated_at TIMESTAMP DEFAULT now()
    );
    """
    op.execute(sql)


def downgrade() -> None:
    sql = """
    DROP TABLE users;
    """
    op.execute(sql)