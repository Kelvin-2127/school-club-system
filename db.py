# db.py
import psycopg2

DATABASE_URL = "postgresql://neondb_owner:npg_mY6C7dtGLoqc@ep-jolly-shadow-agrl63em-pooler.c-2.eu-central-1.aws.neon.tech/school-club-system?sslmode=require&channel_binding=require"

def get_connection():
    return psycopg2.connect(DATABASE_URL)

