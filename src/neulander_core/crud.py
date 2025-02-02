from datetime import datetime
from typing import Any

from azure.storage.blob import ContainerClient

"""Module for CRUD operations on various storage backends."""


class GenericStorage:
    def __init__(self):
        pass

    def write(self):
        pass

    def read(self):
        pass

    def delete(self):
        raise NotImplementedError

    def list(self):
        raise NotImplementedError


class AzureBlobStorage:
    def __init__(self, sas_url):
        self.sas_url = sas_url
        self.container_client = ContainerClient.from_container_url(sas_url)

    async def read(self, blob_name: str) -> bytes:
        blob_client = self.container_client.get_blob_client(blob_name)
        blob = blob_client.download_blob(timeout=60)
        blob_content = blob.readall()
        return blob_content

    async def write(self, blob_name: str, data: Any):
        now = datetime.now()
        blob_path = f"{now.year}/{now.month}/{now.day}/{blob_name}"
        response = self.container_client.upload_blob(
            name=blob_path, data=data, overwrite=True
        )
        return response
