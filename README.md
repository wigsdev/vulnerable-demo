# Vulnerable Demo App

> Este repositorio contiene vulnerabilidades **intencionadas** para testing de herramientas de auditoría de seguridad.

**NO usar en producción.**

## Propósito

Repositorio de prueba para validar el Auditor 3D y Auto-Fix Engine de [OmniSpec AI](https://github.com/wigsdev/omnispec-ai).

## Vulnerabilidades Incluidas

- Secretos hardcoded (AWS keys, passwords, JWT tokens)
- Claves privadas PEM expuestas
- Políticas IAM con `Action: "*"` y `Resource: "*"`
- Security Groups abiertos a `0.0.0.0/0` en puertos sensibles
- Tags de gobierno faltantes
- Sin estructura de tests
