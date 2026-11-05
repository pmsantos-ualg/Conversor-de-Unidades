#!/usr/bin/env python3
 
if __name__ == "__main__":
    print("Conversor de unidades")
    print("a) m -> km")
    print("b) m -> cm")
    print("c) cm -> m")
    print("d) m -> milhas")
    print("e) milhas -> m")
    print("f) l -> hl")
    print("g) hl -> l")
    print("h) m2 -> hectares")
    print("i) hectares -> m2")

    opcao = input("> ")
 
    if opcao == "a":
        m = float(input("m = "))
        print(f"{m} m = {m/1000} km")
 
    elif opcao == "b":
        m = float(input("m = "))
        print(f"{m} m = {m*100} cm")
 
    elif opcao == "c":
        cm = float(input("cm = "))
        print(f"{cm} cm = {cm/100} m")
        
    elif opcao == "d":
        m = float(input("m = "))
        print(f"{m} m = {m/1609.344} milhas")
 
    elif opcao == "e":
        milhas = float(input("milhas = "))
        print(f"{milhas} milhas = {milhas*1609.344} m")
   
    elif opcao == "f":
        litros = float(input("l = "))
        print(f"{litros} l = {litros/100} hl")
 
    elif opcao == "g":
        hl = float(input("hl = "))
        print(f"{hl} hl = {hl*100} l")
    elif opcao == "h":
        m2 = float(input("m2 = "))
        print(f"{m2} m2 = {m2/10000} hectares")
 
    elif opcao == "i":
        hectares = float(input("hectares = "))
        print(f"{hectares} hectares = {hectares*10000} m2")

 
    else:
        print("Opção inválida")
