#!/usr/bin/env python3
 
if __name__ == "__main__":
    print("Conversor de unidades")
    print("a) m -> km")
    print("b) m -> cm")
    print("c) cm -> m")
    print("d) m -> milhas")
    print("e) milhas -> m")
     
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
        print(f"{m} m = {m/1609.34} milhas")
 
    elif opcao == "e":
        milhas = float(input("milhas = "))
        print(f"{milhas} milhas = {milhas*1609.34} m")
    
    else:
        print("Opção inválida")
