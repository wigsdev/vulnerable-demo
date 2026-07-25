# Terraform config — INSEGURO para testing de auditoría

provider "aws" {
  region = "us-east-1"
}

# VULNERABILIDAD: Security Group completamente abierto
resource "aws_security_group" "open_all" {
  name        = "open-to-world"
  description = "INSEGURO - Todo abierto"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# VULNERABILIDAD: IAM policy con acceso total
resource "aws_iam_policy" "admin_access" {
  name        = "full-admin-access"
  description = "INSEGURO - Acceso total"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "*"
        Resource = "*"
      }
    ]
  })
}

# VULNERABILIDAD: Bucket S3 sin encryption
resource "aws_s3_bucket" "data" {
  bucket = "vulnerable-data-bucket"
  acl    = "public-read"
}
