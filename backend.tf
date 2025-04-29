
terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "Cognita-Cloud"

    workspaces {
      name = "Cognita-Cloud"
    }
  }
}

resource "alicloud_vpc" "example" {
  vpc_name   = "hcp-tf-test-vpc"
  cidr_block = "192.168.0.0/16"
}