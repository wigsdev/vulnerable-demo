"""Módulo de autenticación — CONTIENE TOKENS EXPUESTOS."""

import jwt

# VULNERABILIDAD: JWT token hardcoded
ADMIN_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"

# VULNERABILIDAD: Secret key para JWT signing
JWT_SECRET = "my-super-secret-key-never-share-this"

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
