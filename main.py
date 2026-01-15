import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.empresa import Empresa
from ui.menu import menu_principal

def iniciar_sistema():
    try:
        print("--- SISTEMA MRP (Eng. Computação IFCE) ---")

        nome_empresa = input("Digite o nome da empresa: ").strip() 

        if not nome_empresa:
            nome_empresa = "Empresa Padrão"

        empresa = Empresa(nome_empresa) 

        menu_principal(empresa)

        print("\nPrograma encerrado com sucesso.")

    except KeyboardInterrupt:
        print("\n\nSaindo... (Interrompido pelo usuário)")
    except Exception as e:
        print(f"\nErro fatal no sistema: {e}")
        print("O sistema será encerrado.")

if __name__ == "__main__":
    iniciar_sistema()
