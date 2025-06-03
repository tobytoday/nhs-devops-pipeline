variable "region" {
  default = "us-east-1"
}
variable "cluster_name" {
  default = "nhs-eks-cluster"
}
variable "node_instance_type" {
  default = "t3.medium"
}
variable "desired_capacity" {
  default = 2
}

