from buildings import buildings
import pickle

def name_list():
    with open("names.txt", 'w') as f:
        res = "["
        lines = buildings
        for i in lines:
            name = i['nameS']
            res += "'" + name + "', "
        res += "]"
        f.write(res)

def des_list():
    with open("des.txt", 'w') as f:
        res = "["
        lines = buildings
        ind = 0
        for i in lines:
            ind += 1
            des = i['des']
            # print(des)
            des = des.replace('\n', '')
            des = des.replace('\t', '')
            res += "'" + des + "', "
            if ind%10 == 0: res += '\n'
        res += "]"
        f.write(res)

if __name__ == "__main__":
    # name_list()
    des_list()