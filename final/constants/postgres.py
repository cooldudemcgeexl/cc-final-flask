from .env import POSTGRES_PWD

POSTGRES_DB_NAME = 'cloud-comp-final'

POSTGRES_CON_STR = f'postgresql://cc_postgres_admin:{POSTGRES_PWD}@cc-final-postgres2.postgres.database.azure.com/{POSTGRES_DB_NAME}?sslmode=require'
