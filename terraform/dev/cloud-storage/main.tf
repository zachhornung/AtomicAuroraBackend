variable "project_id" {}
variable "backend_gcs_bucket_name" {}

resource "google_storage_bucket" "django" {
  name = var.backend_gcs_bucket_name
  location = "us-west1"
}
