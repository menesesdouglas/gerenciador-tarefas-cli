"""Modelo de dados de uma tarefa."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

STATUS_PENDENTE = "pendente"
STATUS_CONCLUIDA = "concluída"


@dataclass
class Task:
    """Uma tarefa pessoal.

    Atributos:
        id: identificador único da tarefa.
        title: título obrigatório da tarefa.
        description: descrição opcional da tarefa.
        created_at: data/hora de criação gerada automaticamente (ISO 8601).
        status: "pendente" ou "concluída".
    """

    id: int
    title: str
    description: str = ""
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    status: str = STATUS_PENDENTE

    def mark_done(self) -> None:
        """Marca a tarefa como concluída."""
        self.status = STATUS_CONCLUIDA

    def mark_pending(self) -> None:
        """Marca a tarefa como pendente."""
        self.status = STATUS_PENDENTE

    def is_done(self) -> bool:
        """Retorna True quando a tarefa está concluída."""
        return self.status == STATUS_CONCLUIDA

    def to_dict(self) -> dict:
        """Converte a tarefa em dicionário para serialização JSON."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Recria uma Task a partir de um dicionário (desserialização JSON)."""
        return cls(**data)
