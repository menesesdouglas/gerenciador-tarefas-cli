"""Interface de linha de comando: menus, validação de entrada e fluxo de CRUD."""

from __future__ import annotations

from typing import Optional

from storage import TaskStorage, TaskNotFoundError


class TaskCLI:
    """Menu interativo de gerenciamento de tarefas."""

    MENU = (
        "\n=== Gerenciador de Tarefas ===\n"
        "1. Listar tarefas\n"
        "2. Criar tarefa\n"
        "3. Marcar tarefa como concluída\n"
        "4. Excluir tarefa\n"
        "5. Sair\n"
        "Escolha uma opção: "
    )

    def __init__(self, storage: TaskStorage) -> None:
        self.storage = storage

    def run(self) -> None:
        """Executa o loop principal da CLI até o usuário escolher sair."""
        while True:
            try:
                option = input(self.MENU).strip()
            except (EOFError, KeyboardInterrupt):
                print("\nEncerrando aplicação...")
                break

            if option == "1":
                self._list_tasks()
            elif option == "2":
                self._create_task()
            elif option == "3":
                self._mark_done()
            elif option == "4":
                self._delete_task()
            elif option == "5":
                print("Encerrando aplicação...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def _list_tasks(self) -> None:
        tasks = self.storage.list_tasks()
        if not tasks:
            print("Nenhuma tarefa cadastrada.")
            return

        print("\n--- Tarefas ---")
        for task in tasks:
            marker = "✓" if task.is_done() else " "
            print(f"[{task.id}] [{marker}] {task.title}")
            if task.description:
                print(f"      Descrição: {task.description}")
            print(f"      Criado em: {task.created_at} | Status: {task.status}")

    def _read_int(self, prompt: str) -> Optional[int]:
        value = input(prompt).strip()
        if not value:
            return None
        try:
            return int(value)
        except ValueError:
            print("Entrada inválida: informe um número inteiro.")
            return None

    def _create_task(self) -> None:
        title = input("Título da tarefa: ").strip()
        if not title:
            print("Erro: o título é obrigatório.")
            return
        description = input("Descrição (opcional): ").strip()
        task = self.storage.add_task(title=title, description=description)
        print(f"Tarefa criada com id {task.id}.")

    def _mark_done(self) -> None:
        task_id = self._read_int("Id da tarefa para concluir: ")
        if task_id is None:
            return
        try:
            self.storage.mark_done(task_id)
            print(f"Tarefa {task_id} marcada como concluída.")
        except TaskNotFoundError as exc:
            print(f"Erro: {exc}")

    def _delete_task(self) -> None:
        task_id = self._read_int("Id da tarefa para excluir: ")
        if task_id is None:
            return
        try:
            self.storage.delete_task(task_id)
            print(f"Tarefa {task_id} excluída.")
        except TaskNotFoundError as exc:
            print(f"Erro: {exc}")
