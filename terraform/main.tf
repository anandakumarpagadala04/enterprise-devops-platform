resource "aws_ecr_repository" "transaction_service_tf" {
  name                 = "transaction-service-tf"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
