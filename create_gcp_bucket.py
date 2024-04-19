from google.cloud import storage

def create_bucket(bucket_name):
    """Create a new bucket."""
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket {bucket.name} created.")

if __name__ == "__main__":
    bucket_name = "MCITCAPSTONE"
    create_bucket(bucket_name)
