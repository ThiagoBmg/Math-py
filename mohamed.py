def algoritimoA(a,b,c):
    #print("\nNome: Mahmoud Maksoud Hindi\nRA: 22.121.085-9\n\nNome: Ibrahim Said El Orra\nRA: 22.121.058-6\n")
    #w=complex(input("Insira o número complexo 'w': "))
    w=a
    z0=0
    #M=int(input("Insira o número de iterações 'M': "))
    M=b
    lista=list(range(M))
    #erro=float(input("Insira o erro máximo 'e': "))
    erro = c
    x=[]
    lista_achei=[]

    for n in lista:
        zn=(z0)*(z0)+w
        x=x+[zn]
        z0=zn

    'print(x)'

    for n in lista:
        novo_indice=n+1
        achei=''
        while novo_indice<M:
            E=abs(x[n]-x[novo_indice])
            'print(E)'
            if E<erro:
                achei=achei+"S"
            else:
                achei=achei+"N"
            novo_indice=novo_indice+1
        if not "N" in achei:
            if "S" in achei:
                lista_achei = lista_achei + [n + 1]

    'print(lista_achei)'

    if  lista_achei !=[]:
        print(f"\nO menor índice procurado é {lista_achei[0]}")
    else:
        print(f"\nNão há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor que {erro}")

