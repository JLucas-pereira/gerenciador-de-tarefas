"""Gerenciador de tarefas no terminal. Os dados ficam salvos em tarefas.json."""
import json
from pathlib import Path

ARQUIVO = Path(__file__).with_name("tarefas.json")


def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text(encoding="utf-8"))
    return []


def salvar(tarefas):
    ARQUIVO.write_text(
        json.dumps(tarefas, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, t in enumerate(tarefas, start=1):
        marca = "x" if t["feita"] else " "
        print(f"{i}. [{marca}] {t['titulo']}")


def escolher_numero(tarefas):
    listar(tarefas)
    if not tarefas:
        return None
    try:
        indice = int(input("Número da tarefa: ")) - 1
    except ValueError:
        print("Digite um número válido.")
        return None
    if 0 <= indice < len(tarefas):
        return indice
    print("Tarefa não encontrada.")
    return None


def main():
    tarefas = carregar()
    while True:
        print("\n1) Listar  2) Adicionar  3) Concluir  4) Remover  0) Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            listar(tarefas)
        elif opcao == "2":
            titulo = input("Título da tarefa: ").strip()
            if titulo:
                tarefas.append({"titulo": titulo, "feita": False})
                salvar(tarefas)
        elif opcao == "3":
            indice = escolher_numero(tarefas)
            if indice is not None:
                tarefas[indice]["feita"] = True
                salvar(tarefas)
        elif opcao == "4":
            indice = escolher_numero(tarefas)
            if indice is not None:
                tarefas.pop(indice)
                salvar(tarefas)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
