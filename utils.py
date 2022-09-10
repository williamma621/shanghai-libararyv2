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

if __name__ == "__main__":
    # name_list_C()
    des_list_C()