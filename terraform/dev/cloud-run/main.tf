variable "project_id" {}

resource "google_secret_manager_secret" "django_backend_secrets" {
  secret_id = "django-backend-secrets"
  project = var.project_id
  labels = {
    label = "django-backend-secrets"
  }
  replication {
    user_managed {
      replicas {
        location = "us-west1"
      }
    }
  }
}

resource "google_cloud_run_v2_service" "atomic_aurora_backend_server" {
  name = "atomic-aurora-backend-server"
  location = "us-west1"
  project = var.project_id
  template {
    volumes {
      name = "secrets-volume"
      secret {
        secret = google_secret_manager_secret.django_backend_secrets.secret_id
        items {
          path = ".env"
          mode = 0
          version = "latest"
        }
      }
    }
    vpc_access {
      connector = "atomic-aurora-vpc-connector"
      egress = "ALL_TRAFFIC"
    }
    containers {
      ports {
        container_port = 8000
    }
      image = "us-west1-docker.pkg.dev/atomic-aurora-dev/atomic-aurora/atomic-aurora-backend"
      volume_mounts {
        name = "secrets-volume"
        mount_path = "/secrets"
      }
    }
  }
}

resource "google_secret_manager_secret" "atomic_aurora_service_secrets" {
  secret_id = "atomic-aurora-service-secrets"
  project = var.project_id
  labels = {
    label = "atomic-aurora-service-secrets"
  }
  replication {
    user_managed {
      replicas {
        location = "us-west1"
      }
    }
  }
}
