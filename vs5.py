print("Hello search your favorite website")
import webbrowser
def open_website():
    webbrowser.open('https://www.youtube.com/watch?v=7r7DDHnQpqc&list=PLaKmzX_hXWkJIXbKM2BaFOR04FWMayGrA&index=2')
def open_website1():
    webbrowser.open('www.linkedin.com')
def open_website2():
    webbrowser.open2('https://www.datascienceacademy.com.br')

def choose_site():
    print("Hello choose and '0', '1', '2':" )    
    print("Press 0 - Site '1' :")
    print("Press 1 - Site '2' :")
    print("Press 2 - Site '3' :")
    choose = input("Please choose :\n"   )

    if choose == '0':
        open.website()
    elif choose == '1':
        open_website1
    elif choose == '2':
        open_website2
    else:
        print("Sorry this value is not found! ")

if __name__ == "_main__":
    open_website 