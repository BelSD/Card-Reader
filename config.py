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
        retour = "test"
        return retour

    def Pwd(self):
        retour = "test"
        return retour

    def Db(self):
        retour = "test"
        return retour

    def Host(self):
        retour = "localhost"
        return retour

    def Instruction_Table(self):
        retour = "card_reader"
        return retour

class Led_Position:
    
    def Power(self):
        retour = 18
        return retour

    def Read(self):
        retour = 11
        return retour

    def Ready(self):
        retour = 12
        return retour

class Buzzer_Position:
    
    def Buzzer_1(self):
        retour = 16
        return retour

    def Buzzer_ON(self):
        retour = True
        return retour

class LCD:
    
    def Backlight(self):
        retour = 29
        return retour

    def Time_OUT(self):
        retour = 1
        return retour

class Button:
    
    def Power_bt(self):
        retour = 31
        return retour

    def Reset_bt(self):
        retour = 32
        return retour

    def PRG_End_bt(self):
        retour = 33
        return retour
