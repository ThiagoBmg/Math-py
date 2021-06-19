def main():
    from random import random, randint
    import time
    import os
    from t_algorithm import algoritimoA
    from algorithm import algoritimoB

    test_range = 1500 # número de rodadas que o teste ira executar

    print("""
    █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗████
    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚═══

               ████████╗███████╗░██████╗████████╗███████╗
               ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝
               ░░░██║░░░█████╗░░╚█████╗░░░░██║░░░█████╗░░
               ░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░
               ░░░██║░░░███████╗██████╔╝░░░██║░░░███████╗
               ░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝

        ██╗░░░██╗███╗░░██╗██╗████████╗░█████╗░██████╗░██╗░█████╗
        ██║░░░██║████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗
        ██║░░░██║██╔██╗██║██║░░░██║░░░███████║██████╔╝██║██║░░██║
        ██║░░░██║██║╚████║██║░░░██║░░░██╔══██║██╔══██╗██║██║░░██║
        ╚██████╔╝██║░╚███║██║░░░██║░░░██║░░██║██║░░██║██║╚█████╔
         ╚═════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░

    █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗████
    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚═══
    """, end="\b")

    time.sleep(2)
    os.system('cls')
    counter = 1 

    while True:
        print('='*60, end="\n")
        print(f'Iniciando nova bateria de testes -> {counter}', end="\n")

        a = complex(random()-random() * 1j)
        b =  randint(5, 100)
        c =  random()

        print(f'Número Complexo: {a}' , end="\n")
        print(f'Número de Termos: {b}' , end="\n")
        print(f'Épsilon: {c}' , end="\n\n")

        alA = algoritimoA(a, b, c) 
        alB = algoritimoB(a, b, c) 

        if alA == alB:
            print('RESULTADO OK', end="\n")
            if 'O menor' in alA and 'O menor' in alB:
                print(f'\n {alA}', end="\n")
                print('='*60, end="\n")
                time.sleep(1)
            time.sleep(0.015)
        else: 
            print('O RESULTADO NÃO ESTA OK' , end="\n")
            print('='*60, end="\n")
            time.sleep(10)

        #print(alA) #print(alB)

        if counter >= 1800:
            
            break

        os.system('cls')
        counter +=1 

        
main()

#     log = []
#     log.append({"indice":current_in, "status": abs(z[d] - z[i]) < eps, "op":"abs(z[d] - z[i]) < eps", "zD":z[d], "zI":z[i]}) 
