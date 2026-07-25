"""Conexión a base de datos — CREDENCIALES EXPUESTAS."""

import os

# VULNERABILIDAD: Connection string con password visible
DATABASE_URL = "postgresql://admin:P@ssw0rd_Pr0d!@db.production.internal:5432/maindb"

# VULNERABILIDAD: Password de backup
BACKUP_DB_PASSWORD = "backup_readonly_2024!"

def get_connection():
    """Obtiene conexión a la base de datos."""
    import psycopg2
    return psycopg2.connect(DATABASE_URL)

def run_query(query, params=None):
    """Ejecuta una query — VULNERABLE A SQL INJECTION."""
    conn = get_connection()
    cursor = conn.cursor()
    # VULNERABILIDAD: String formatting en vez de parameterized queries
    if params:
        cursor.execute(query % params)
    else:
        cursor.execute(query)
    return cursor.fetchall()
