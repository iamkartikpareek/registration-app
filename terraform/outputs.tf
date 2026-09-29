output "vpc_id" {
  description = "ID of the registration VPC"
  value       = module.vpc.vpc_id
}

output "vpc_cidr" {
  description = "CIDR of the registration VPC"
  value       = module.vpc.vpc_cidr
}

output "security_group_id" {
  description = "Application security group ID"
  value       = module.security_group.security_group_id
}

output "ecr_repository_url" {
  description = "URL of the application ECR repository"
  value       = module.ecr.repository_url
}