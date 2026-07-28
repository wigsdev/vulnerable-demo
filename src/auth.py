"""Módulo de autenticación — CONTIENE TOKENS EXPUESTOS."""

import os
import jwt

# VULNERABILIDAD: JWT token hardcoded
# ADMIN_TOKEN = "..."
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

# VULNERABILIDAD: Secret key para JWT signing
JWT_SECRET = os.getenv("JWT_SECRET")

def authenticate(username, password):
    """Autentica un usuario — sin hashing de password."""
    # VULNERABILIDAD: Comparación directa de password sin hash
    if password == "admin123":
        return {"token": ADMIN_TOKEN, "role": "admin"}
    return None

def verify_token(token):
    """Verifica un JWT token."""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.InvalidTokenError:
        return None