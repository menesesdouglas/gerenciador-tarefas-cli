"""Camada de armazenamento: leitura e gravação de tarefas em JSON via pathlib."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from models import Task, STATUS_PENDENTE


class TaskNotFoundError(Exception):
    """Erro ao tentar acessar uma tarefa que não existe."""


class TaskStorage:
    """Gerencia o CRUD de tarefas com persistência automática em JSON.

    Cada operação que altera o estado (criar, concluir, excluir) grava o
    arquivo JSON imediatamente, garantindo que os dados sobrevivam ao
    encerramento do programa.
    """

    def __init__(self, filepath: str | Path | None = None) -> None:
        if filepath is None:
            filepath = Path(__file__).resolve().parent / "data" / "tarefas.json"
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self._tasks: dict[int, Task] = {}
        self._load()

    def _load(self) -> None:
        """Carrega as tarefas do arquivo JSON. Arquivo ausente/corrompido -> vazio."""
        if not self.filepath.exists():
            self._tasks = {}
            return
        try:
            with self.filepath.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            # Arquivo ausente ou corrompido: inicia com lista vazia.
            self._tasks = {}
            return
        if not isinstance(data, list):
            self._tasks = {}
            return
        self._tasks = {item["id"]: Task.from_dict(item) for item in data if "id" in item}

    def _save(self) -> None:
        """Grava as tarefas no arquivo JSON de forma atômica."""
        payload = [task.to_dict() for task in self._tasks.values()]
        tmp = self.filepath.with_suffix(self.filepath.suffix + ".tmp")
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        tmp.replace(self.filepath)

    def _next_id(self) -> int:
        return max(self._tasks.keys(), default=0) + 1

    def list_tasks(self) -> list[Task]:
        """Retorna todas as tarefas ordenadas pelo identificador."""
        return sorted(self._tasks.values(), key=lambda task: task.id)

    def get_task(self, task_id: int) -> Task:
        """Retorna a tarefa pelo id ou levanta TaskNotFoundError."""
        try:
            return self._tasks[task_id]
        except KeyError:
            raise TaskNotFoundError(f"Tarefa com id {task_id} não encontrada.") from None

    def add_task(self, title: str, description: str = "") -> Task:
        """Cria uma nova tarefa, persiste e retorna a tarefa criada."""
        task = Task(id=self._next_id(), title=title, description=description)
        self._tasks[task.id] = task
        self._save()
        return task

    def mark_done(self, task_id: int) -> Task:
        """Marca uma tarefa existente como concluída."""
        task = self.get_task(task_id)
        task.mark_done()
        self._save()
        return task

    def delete_task(self, task_id: int) -> Task:
        """Exclui uma tarefa existente e retorna a tarefa excluída."""
        task = self.get_task(task_id)
        del self._tasks[task_id]
        self._save()
        return task
