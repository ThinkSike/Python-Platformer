import sqlite3

g_name=input("Gamer name: ")
password=input("Password: ")

conn = sqlite3.connect('inplantdb.db')

#if g_name=="NEXSIKE" and password=="$T":
print("Welcome ",g_name," !")
print("Your credentials are secured with us.")
#else:
print("Invalid user name or password.")


#execfile('mario.py')

# mario.main(window)
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# WIDTH, HEIGHT = 1000, 800