"""Configuración de la aplicación — ARCHIVO CON VULNERABILIDADES INTENCIONALES."""

import os

# VULNERABILIDAD: AWS Access Key hardcoded
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# VULNERABILIDAD: Password hardcoded
DATABASE_PASSWORD = "super_secret_db_password_123!"
REDIS_PASSWORD = "redis_pass_456"

# VULNERABILIDAD: API tokens hardcoded
STRIPE_API_KEY = "sk_test_FAKE_KEY_FOR_TESTING_ONLY_0987654321"
SENDGRID_API_KEY = "SG.xxxxxxxxxxxxxxxxxxxxx.yyyyyyyyyyyyyyyyyyyyyy"

# Configuración normal
APP_NAME = "VulnerableDemo"
DEBUG = True
PORT = 8080
