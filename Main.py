
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
if operation==1:
    minimum=int(input())
    maximum=int(input())
    old_min=0
    old_max=255
    lst=read_ppm_file(filename)[0]#converting ppm file to the list i will be using it on other operations as well.
    for col in range(len(lst)):
        for row in range(len(lst)):
            for clr in range(3):#for loops for 3-d list.
                oldval=lst[col][row][clr]
                newval=minimum+(maximum-minimum)*(oldval-old_min)/(old_max-old_min)#assignment for new value.
                lst[col][row][clr]=round(newval,4)#round to four decimal.
    img_printer(lst)
elif operation==3:
    lst = read_ppm_file(filename)[0]
    for col in range(len(lst)):
        for row in range(len(lst[0])):#for loops to iterare over coloumn and rows.
            newcol=sum(lst[col][row])/3 #to obtain avg. value for new channel values.
            lst[col][row][0]=int(newcol)
            lst[col][row][1]=int(newcol)
            lst[col][row][2]=int(newcol)
    img_printer(lst)
elif operation==2:
    lst = read_ppm_file(filename)[0]
    sum0=0
    sum1=0
    sum2=0#counter for every r-g-b values through loops.
    for col in range(len(lst)):
        for row in range(len(lst)):
                sum0=sum0+lst[col][row][0]
                sum1=sum1+lst[col][row][1]
                sum2=lst[col][row][2]+sum2
    mean0=sum0/(len(lst)*len(lst))
    mean1=sum1/(len(lst)*len(lst))
    mean2=sum2/(len(lst)*len(lst))#reach mean values for every channel values with multipling by lenght lst squared.
    devsum0=0
    devsum1=0
    devsum2=0 #similar implement for deviaton sum through loops.
    for col in range(len(lst)):
        for row in range(len(lst)):
                devsum0+=(lst[col][row][0]-mean0)**2
                devsum1 += (lst[col][row][1] - mean1) ** 2
                devsum2 += (lst[col][row][2] - mean2) ** 2
    dev1=(devsum1/len(lst)**2)**(1/2)+0.000001
    dev2 = (devsum2/ len(lst) ** 2)**(1/2)+0.000001
    dev0 = (devsum0 / len(lst) ** 2)**(1/2)+0.000001#to implement given formula to find dev. values.

    for col in range(len(lst)):
        for row in range(len(lst)):
            val0=((lst[col][row][0]-mean0)/dev0)
            val1 = ((lst[col][row][1] - mean1) /dev1)
            val2 = ((lst[col][row][2] - mean2) /dev2)#to implement given final formula for final state of channel formulas.
            lst[col][row][0]=round(val0,4)
            lst[col][row][1]=round(val1,4)
            lst[col][row][2]=round(val2,4)#round to four decimal.
    img_printer(lst)
elif operation==4:
    filter_input=input()
    stride_input=int(input())
    lst=read_ppm_file(filename)[0]
    f=open(filter_input,"r")
    lstspc=[]
    for lines in f:
        lstm=[]
        for line in lines.split():
            lstm.append(line)
        lstspc.append(lstm)#to convert filter.txt to 2-d lst.

    lst_final=[]
    for row in range(0,len(lst)-len(lstspc)+1,stride_input):
        row_lst=[]
        for col in range(0,len(lst)-len(lstspc)+1,stride_input):
            smllst = []
            for clr in range(3):
                sum=0#counter for weighted sum.
                for i in range(len(lstspc)):
                    for j in range(len(lstspc)):#using 2d lst to iterate.
                        sum+=(float(lst[row+i][col+j][clr])*float(lstspc[i][j]))#to obtain general formula for different filter texts through nested for lopps.
                if sum < 0:
                    sum = 0
                if sum > 255:
                    sum = 255#conditionals in case exceed borders.
                smllst.append(int(sum))#to append sums into new lst.
            row_lst.append(smllst)#to obtain 2d lst.
        lst_final.append(row_lst)#to obtain final state of new 3d lst.
    img_printer(lst_final)
