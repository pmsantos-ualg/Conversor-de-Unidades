#!/usr/bin/env python3
 
if __name__ == "__main__":
    print("Conversor de unidades")
    print("a) m -> km")
 
    opcao = input("> ")
 
    if opcao == "a":
        m = float(input("m = "))
        print(f"{m} m = {m/1000} km")
 
    else:
        print("Opção inválida")
