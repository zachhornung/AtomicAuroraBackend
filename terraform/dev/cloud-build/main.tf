variable "project_id" {}

resource "google_cloudbuild_trigger" "backend-deploy-trigger" {
  location = "us-west1"
  project = "atomic-aurora"
  name = "backend-server-deploy-trigger"
  github {
    owner = "zachhornung"
    name = "AtomicAuroraBackend"
    push {
      branch = "^development$"
    }
  }
  substitutions = {
    _LOCATION = "us-west1"
    _REPOSITORY = "atomic-aurora"
    _IMAGE = "atomic-aurora-backend"
    _SERVER = "atomic-aurora-backend-server"
    _REGION = "us-west1"
  }
  filename = "deploy/cloudbuild-deploy.yaml"
}
