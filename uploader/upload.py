import os
from minio import Minio

MINIO_ENDPOINT = "minio:9000"
MINIO_USER = "GUTS"
MINIO_PASSWORD = "B3RS39KiN6T1ME"
BUCKET_NAME = "mybucket"
SIZE_KB = 1024

client = Minio(
    endpoint=MINIO_ENDPOINT,
    access_key=MINIO_USER,  
    secret_key= MINIO_PASSWORD,
    secure=False
)

if not client.bucket_exists(BUCKET_NAME):
    client.make_bucket(BUCKET_NAME)

def generate_data(size_kb):
    return os.urandom(size_kb * 1024)

def upload_data(filename, data):
    try:
        with open(filename, 'wb') as f:
            f.write(data)
        client.fput_object(
            bucket_name=BUCKET_NAME, 
            object_name=filename, 
            file_path=filename,
            content_type='application/octet-stream'
        )
        os.remove(filename)
        print(f"Successfully uploaded {filename}")
        return True
    except Exception as e:
        print(f"Error uploading {filename}: {e}")
        return False

def main():
    file_index = 0
    err_index = 0
    while err_index < 3:
        file_index += 1
        filename = f"file_{file_index}.txt"
        data = generate_data(SIZE_KB)
        if not upload_data(filename, data):
            err_index += 1

if __name__ == "__main__":
    main()
