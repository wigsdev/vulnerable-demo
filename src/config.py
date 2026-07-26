"""Configuración de la aplicación — ARCHIVO CON VULNERABILIDADES INTENCIONALES."""

import os

# VULNERABILIDAD: AWS Access Key hardcoded
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")  # AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")  # AWS_SECRET_ACCESS_KEY

# VULNERABILIDAD: Password hardcoded
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")  # DATABASE_PASSWORD
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")  # REDIS_PASSWORD

# VULNERABILIDAD: API tokens hardcoded
STRIPE_API_KEY = "sk_test_FAKE_KEY_FOR_TESTING_ONLY_0987654321"
SENDGRID_API_KEY = "SG.xxxxxxxxxxxxxxxxxxxxx.yyyyyyyyyyyyyyyyyyyyyy"

# Configuración normal
APP_NAME = "VulnerableDemo"
DEBUG = True
PORT = 8080