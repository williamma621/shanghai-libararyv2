from buildings import buildings
import pickle

def name_list_C():
    with open("names.txt", 'w') as f:
        res = "["
        lines = buildings
        ind = 0
        for i in lines:
            ind += 1
            name = i['nameS']
            res += "'" + name + "', "
            if ind%100 == 0: res += '\n'
        print(ind)
        res += "]"
        
        f.write(res)

def des_list_C():
    with open("desC.txt", 'w') as f:
        res = "["
        lines = buildings
        ind = 0
        for i in lines:
            ind += 1
            des = i['des']
            if des == "":
                des = i['address']
            # print(des)
            else:
                des = des.replace('\n', '')
                des = des.replace('\t', '')
            res += "'" + des + "', "
            if ind%9 == 0: res += '\n'
        res += "]"
        # print(ind)
        f.write(res)

def info_C_list():

    with open("infoC.txt", 'w') as f:
        res = "["
        lines = buildings
        ind = 0
        for i in lines:

            temp = "{"

            #get name
            name = i['nameS']
            temp += "name:'" + name + "', "

            # get description
            des = i['des']
            if des == "":
                des = i['address']
            # print(des)
            else:
                des = des.replace('\n', '')
                des = des.replace('\t', '')
            temp += "des:'" + des + "', "

            # get longitude and latitude
            y = i['long']
            x = i['lat']
            if len(y) == 0 or len(x) == 0:
                continue
            temp += "y:'" + y + "', "
            temp += "x:'" + x + "'"
            temp += "}"

            res += temp + ", "
            ind += 1
            if ind%10 == 0: res += '\n'
        res = res[:-2] + "]"
        print(ind)
        f.write(res)



if __name__ == "__main__":
    # name_list_C()
    # des_list_C()
    info_C_list()