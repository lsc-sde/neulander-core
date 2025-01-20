import os
from dataclasses import dataclass

from dotenv import find_dotenv, load_dotenv

# from pydantic import BaseModel, computed_field
from faststream.rabbit import RabbitQueue
from pydantic import AmqpDsn, BaseModel, computed_field

load_dotenv(find_dotenv("dev.env"))


class Settings(BaseModel):
    rabbitmq_host: str = os.getenv("RABBITMQ_HOST", "localhost")
    rabbitmq_username: str = os.getenv("RABBITMQ_USERNAME", "neulander")
    rabbitmq_password: str = os.getenv("RABBITMQ_PASSWORD", "neulander")
    rabbitmq_port: int = os.getenv("RABBITMQ_PORT", default="5672")

    fastapi_debug: bool = os.getenv("FASTAPI_DEBUG", False)

    @computed_field
    @property
    def rabbitmq_connection_string(self) -> AmqpDsn:
        return f"amqp://{self.rabbitmq_username}:{self.rabbitmq_password}@{self.rabbitmq_host}:{self.rabbitmq_port}"


settings = Settings()


@dataclass
class WorkerQueues:
    worker_name: str

    # @computed_field
    @property
    def qin(self) -> RabbitQueue:
        return RabbitQueue(
            f"q-{self.worker_name}-in",
            durable=True,
        )

    @property
    def qout(self) -> RabbitQueue:
        return RabbitQueue(f"q-{self.worker_name}-out", durable=True)

    @property
    def qerr(self) -> RabbitQueue:
        return RabbitQueue(f"q-{self.worker_name}-err", durable=True)
