#
#Creer Par Waldorf Jean-Pierre (c)BelSD (2005-2018)
#Config file
#

class DEFAULT:
    
    def APP_Name(self):
        retour = "BelSD Card Reader"
        return retour
    def Client_Name(self):
        retour = "   Jessynails   "
        return retour
    
class Database:
    
    def User(self):
        retour = "DB_User_Login"
        return retour

    def Pwd(self):
        retour = "DB_Password"
        return retour

    def Db(self):
        retour = "DB_Data_base"
        return retour

    def Host(self):
        retour = "localhost"
        return retour

    def Instruction_Table(self):
        retour = "card_reader"
        return retour

class Led_Position:
    
    def Power(self):
        retour = 18 # Power Led GPIO Pin
        return retour

    def Read(self):
        retour = 11 # Read Led GPIO Pin
        return retour

    def Ready(self):
        retour = 12 # Ready Led GPIO Pin
        return retour

class Buzzer_Position:
    
    def Buzzer_1(self):
        retour = 16  # Buzzer GPIO Pin
        return retour

    def Buzzer_ON(self):
        retour = True # True -> Buzzer ON | False -> Buzzer OFF
        return retour

class LCD:
    
    def Backlight(self):
        retour = 29 # Backlight LCD Display GPIO Pin
        return retour

    def Time_OUT(self):
        retour = 1 # Backlight LCD Display power OFF after x Minute
        return retour
    
    def I2CBUS(self):
        retour = 1 # I2C BUS (0 -- original Pi, 1 -- Rev 2 Pi)
        return retour
    
    def ADDRESS(self):
        retour = 0x27 # LCD I2C Address
        return retour
class Button:
    
    def Power_bt(self):
        retour = 31 # Power Button GPIO Pin
        return retour

    def Reset_bt(self):
        retour = 32 # Reset Button GPIO Pin
        return retour

    def PRG_End_bt(self):
        retour = 33 # Program End Button GPIO Pin
        return retour
