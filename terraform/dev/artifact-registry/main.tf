variable "project_id" {}

resource "google_artifact_registry_repository" "atomic-aurora" {
  location      = "us-west1"
  repository_id = "atomic-aurora"
  description   = "Atomic Aurora website image repository"
  format        = "DOCKER"
  project       = "atomic-aurora"
}
