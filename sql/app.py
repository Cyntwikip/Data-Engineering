import streamlit as st
import pandas as pd
import psycopg2
import os

# Database connection settings (adjust as needed)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "data_eng_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

@st.cache_data
def get_table(table_name):
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
    conn.close()
    return df

st.title("PostgreSQL Data Tables Viewer")

for table in ["customers", "products", "transactions"]:
    st.header(f"{table.capitalize()} Table")
    try:
        df = get_table(table)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Could not load table '{table}': {e}")