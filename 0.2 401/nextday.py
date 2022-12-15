# новый день

#функция удаления нужной строки и столбцах
def Delete(matrix,index1,index2):
    del matrix[index1]
    for i in matrix:
        del i[index2]
    return matrix

# новый день
def nextday(iposl,new_pathi,nq,tq,TT,mr):
    print('__________________nextday ')
    print(' до TT', TT)
    print (' до nq ',nq) # Количество посещений
    for i in range (0,iposl+1): #____________!!!!!!!!!!! +1
        ni=new_pathi[i]-1
        print ('ni  =' ,ni)
        nq[ni]=nq[ni]-1 # уменьшение количества посщени оставшихся на этой неделе

    print(' nq -1 ', nq)  # Количество посещений
    #print('TT ',TT)
    idel=[] # какие ТТ больше не надо посещать
    for i in range(len(nq)):
        if nq[i]==0:
            print('nq[i]==0 ', nq[i] ,i)
            idel.append(i+1)

    if len(idel) > 0:
        print('____ idel =', idel)
        for i in range(len(idel)):
            j=idel[i]-1-i
            #print('____ j =', j)
            nq.pop(j)
            #print('nq ', nq)
            Delete(mr,j,j)
            tq.pop(j)
            TT[0].pop(j)
            TT[1].pop(j)
        for i in range(len(TT[0])):
            TT[0][i]=i+1
        print ('idel ',idel)
        # print ('matrix')
        # for i in range(len(mr)):
        #     print(i+1, ' ', mr[i])
        #print (mr)
        print('TT',TT)
        print('nq ',nq)
    #print('idel ', idel)
    print('len idel ', len(idel))
    return tq,nq,TT,mr,len(idel)

