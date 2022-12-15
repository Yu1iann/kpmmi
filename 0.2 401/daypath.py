def Reloorization_path(dist,first_TT):
    new_pathi = [] * len(dist)
    dlt = len(dist) - first_TT
    for j in range(len(dist)):  # перестанавливаем путь
        if j < (dlt):
            new_pathi.append(dist[first_TT + j])
        else:
            new_pathi.append(dist[-dlt + j])
    return new_pathi

def daypath(dist,nq,tq,mr,first_TT):
    tday = 9 * 60 + 30  # рабочий день ТП
    path = []

    new_pathi=Reloorization_path(dist,first_TT)
    #print(' first_TT ', first_TT)
    print('__________________daypath ')
    print(' изнач nq ', nq)
    print(' new_pathi ',new_pathi)
    print(' len(new_pathi) ', len(new_pathi))


    for i in range(len(new_pathi)-1):  # находим время поездок вмести с посящениями на маршруте
        path.append(mr[new_pathi[i] - 1][new_pathi[i + 1] - 1] * 60 / (1000 * 60) + tq[new_pathi[i + 1] - 1])
        print('i ', i, '  ', new_pathi[i],new_pathi[i + 1], '  ', path[i], '  min')
    # __________________________________
    daypath=[]
    dist_real=tq[new_pathi[0] - 1]
    daypath.append(tq[new_pathi[0] - 1] ) # старт с точки первого ТТ и его посещени я
    #print('daypath0 = ',daypath)
    #iposl=float('inf')
    iposl=0
    for i in range(0, len(path)):  # проверяем не превзашло ли время работы дневной лимит
        dist_real += path[i]
        iposl = i
        if dist_real > tday:
            dist_real -= path[i]
            iposl = i
            break
        daypath.append(mr[new_pathi[i] - 1][new_pathi[i + 1] - 1] * 60 / (1000 * 60))
        daypath.append(tq[new_pathi[i + 1] - 1])
    print('daypath = ',daypath)
    print('dist_real =', dist_real)
    print('iposl =',iposl)
    #print('new_pathi[0] =',new_pathi[0])
    return new_pathi,daypath, iposl