from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
choice = Table('choice', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('url', VARCHAR(length=300)),
    Column('title', VARCHAR(length=300)),
    Column('year', VARCHAR(length=4)),
    Column('blogger_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['choice'].columns['blogger_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['choice'].columns['blogger_id'].create()
