#!/usr/bin/env python3
 
if __name__ == "__main__":
    print("Conversor de unidades")
    print("a) m -> km")
    print("b) l -> hl")
    print("c) hl -> l")
    print("d) m2 -> hectares")
    print("e) hectares -> m2")

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
    elif opcao == "d":
        m2 = float(input("m2 = "))
        print(f"{m2} m2 = {m2/10000} hectares")
 
    elif opcao == "e":
        hectares = float(input("hectares = "))
        print(f"{hectares} hectares = {hectares*10000} m2")

 
    else:
        print("Opção inválida")
