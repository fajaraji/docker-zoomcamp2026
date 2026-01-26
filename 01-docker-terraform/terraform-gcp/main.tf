 terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

 # Connect to gcp using ADC (identity verification)
 provider "google" {
   project = "de-zoomcamp-2026-01"
   region  = "us-central1"
 }
 
resource "google_storage_bucket" "demo-bucket" {
  name          = "de-zoomcamp-2026-01-terrademobucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}