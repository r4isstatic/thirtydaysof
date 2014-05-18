from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
choice = Table('choice', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('url', String(length=300)),
    Column('title', String(length=300)),
    Column('year', String(length=4)),
    Column('blogger_id', Integer),
    Column('question_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['choice'].columns['blogger_id'].create()
    post_meta.tables['choice'].columns['question_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['choice'].columns['blogger_id'].drop()
    post_meta.tables['choice'].columns['question_id'].drop()
