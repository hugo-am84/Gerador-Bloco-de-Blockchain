import json
import hashlib
import os
from datetime import datetime

ARQUIVO_BLOCOS = "blocos.json"

def carregar_blocos():
    if os.path.exists(ARQUIVO_BLOCOS):
        with open(ARQUIVO_BLOCOS, "r") as f:
            return json.load(f)
    return []

def salvar_blocos(blocos):
    with open(ARQUIVO_BLOCOS, "w") as f:
        json.dump(blocos, f, indent=4)

def gerar_hash(dados):
    conteudo = f"{dados['numero']}{dados['data']}{dados['conteudo']}{dados['prev']}"
    hash_base = hashlib.sha256(conteudo.encode()).hexdigest()
    hash_final = ("0" * dados["dificuldade"]) + hash_base
    return hash_final

def gerar_bloco(blocos):
    os.system("clear" if os.name == "posix" else "cls")
    print("=" * 80)
    print("GERADOR DE BLOCOS FICTÍCIOS".center(80))
    print("=" * 80)

    while True:
        try:
            dificuldade = int(input("Nível de dificuldade (1 a 20): "))
            if 1 <= dificuldade <= 20:
                break
            else:
                print("Digite um número entre 1 e 20.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    conteudo = input("Conteúdo do bloco: ")

    numero_bloco = len(blocos) + 1
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prev_hash = blocos[-1]["hash"] if blocos else "0" * 64

    bloco = {
        "numero": numero_bloco,
        "data": data_criacao,
        "conteudo": conteudo,
        "prev": prev_hash,
        "nonce": None,
        "dificuldade": dificuldade
    }

    bloco["hash"] = gerar_hash(bloco)

    print("\n" + "-" * 80)
    print(f"🧱  Bloco #{bloco['numero']} gerado com sucesso!")
    print("-" * 80)
    print(f"Data:           {bloco['data']}")
    print(f"Conteúdo:       {bloco['conteudo']}")
    print(f"Hash Anterior:  {bloco['prev']}")
    print(f"Hash Final:     {bloco['hash']}")
    print(f"Nonce:          {bloco['nonce']}")
    print("-" * 80)

    blocos.append(bloco)
    salvar_blocos(blocos)

def main():
    blocos = carregar_blocos()
    while True:
        gerar_bloco(blocos)
        opcao = input("\nDeseja gerar outro bloco? (s/n): ").strip().lower()
        if opcao != "s":
            print("\nEncerrando...\n")
            break

if __name__ == "__main__":
    main()
