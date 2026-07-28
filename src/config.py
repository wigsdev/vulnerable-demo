"""Configuración de la aplicación — ARCHIVO CON VULNERABILIDADES INTENCIONALES."""

import os

# VULNERABILIDAD: AWS Access Key hardcoded
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")  # type: ignore
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")  # type: ignore

# VULNERABILIDAD: Password hardcoded
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")  # type: ignore
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")  # type: ignore

# VULNERABILIDAD: API tokens hardcoded
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")  # type: ignore
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")  # type: ignore

# Configuración normal
APP_NAME = "VulnerableDemo"
DEBUG = True
PORT = 8080