elif operation==5:
    filter_input = input()
    stride_input = int(input())
    lst = read_ppm_file(filename)[0]
    f = open(filter_input, "r")
    lstspc = []
    for lines in f:
        lstm = []
        for line in lines.split():
            lstm.append(line)
        lstspc.append(lstm)
        #same thing above operation to obtain 2-d filter lst.

    for row in range(len(lst)):
        for i in range(len(lstspc) // 2):
            lst[row].append([0, 0, 0])
            lst[row].insert(0, [0, 0, 0])#to add new zero groups along the image.
    for i in range(len(lstspc)//2):
        lst.insert(0, [[0, 0, 0] for x in range(len(lst[0]))])
        lst.append([[0, 0, 0] for x in range(len(lst[0]))])#to add new zero groups along the image.

    lst_final = []#all applications below same as operation-4.
    for row in range(0, len(lst) - len(lstspc) + 1, stride_input):
        row_lst = []
        for col in range(0, len(lst) - len(lstspc) + 1, stride_input):
            smllst = []
            for clr in range(3):
                summation = 0

                for i in range(len(lstspc)):
                    for j in range(len(lstspc)):
                        summation += (float(lst[row + i][col + j][clr]) * float(lstspc[i][j]))

                if summation < 0:
                    summation = 0
                if summation > 255:
                    summation = 255

                smllst.append(int(summation))
            row_lst.append(smllst)
        lst_final.append(row_lst)

    img_printer(lst_final)

elif operation==6:

    def range_eq(lst,row,col,range_input):
        if len(lst)%2==0:#to determine when code should finish itself(final state).
            if row==0 and col==len(lst)-1:
                return lst
        else:
            if row==len(lst)-1 and col==len(lst)-1:#to determine when code should finish itself(final state).
                return lst

        if col%2==0:#when coloumn is even nubmer
            if row < len(lst)-1:#in case of that condition rows should be raised one by one.
                if abs(lst[row][col][0]-lst[row+1][col][0])<range_input and abs(lst[row][col][1]-lst[row+1][col][1])<range_input and abs(lst[row][col][2]-lst[row+1][col][2])<range_input:
                    #statement above made channel values equal if it is true.
                    lst[row+1][col][0]=lst[row][col][0]
                    lst[row+1][col][1] = lst[row][col][1]
                    lst[row+1][col][2] = lst[row][col][2]

                return range_eq(lst,row+1,col,range_input)#recursive expression
            if row==len(lst)-1:#in case of that condition coloumns should be raised one by one.
                if abs(lst[row][col][0]-lst[row][col+1][0])<range_input and abs(lst[row][col][1]-lst[row][col+1][1])<range_input and abs(lst[row][col][2]-lst[row][col+1][2])<range_input:
                    # statement above made channel values equal if it is true
                    lst[row][col+1][0] = lst[row][col][0]
                    lst[row][col+1][1] = lst[row][col][1]
                    lst[row][col+1][2] = lst[row][col][2]
                return range_eq(lst,row,col+1,range_input)#recursive expression
        else:
            if 0<row <= len(lst)-1:
                if abs(lst[row][col][0]-lst[row-1][col][0])<range_input and abs(lst[row][col][1]-lst[row-1][col][1])<range_input and abs(lst[row][col][2]-lst[row-1][col][2])<range_input:
                    lst[row-1][col][0]=lst[row][col][0]#in case of that condition rows should be reduced one by one.
                    lst[row-1][col][1] = lst[row][col][1]
                    lst[row-1][col][2] = lst[row][col][2]

                return range_eq(lst,row-1,col,range_input)
            if row==0:
                if abs(lst[row][col][0]-lst[row][col+1][0])<range_input and abs(lst[row][col][1]-lst[row][col+1][1])<range_input and abs(lst[row][col][2]-lst[row][col+1][2])<range_input:
                    lst[row][col+1][0] = lst[row][col][0]#in case of that condition coloumn should be raised one by one.
                    lst[row][col+1][1] = lst[row][col][1]
                    lst[row][col+1][2] = lst[row][col][2]
                return range_eq(lst,row,col+1,range_input)

    range_input = int(input())
    lst = read_ppm_file(filename)[0]
    x=range_eq(lst,0,0,range_input)
    img_printer(x)
elif operation==7:
    def colr_quan(lst,row,col,clr,range_input):
        if len(lst)%2==0:#to determinde when code should finish itself.(base conditions)
            if row==0 and col==len(lst)-1 and clr==2:
                return lst
        else:
            if row==len(lst)-1 and col==len(lst)-1 and clr==2:
                return lst

        if clr % 2 == 0:#condition for when colour index is even.
            if col%2==0:#condition for when coloumn index is even.They should be used for control pattern.

                if row < len(lst)-1:#in this condition rows should be raised one by one.
                    if abs(lst[row][col][clr]-lst[row+1][col][clr])<range_input:#in case of that made both equal with respect to previous one.
                        lst[row + 1][col][clr]=lst[row][col][clr]
                    return colr_quan(lst,row+1,col,clr,range_input)#recursive expression
                if row==len(lst)-1:#in this condition coloumns should be raised one by one.
                    if abs(lst[row][col][clr]-lst[row][col+1][clr])<range_input:#in case of that made both equal with respect to previous one
                        lst[row][col + 1][clr]=lst[row][col][clr]
                    return colr_quan(lst,row,col+1,clr,range_input)#recursive expression
                if row==len(lst)-1 and col==len(lst)-1:#in this condition colours should be raised one by one.
                    if abs(lst[row][col][clr] - lst[row][col][clr+1]) < range_input:#in case of that made both equal with respect to previous one.
                        lst[row][col][clr+1] = lst[row][col][clr]
                    return colr_quan(lst,row,col,clr+1,range_input)#recursive expression
            else:
                if 0<row<=len(lst)-1:#in this condition rows should be reduuced one by one.
                    if abs(lst[row][col][clr]-lst[row-1][col][clr])<range_input:
                        lst[row - 1][col][clr]=lst[row][col][clr]
                    return colr_quan(lst,row-1,col,clr,range_input)#recursive expression
                if row==0 and col!=len(lst)-1:#in this condition coloumns should be raised one by one.
                    if abs(lst[row][col][clr]-lst[row][col+1][clr])<range_input:
                        lst[row][col + 1][clr]=lst[row][col][clr]
                    return colr_quan(lst,row,col+1,clr,range_input)#recursive expression
                if row==0 and col==len(lst)-1:#in this condition colours should be raised one by one.
                    if abs(lst[row][col][clr] - lst[row][col ][clr+1]) < range_input:
                        lst[row][col][clr+1] = lst[row][col][clr]
                    return colr_quan(lst, row, col , clr+1, range_input)#recursive expression

        if clr%2!=0:
            if col%2==0:
                if 0<row<=len(lst)-1:#in this condition rows should be reduced one by one.
                    if abs(lst[row][col][clr] - lst[row - 1][col][clr]) < range_input:#same as above.
                        lst[row -1][col][clr] = lst[row][col][clr]
                    return colr_quan(lst, row - 1, col, clr, range_input)#recursive expression
                if row==0 and col!=0:#in this condition coloumns should be reduced one by one.
                    if abs(lst[row][col][clr] - lst[row][col-1][clr]) < range_input:
                        lst[row ][col-1][clr] = lst[row][col][clr]
                    return colr_quan(lst, row, col-1, clr, range_input)#recursive expression
                if row==0 and col ==0 :#in this condition colours should be raised one by one.
                    if abs(lst[row][col][clr] - lst[row][col][clr+1]) < range_input:
                        lst[row][col][clr+1] = lst[row][col][clr]
                    return colr_quan(lst, row, col, clr+1, range_input)#recursive expression
            else:
                if row<len(lst)-1:#in this condition rows should be raised one by one.
                    if abs(lst[row][col][clr] - lst[row + 1][col][clr]) < range_input:
                        lst[row +1][col][clr] = lst[row][col][clr]
                    return colr_quan(lst, row + 1, col, clr, range_input)#recursive expression
                if row==len(lst)-1:#in this condition coloumns should be reduced one by one.
                    if abs(lst[row][col][clr] - lst[row][col-1][clr]) < range_input:
                        lst[row ][col-1][clr] = lst[row][col][clr]
                    return colr_quan(lst, row, col-1, clr, range_input)#recursive expression
                if row==0 and col==0:#in this condition colours should be raised one by one.
                    if abs(lst[row][col][clr] - lst[row][col][clr + 1]) < range_input:
                        lst[row][col][clr + 1] = lst[row][col][clr]
                    return colr_quan(lst, row, col, clr + 1, range_input)#recursive expression

    range_input = int(input())
    lst = read_ppm_file(filename)[0]
    x = colr_quan(lst,0,0,0,range_input)
    img_printer(x)






























# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

