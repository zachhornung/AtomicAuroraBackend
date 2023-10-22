terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.83.0"
    }
  }
}

provider "google" {
  # Configuration options
  project = "atomic-aurora"
}

module "artifact-registry" {
  source = "./artifact-registry"
  project_id = var.project_id
}

module "cloud-build" {
  source = "./cloud-build"
  project_id = var.project_id
}

module "cloud-run" {
  source = "./cloud-run"
  project_id = var.project_id
}

module "cloud-storage" {
  source = "./cloud-storage"
  project_id = var.project_id
  backend_gcs_bucket_name = var.backend_gcs_bucket_name
}
