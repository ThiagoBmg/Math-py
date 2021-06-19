def main():
    from random import random, randint
    import time
    import os
    from t_algorithm import algoritimoA
    from algorithm import algoritimoB

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
        ░╚═════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░

    █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗████
    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚═══
    """, end="\b")

    time.sleep(5)
    os.system('cls')
    counter = 1 

    while True:
        print('='*30, end="\n")
        print(f'Iniciando nova bateria de testes -> {counter}', end="\n")

        a = complex(random()-random() * 1j)
        b =  randint(5, 30)
        c =  random()

        print(f'Número Complexo: {a}' , end="\n")
        print(f'Número de Termos: {b}' , end="\n")
        print(f'Épsilon: {c}' , end="\n")

        alA = algoritimoA(a, b, c) # mohamed
        alB = algoritimoB(a, b, c) # Thiago

        if alA == alB:
            print('\n RESULTADO OK')
            time.sleep(0.001)
        else: 
            print('\n O RESULTADO NÃO ESTA OK')
            time.sleep(10)

        #print(alA) #print(alB)

        os.system('cls')
        counter +=1 
        
main()