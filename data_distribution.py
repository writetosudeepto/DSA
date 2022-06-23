def distribute(arr,start,end,el,carry,checklist):
    if(el=='_'):
        el = 0 
    count = end-start+1
    print("el type:",type(el),"carry type:",type(carry),"count type:",type(count))
    avg = (el+carry)//count
    for i in range(start,end+1):
        arr[i] = avg
    return avg
def mapint(ch):
        if ch!='_':
            return int(ch)
        return ch
def data_distribute(input_data):
    input_data = list(map(mapint,input_data.split(',')))
    checklist = []
    avgs = [0,]
    currindex = 0
    sindex = 0
    for i,el in enumerate(input_data):
        if len(checklist)<3 and el!='_':
            if el not in checklist: 
                checklist.append(el)
                carry = avgs[sindex]
                sindex+=1
                navg = distribute(input_data,currindex,i,el,carry,checklist)
                avgs.append(navg)
                currindex = i
            else:
                continue
        elif len(checklist)>=2 and el=='_':
            carry = avgs[sindex]
            distribute(input_data,currindex,len(input_data)-1,el,carry,checklist)
            break
    return input_data

print(data_distribute("_,_,30,_,_,_,50,_,_"))