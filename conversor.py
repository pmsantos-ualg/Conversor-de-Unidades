#!/usr/bin/env python3
 
if __name__ == "__main__":
    print("Conversor de unidades")
    print("a) m -> km")
    print("b) l -> hl")
    print("c) hl -> l")
    
    opcao = input("> ")
 
    if opcao == "a":
        m = float(input("m = "))
        print(f"{m} m = {m/1000} km")

    elif opcao == "b":
        litros = float(input("l = "))
        print(f"{litros} l = {litros/100} hl")
 
    elif opcao == "c":
        hl = float(input("hl = "))
        print(f"{hl} hl = {hl*100} l")

 
    else:
        print("Opção inválida")
