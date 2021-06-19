def algoritimo(a,b,c):
    #import time
    z = [0]
    w = a  #w = complex(input("Digite w: "))
    M = b #M = int(input('Digite o valor de M: '))
    eps = c  #eps = float(input('Digite o epsilon: '))
    z = [w]

    for k in range(M-1):
        z.append(z[k]*z[k] + w)
    
    for d in range(len(z)):
        tmp = [] 
        current_in = d+1

        for i in range(M):
            if i <= d:
                a = 1 
            elif abs(z[d] - z[i]) < eps:
                tmp.append(True) #print(f"{d+1} {z[d]} - {z[i]} = {abs(z[d] - z[i])} {True}", end="\n")
            else:
                tmp.append(False) #print(f"{d+1} {z[d]} - {z[i]} = {abs(z[d] - z[i])} {False}", end="\n")
        #print('*'*10) #print(tmp)

        if not False in tmp and tmp !=[]:
            return f"\nO menor índice procurado é {current_in}"
    return f"\nNão há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor que {eps}"
    #print(tmp) #print(len(z))
