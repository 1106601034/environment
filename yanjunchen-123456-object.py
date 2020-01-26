from Week2 import create_bucket
from Week2 import put_object
from Week2 import delete_object
from Week2 import delete_bucket
from Week2 import copy_object
from Week2 import download_file
import time

#A list supports pointing functions, warning, etc
menu = [1,2,3,4,5,6,7]

#interface
def interface(when):
    print('#############################')
    #welcome when startup
    if when:
        print('-----------Welcome-----------')
    print('---1-Creat-a-bucket----------')
    print('---2-Put-an-object-----------')
    print('---3-Delete-an-object--------')
    print('---4-Delete-an-bucket--------')
    print('---5-Copy-an-object----------')
    print('---6-Download-an-object------')
    print('---7-exit--------------------')
    print('#############################')
    #leaves selection to user, will notices instead of crash if got invaild input
    selection = 0
    while selection not in menu:
        try:
            selection = int(input('select an action: '))
        except ValueError:
            print('Invaild command.')
        else:
            if selection in menu:
                return selection
            else :
                print('Invaild command')

def guide(mask):
    if mask == 1:
        create_bucket.main()
    if mask == 2:
        put_object.main()
    if mask == 3:
        delete_object.main()
    if mask == 4:
        delete_bucket.main()
    if mask == 5:
        copy_object.main()
    if mask == 6:
        download_file

def main():
    #the program will not end until user click end.
    #welcome user when startup, will not greet unless restart 
    selection = interface(True)
    while (1):
        if selection == 7:
            #print time then stop
            print(time.ctime())
            return 0
        else:
            guide(selection)
            selection = interface(False)
            
main()