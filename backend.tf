
terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "Cognita-Cloud"

    workspaces {
      name = "Cognita-Cloud"
    }
  }
}