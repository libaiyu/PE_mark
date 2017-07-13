
import math

cal_dict = {1:'+', 2:'-', 3:'x', 4:'/', 5:'-', 6:'/' }

def cal_two_num(x1,x2):
    yy = []
    yy.append(x1+x2)
    yy.append(x1-x2)
    yy.append(x1*x2)
    if x2:
        yy.append(x1/x2)
    yy.append(x2-x1)
    if x1:
        yy.append(x2/x1)
    return(yy)

def cal_four(a,b,c,d):
    y1 = cal_two_num(a,b)
##    print('y1',y1)
    count1 = 0
    for y in y1:
        count1 += 1
        y2 = cal_two_num(y,c)
##        print('y2',y2)
        count2 = 0
        for y in y2:
            count2 += 1
            y3 = cal_two_num(y,d)
##            print('y3',y3)
            count3 = 0
            for y in y3:
                count3 += 1
                if y == 24:   # output the sequence of calculate.
                    global snum
                    snum += 1
##                    print( '--解法%d--:  '% snum, end='')
                    out_four1 = out_two_cal(count1,a,b)
                    out_four2 = out_two_cal(count2,out_four1,c)
                    out_four3 = out_two(count3,out_four2,d)
                    dhr.setdefault(out_four3,1)
##                    print( out_four3)
    xj_cal( a, b, c, d)

def xj_cal(a,b,c,d):                   
    y1 = cal_two_num(a,b)
    y4 = cal_two_num(c,d)
    count1 = 0
    for e in y1:
        count1 += 1
        count2 = 0
        for f in y4:
            count2 += 1
            y5 = cal_two_num(e,f)
            count3 = 0
            for y in y5:
                count3 += 1
                if y == 24:   # output the sequence of calculate.
                    global snum
                    snum += 1
##                    print( '--解法%d--:  '% snum, end='')
                    out_four1 = out_two_cal(count1,a,b)
                    out_four2 = out_two_cal(count2,c,d)
                    out_four3 = out_two(count3,out_four1,out_four2)

                    dhr.setdefault(out_four3,1)
##                    print( out_four3)

                    

def out_two_cal(count, a, b):
    if count < 5:
        solve_out = '('+str(a)+cal_dict[count]+str(b)+')'
    else:
        solve_out = '('+str(b)+cal_dict[count]+str(a)+')'
    return(solve_out)

def out_two(count, a, b):
    if count < 5:
        solve_out = str(a)+cal_dict[count]+str(b)
    else:
        solve_out = str(b)+cal_dict[count]+str(a)
    return(solve_out)
                        
###########################
a,b,c,d = map(int, input('please input 4 numbers(1-13):').split()) ##abcd = input('a,b,c,d:1-13')

dhr = {}
snum = 0
cal_four(a,b,c,d)    # 2,3,5,12, ZeroDivisionError: division by zero
cal_four(a,b,d,c)
cal_four(a,c,b,d)
cal_four(a,c,d,b)
cal_four(a,d,b,c)
cal_four(a,d,c,b)
cal_four(b,c,a,d)
cal_four(b,c,d,a)
cal_four(b,d,a,c)
cal_four(b,d,c,a)
cal_four(c,d,a,b)
cal_four(c,d,b,a)

num = 0
for each in dhr:
    num += 1
    print( '--解法%d--: %s '% (num, each))

##innum = []    
##for x in range(4):
##    innum.append( int( input( 'please input a number(1-13):')))
##a = innum[0]
##b = innum[1]
##c = innum[2]
##d = innum[3]
