from PIL import Image

#start: Greeting section
user_name = input("Hello! Could you please introduce yourself? : ")
print('Greetings ', user_name,'!' )
print('Now you can make your choice about what information you\'d like to export about the picture!')

#appoint the work image
img = Image.open('./image1.jpeg')


#options menu
menu_options = {
    1: 'Picture mode',
    2: 'Picture format',
    3: 'Picture size in px',
    4: 'Exit the program'
}
#option menu structure
def print_menu():
    for key in menu_options.keys():
        print (key, '->', menu_options[key] )
#option menu choices
def option1():
    print('Picture mode \'Option 1\'')
def option2():
    print('Picture format \'Option 2\'')
def option3():
    print('Picture size in px \'Option 3\'')
def option4():
    print('Exit the program \'Option 4\'')

#action section
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Make your choice: '))
        except:
            print('Please enter a digit from 1-7')
        if option == 1:
            print(img.mode)
        elif option == 2:
            print(img.format)
        elif option == 3:
            print(img.size)
        elif option == 4:
            print('Thank you! Goodbye!')
            exit()
        else:
            print('Out of range choice - please choose a digit between 1 to 3 to continue or 4 to exit the program')

