import os
from dataclasses import dataclass

from faststream.rabbit import RabbitQueue
from pydantic import AmqpDsn, BaseModel, computed_field


class Settings(BaseModel):
    rabbitmq_host: str = os.getenv("RABBITMQ_HOST", "localhost")
    rabbitmq_username: str = os.getenv("RABBITMQ_USERNAME", "neulander")
    rabbitmq_password: str = os.getenv("RABBITMQ_PASSWORD", "neulander")
    rabbitmq_port: int = int(os.getenv("RABBITMQ_PORT", 5672))
    fastapi_debug: bool = bool(os.getenv("FASTAPI_DEBUG", False))

    @computed_field
    @property
    def rabbitmq_connection_string(self) -> str:
        out = AmqpDsn.build(
            scheme="amqp",
            username=self.rabbitmq_username,
            password=self.rabbitmq_password,
            host=self.rabbitmq_host,
            port=self.rabbitmq_port,
        )

        return out.unicode_string()


settings = Settings()


@dataclass
class WorkerQueues:
    worker_name: str

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
