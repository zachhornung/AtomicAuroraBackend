resource "google_vpc_access_connector" "connector" {
  name          = "atomic-aurora-vpc-connector"
  network       = "default"
  region        = "us-west1"
  ip_cidr_range = "10.8.0.0/28"
}
