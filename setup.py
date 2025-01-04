import os

PWD = os.environ["PGPASS"]
USER_ID = "postgres.fzcllhsilkspaodlonqy"
SERVER = "aws-0-ap-southeast-1.pooler.supabase.com"
DB = "postgres"
DRIVER = "org.postgresql.Driver"

USER_ID_TARGET = "postgres.vljjmfvcwwokmuhcxxpj"
SERVER_TARGET = "aws-0-ap-southeast-1.pooler.supabase.com"

src_url = f"jdbc:postgresql://{SERVER}:5432/{DB}?user={USER_ID}&password={PWD}"

target_url = f"jdbc:postgresql://{SERVER_TARGET}:5432/{DB}?user={USER_ID_TARGET}&password={PWD}"