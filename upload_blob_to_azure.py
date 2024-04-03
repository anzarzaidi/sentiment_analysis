import os
from azure.storage.blob import BlobServiceClient

def upload_blob_file(blob_service_client: BlobServiceClient, container_name: str):
    container_client = blob_service_client.get_container_client(container=container_name)
    with open(file=os.path.join('.', 'output.csv'), mode="rb") as data:
        blob_client = container_client.upload_blob(name="sentiment_analysis.csv", data=data, overwrite=True)


if __name__ == '__main__':
    connection_string = "DefaultEndpointsProtocol=https;AccountName=storageaccountzaidi;AccountKey=VVEpa+fjbBP660rAQO0hgAselKvddFbHVPhBzzdSdz4bkfcVyYFqCLT5/j+tLjeCR8OoUWQ9NCQY+AStYCW4nQ==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    upload_blob_file(blob_service_client= blob_service_client, container_name="my-container")
