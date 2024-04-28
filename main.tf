resource "google_storage_bucket" "TF" {
  name          = "capstone"
  location      = "US"
  force_destroy = true

  
}
resource "google_storage_bucket_object" "picture" {
  name   = "gcplogo"
  source = "/images/nature/garden-tiger-moth.jpg"
  bucket = create_bucket_gcp.tf.name
}
