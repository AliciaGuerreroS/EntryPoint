"""Encontrar los números comunes entre 2 listas sin usar set."""
list1=[1,2,3,5,6,7,8]
list2=[1,4,3,2,5,6,7,8]

def common_element(list1,list2):
    new_list=[]
    for i in list1:
        if i in list2:
            new_list.append(i)
    print(new_list)

if __name__== '__main__':
    common_element(list1,list2)