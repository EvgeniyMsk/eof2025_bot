from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

raffle_users = Table(
    'raffle_users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('telegram_id', String),
    Column('last_name', String),
    Column('ticket_number', String),
)
