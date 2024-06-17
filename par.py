# Par ou Impar

while True:
    
    print("\n\t\t\t -- Par ou Impar --")
      
    print("1. Par ou Impar")
    print("2. Sair")
    
    op = int(input("\nOpção:"))
    
    if op == 1:
        print("\n\t\t\t -- Par ou Impar --")
        
        # Entrada 
        n1 = float(input("Informe n1: "))
        
        total = n1 / 2
        
        #saida 
        if total % 2 == 0:
            print("\n\t\t O NÚMERO É PAR! \n")
        else:
            print("\n\t\t O NÚMERO É IMPAR! \n")
            
    
    elif op== 2:
        print("\n\ Beijoss!\n\n")
        break
    else:
        print("\n\nOpção {} Incorreta!\n\n".format(op))

        
        
    
      
