"""Ponto de entrada da aplicação Gerenciador de Tarefas."""

from __future__ import annotations

from cli import TaskCLI
from storage import TaskStorage


def main() -> None:
    storage = TaskStorage()
    cli = TaskCLI(storage)
    cli.run()


if __name__ == "__main__":
    main()
