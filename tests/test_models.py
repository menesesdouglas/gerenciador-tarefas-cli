"""Testes unitários para models.py."""

from models import Task, STATUS_PENDENTE, STATUS_CONCLUIDA


def test_task_default_status_is_pending():
    task = Task(id=1, title="Tarefa de teste")
    assert task.status == STATUS_PENDENTE


def test_task_mark_done():
    task = Task(id=1, title="Tarefa de teste")
    task.mark_done()
    assert task.is_done()
    assert task.status == STATUS_CONCLUIDA


def test_task_to_dict_roundtrip():
    original = Task(id=1, title="Título", description="Descrição")
    data = original.to_dict()
    restored = Task.from_dict(data)
    assert restored == original
