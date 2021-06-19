def algoritimoA(a,b,c):
    #w=complex(input("Insira o número complexo 'w': "))
    #M=int(input("Insira o número de iterações 'M': "))
    #erro=float(input("Insira o erro máximo 'e': "))
    w=a
    z0=0
    M=b
    lista=list(range(M))
    erro = c
    x=[]
    lista_achei=[]
    #print(lista)

    for n in lista:
        zn=(z0)*(z0)+w
        x=x+[zn]
        z0=zn

    #print(lista)
    
    for n in lista:
        novo_indice=n+1
        achei=''
        while novo_indice<M:
            E=abs(x[n]-x[novo_indice])
            #print(E)
            if E<erro:
                achei=achei+"S"
            else:
                achei=achei+"N"
            novo_indice=novo_indice+1
        if not "N" in achei:
            if "S" in achei:
                lista_achei = lista_achei + [n + 1]

    if  lista_achei !=[]:
        return f"\nO menor índice procurado é {lista_achei[0]}"
    else:
        return f"\nNão há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor que {erro}"


#print(algoritimoA((0.44377114713087973-0.8119779139607677j),23, 0.6115388814166652))