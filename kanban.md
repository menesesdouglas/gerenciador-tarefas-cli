# Kanban - Gerenciador de Tarefas Local (CLI)

## Projeto
- **Nome**: Gerenciador de Tarefas Local (CLI)
- **Nível**: Júnior I
- **Stack**: Python 3.11+, JSON (armazenamento local), pathlib, pytest
- **Módulos**: main.py, models.py, storage.py, cli.py
- **Objetivo**: aplicação de console para gerenciar tarefas pessoais com persistência em JSON

## Legenda de status
- `[ ]` To Do / Pendente
- `[x]` Done / Concluído

---

## Sprint 1 - Estrutura base e persistência de dados
**Objetivo**: configurar o projeto, definir o modelo de dados e implementar a camada de armazenamento em JSON.

| # | Task | Módulo | Status |
|---|------|--------|--------|
| 1.1 | Criar estrutura de pastas do projeto e ambiente virtual (Python 3.11+) | — | [x] |
| 1.2 | Implementar models.py: estrutura da tarefa (id, título, descrição opcional, data de criação automática, status pendente/concluída) | models.py | [x] |
| 1.3 | Implementar storage.py: leitura e gravação de tarefas em arquivo JSON com pathlib | storage.py | [x] |
| 1.4 | Implementar persistência automática (salvar JSON a cada alteração de estado CRUD) | storage.py | [ ] |
| 1.5 | Testes unitários com pytest para models.py e storage.py | tests/ | [ ] |

---

## Sprint 2 - Interface de linha de comando e CRUD
**Objetivo**: construir a CLI interativa e as operações de criar, listar, concluir e excluir tarefas.

| # | Task | Módulo | Status |
|---|------|--------|--------|
| 2.1 | Implementar cli.py: menu interativo e validação de entrada do usuário | cli.py | [ ] |
| 2.2 | Implementar main.py: ponto de entrada da aplicação e loop de interação | main.py | [ ] |
| 2.3 | Implementar funcionalidade de criar nova tarefa (título, descrição opcional) | cli.py / models.py | [ ] |
| 2.4 | Implementar listagem de todas as tarefas exibindo status (pendente/concluída) | cli.py | [ ] |
| 2.5 | Implementar marcar tarefa específica como concluída pelo identificador | cli.py | [ ] |
| 2.6 | Implementar excluir tarefa pelo identificador | cli.py | [ ] |
| 2.7 | Tratamento de erros: tarefa inexistente, entradas inválidas, JSON ausente ou corrompido | cli.py / storage.py | [ ] |
| 2.8 | Testes unitários com pytest para cli.py e fluxos de CRUD | tests/ | [ ] |

---

## Sprint 3 - Refinamento, testes e entrega
**Objetivo**: validar o fluxo completo, corrigir bugs e entregar o projeto documentado.

| # | Task | Módulo | Status |
|---|------|--------|--------|
| 3.1 | Revisão de código e boas práticas (PEP 8, estrutura modular) | Todos | [ ] |
| 3.2 | Testes de integração: fluxo completo (criar → listar → concluir → excluir) | tests/ | [ ] |
| 3.3 | Correção de bugs encontrados nos testes | Todos | [ ] |
| 3.4 | Escrever README.md com instruções de instalação e uso | — | [ ] |
| 3.5 | Execução final de todos os testes e validação da entrega | — | [ ] |

---

## Backlog / Evoluções futuras (fora do escopo do MVP)
- Adicionar categorias e prioridades às tarefas
- Exportar a lista de tarefas para CSV
- Adicionar data de vencimento e filtro por tarefas vencidas

---

## Critérios de aceitação (Definition of Done)
- A aplicação roda com Python 3.11+ sem dependências externas (apenas stdlib: `json`, `pathlib`)
- Os dados persistem em arquivo JSON e sobrevivem ao encerramento do programa
- É possível criar, listar, marcar como concluída e excluir tarefas
- Entradas inválidas e tarefas inexistentes são tratadas com mensagens de erro
- Testes unitários com pytest passam (cobertura de models, storage e cli)
