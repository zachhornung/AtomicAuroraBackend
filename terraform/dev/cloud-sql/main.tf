variable "project_id" {}

resource "google_sql_database_instance" "atomic-aurora-db" {
  name              = "atomic-aurura-db"
  database_version  = "POSTGRES_15"
  region            = "us-west1"

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "database" {
  name     = "atomic-aurora-db"
  instance = google_sql_database_instance.atomic-aurora-db.name
}
