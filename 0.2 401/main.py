import numpy as np
from  python_tsp.exact import solve_tsp_dynamic_programming #python-tsp
import output as out
import input as imp
import daypath as dp
import nextday as nd
#from variables import R, NA, xgamma, xalpha, xn
#import functions as fun

nday = 7  # период 7 дней
nameday=['Monday','Tuesday ','Wednesday ','Thursday ','Friday','Saturday ','Sunday']
rowpast=1 # строка с которой начинается считывание для текущего тп
oldrow=2

for g in range(1):  #14
    TP0,PARAM,nq, tq, TT,mr=imp.input1(rowpast)
    rowpast+=len(nq)

    #nq, tq, TT,mr=imp.input()
    n_idel=1 # для первого прогона цикла
    for i in range(nday):
        nda=i
        print('_________DAY__',i+1,'_______ ')
        #print('_________PARAM__', '_______ ')
        #for k in range(4):
            #print(PARAM[k])
        #print(PARAM)
        if n_idel == 0:
            first_TT = iposl + 1
        else:
            matls = np.array(mr)
            path, dist = solve_tsp_dynamic_programming(matls)  # решение задачи коммивояжера
            for i in range(len(path)):
                path[i] += 1
            max_nq = nq.index(max(nq)) + 1  # ТТ с наибоьшим количеством посещений
            first_TT = path.index(max_nq)  # первое место посещения
        new_pathi, daypath, iposl = dp.daypath(path, nq, tq, mr, first_TT)
        #out.output(nameday[nda],daypath,new_pathi,TT)
        out.output2(TP0,PARAM,nameday[nda], daypath, new_pathi, TT,oldrow)
        oldrow+=iposl+1
        if iposl==0: break
        tq, nq, TT, mr, n_idel = nd.nextday(iposl, new_pathi, nq, tq, TT, mr)
        path=new_pathi
        print('__________oldrow________ ',oldrow)
        print('__________________ ')
        print(path, dist)
out.clocwb()