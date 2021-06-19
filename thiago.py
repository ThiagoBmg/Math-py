def resolucao():
    import time
    z = [0]
    #w = complex(input("Digite w: "))
    #M = int(input("Digite a quantidade de termos da sequência: "))
    #eps = float(input("Digite o épsilon: "))
    w = complex(0.2-0.3j) #w = complex(input('Digite o valor de w: '))
    M = 20 #M = int(input('Digite o valor de M: '))
    eps = 0.05 #eps = float(input('Digite o epsilon: '))
    z = [w]

    for k in range(M-1):
        z.append(z[k]**2 + w)
    
    for d in range(len(z)):
        tmp = [] 
        current_in = d+1

        for i in range(M):
            if i <= d:
                a = 1 
            elif abs(z[d] - z[i]) >= eps:
                #print(f"{d+1} {z[d]} - {z[i]} = {abs(z[d] - z[i])} {False}" , end="\n")
                #time.sleep(1)
                #tmp.append({d+1 : False})
                tmp.append(False)
            else:
                #print(f"{d+1} {z[d]} - {z[i]} = {abs(z[d] - z[i])} {True}", end="\n")
                #time.sleep(1)
                #tmp.append({d+1 : True})
                tmp.append(True)
        
        #print(tmp)

        if not False in tmp:
            return print(f"O menor índice procurado é {current_in}", end="\n")
            #time.sleep(10000)


    print(tmp)
    print(len(z))

resolucao()