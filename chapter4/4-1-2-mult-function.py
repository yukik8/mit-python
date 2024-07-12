def mult(int1,int2):
    #inputがNoneかどうかは, ==None ではなく =="" で判定
    # （常にstr型であるためNone型にならない）
    if int1!= "": int1=int(int1)
    else: return int2
    if int2!= "": int2=int(int2)
    else: return int1
    return int1*int2

#inputはstr型を返す
int1=input('int1:')
int2=input('int2:')
print(mult(int1,int2))