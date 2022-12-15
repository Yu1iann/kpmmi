from openpyxl import load_workbook

def clock(tmin):
    hour=tmin//60
    minn =tmin%60
    return hour,minn

def output(nameday,daypath,new_pathi,TT):
    print('_____________________________ ')
    print(nameday)
    tim0=9*60
    for i in range(0,len(daypath),2):
        j=int(i/2)
        indTT= TT[0].index(new_pathi[j])
        print(TT[1][indTT])
        hour,min=clock(tim0)
        print('Время прибытия ',"%02d:%02d" % (hour, min))
        hour, min = clock(daypath[i])
        print('Продолжительность посещения',daypath[i], "%02d:%02d" % (hour, min))
        tim0=daypath[i]+tim0
        hour, min = clock(tim0)
        print('Время убытия ', "%02d:%02d" % (hour, min))
        if i<(len(daypath)-1):
            print('Дистанция до следующей ', daypath[i+1])
            tim0=tim0+daypath[i+1]

    return 0
def output2(TP0,PARAM,nameday,daypath,new_pathi,TT,oldrow):
    wb = load_workbook('Решение.xlsx')
    #print(wb.sheetnames)
    sheet = wb['Отчет']
    #cell = sheet.cell(row=row, column=col)
    nn=len(daypath)-len(daypath)//2
    print('____________nn ',nn)
    value = str(nameday)
    TP0=str(TP0)
    tim0 = 9 * 60
    i=0
    j=0
    for row in range(oldrow,oldrow+nn):
        j=i*2
        cell=sheet.cell(row=row,column=1) #день недели
        cell.value=value
        cell = sheet.cell(row=row, column=2)  # день недели
        cell.value = TP0
        indTT= TT[0].index(new_pathi[i])
        iTT = PARAM[0].index(TT[1][indTT])
        indTT=str(TT[1][indTT])

        nameTT=PARAM[1][iTT]
        adresTT = PARAM[2][iTT]
        chastotaTT=PARAM[3][iTT]
        cell = sheet.cell(row=row, column=3) #Номер точки маршрута
        cell.value=indTT
        cell = sheet.cell(row=row, column=4)
        cell.value=nameTT

        cell = sheet.cell(row=row, column=5)
        cell.value=adresTT

        cell = sheet.cell(row=row, column=9) # Частота посещения ( раз в неделю)
        cell.value=chastotaTT
        hour,min=clock(tim0)
        vp=str("%02d:%02d" % (hour, min))
        cell = sheet.cell(row=row, column=6)  # Время прибытия
        cell.value=vp
        hour, min = clock(daypath[j])
        pp=str("%02d:%02d" % (hour, min))
        cell = sheet.cell(row=row, column=7)  # Продолжительность посещения
        cell.value=pp
        tim0=daypath[j]+tim0
        hour, min = clock(tim0)
        vu=str("%02d:%02d" % (hour, min))
        cell = sheet.cell(row=row, column=8)  # Время убытия
        cell.value=vu
        if row!=oldrow+nn-1:
            ds=str(daypath[j+1])
            tim0=tim0+daypath[j+1]
            cell = sheet.cell(row=row, column=10)  # Дистанция до следующей
            cell.value = ds
        i+=1

    wb.save('Решение.xlsx')
    #wb.close()
    return 0

def clocwb():
    wb = load_workbook('Решение.xlsx')
    wb.save('Решение.xlsx')
    wb.close()
    return 0


