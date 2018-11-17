#!/usr/bin/env python
# -*- coding: utf8 -*-
# Version modifiee de la librairie https://github.com/mxgxw/MFRC522-python

import os
import RPi.GPIO as GPIO
#import I2C_LCD_driver
#import MFRC522
import signal
import sys
import config
import time
import MySQLdb
from time import sleep
import BelSD_RFID
from threading import Thread

###############################
# Initialisation du programme #
###############################

# Lire fichier de configuration
LED_Position = config.Led_Position()
DataBase = config.Database()
BUZZER_Position = config.Buzzer_Position()
LCD_Info = config.LCD()
BT = config.Button()
BASE_CFG = config.DEFAULT()

# Les Fonctions
LED = BelSD_RFID.LEDS()
BUZZER = BelSD_RFID.BUZZERS()
MYSQL = BelSD_RFID.MYSQL()
BKL_LCD = BelSD_RFID.BackLight()

La_Table = DataBase.Instruction_Table()

# Initialisation du GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Initialisation LCD
mylcd = BelSD_RFID.lcd()

# Led Rouge
Power_led = LED_Position.Power()
LED.INI(Power_led)

# Led Bleu
Read_led = LED_Position.Read()
LED.INI(Read_led)

# Led Verte
Ready_led = LED_Position.Ready()
LED.INI(Ready_led)

# Buzzer
Buzzer_1 = BUZZER_Position.Buzzer_1()
BUZZER.INI(Buzzer_1)
buzzer = BUZZER_Position.Buzzer_ON()

#Backlight LCD
LCD = LCD_Info.Backlight()
BKL_LCD.INI(LCD)
LCD_Time_OUT = (LCD_Info.Time_OUT())*60

# Button PRG End
PRG_END_BUTTON=BT.PRG_End_bt()
GPIO.setup(PRG_END_BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Button Reset et Power
RESET_BUTTON=BT.Reset_bt()
POWER_OFF_BUTTON=BT.Power_bt()
GPIO.setup(RESET_BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(POWER_OFF_BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)

continue_reading = True
boucle = True

#########################
# Définition des Thread #
#########################

class RPI_BT(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        BS1=False
        BS2=False
        global RESET_BUTTON
        global POWER_OFF_BUTTON
        global PRG_END_BUTTON
        global mylcd
        global boucle
        global Power_led
        global Read_led
        global Ready_led
        while(1):
                if GPIO.input(RESET_BUTTON)==0:
                        boucle = False
                        sleep(1)
                        BKL_LCD.ON(LCD)
                        mylcd.lcd_clear()
                        mylcd.lcd_display_string("  Reboot du PC  ", 1)
                        mylcd.lcd_display_string("  en court...   ", 2)
                        sleep(2)
                        LED.OFF(Read_led)
                        LED.OFF(Ready_led)
                        LED.OFF(Power_led)
                        mylcd.lcd_clear()
                        GPIO.cleanup()
                        MYSQL.END()
                        os.system("reboot")

                if GPIO.input(POWER_OFF_BUTTON)==0:
                        boucle = False
                        sleep(1)
                        BKL_LCD.ON(LCD)
                        mylcd.lcd_clear()
                        mylcd.lcd_display_string("Extinction du PC", 1)
                        mylcd.lcd_display_string("  en court...   ", 2)
                        sleep(2)
                        LED.OFF(Read_led)
                        LED.OFF(Ready_led)
                        LED.OFF(Power_led)
                        mylcd.lcd_clear()
                        GPIO.cleanup()
                        MYSQL.END()
                        os.system("shutdown now -h")
 
                if GPIO.input(PRG_END_BUTTON)==0:
                        boucle = False
                        sleep(1)
                        BKL_LCD.ON(LCD)
                        mylcd.lcd_clear()
                        mylcd.lcd_display_string("  Arret du prg  ", 1)
                        mylcd.lcd_display_string("  en court...   ", 2)
                        sleep(2)
                        fin()

                sleep(0.05)


# Création des threads pour les Boutons Power, Reset et PRG End
thread_1 = RPI_BT()

# Lancement des threads
thread_1.start()


############################
# Définition des fonctions #
############################

# Fonction qui arrete la lecture proprement 
def end_read(signal,frame):
    f = fin()
    
def fin():
    global continue_reading
    global boucle
    global Power_led
    global Read_led
    global Ready_led
    global Buzzer_1
    global mylcd
    continue_reading = False
    boucle = False
    mylcd.lcd_clear()
    BKL_LCD.ON(LCD)
    mylcd.lcd_display_string("Extinction...", 1)
    sleep(1)
    LED.OFF(Read_led)
    LED.OFF(Ready_led)
    if buzzer == True:
        BUZZER.ON(Buzzer_1)
    LED.ON(Power_led)
    sleep(0.1)
    BUZZER.OFF(Buzzer_1)
    LED.OFF(Power_led)
    sleep(0.2)
    if buzzer == True:
        BUZZER.ON(Buzzer_1)
    LED.ON(Power_led)
    sleep(0.1)
    BUZZER.OFF(Buzzer_1)
    LED.OFF(Power_led)
    sleep(0.2)
    if buzzer == True:
        BUZZER.ON(Buzzer_1)
    LED.ON(Power_led)
    sleep(0.1)
    BUZZER.OFF(Buzzer_1)
    LED.OFF(Power_led)
    sleep(0.2)
    if buzzer == True:
        BUZZER.ON(Buzzer_1)
    LED.ON(Power_led)
    sleep(0.5)
    BUZZER.OFF(Buzzer_1)
    LED.OFF(Power_led)
    mylcd.lcd_clear()
    BKL_LCD.OFF(LCD)
    GPIO.cleanup()
    MYSQL.END()
    sys.exit()

##################################
## Fonction Lecture de la carte ##
##################################

def lecture(quoi):
    global continue_reading
    global mylcd
    global boucle
    global Power_led
    global Read_led
    global Ready_led
    global Buzzer_1
    global La_Table
    global lecture_lcd
    global lcd_lecture
    if quoi == "UID":
        id = 0
    if quoi == "date_creation":
        id = 1
    if quoi == "nom":
        id = 2
    if quoi == "prenom":
        id = 4
    if quoi == "nr_client":
        id = 5
    if quoi == "points":
        id = 6
    if quoi == "date_visite":
        id = 8
    while continue_reading:

            # Detecter les tags
            (status,TagType) = RFID.MFRC522_Request(RFID.PICC_REQIDL)
            LED.OFF(Ready_led)
            LED.OFF(Read_led)
            sleep(0.1)
            LED.ON(Ready_led)

            # Une carte est detectee
            if status == RFID.MI_OK:
                #print ("Carte detectee")
                #mylcd.lcd_clear()
                #mylcd.lcd_display_string("Carte detectee", 1)
                #mylcd.lcd_display_string(MYSQL.Read_Instruction(La_Table), 2)
                lecture_lcd = True
                LED.ON(Read_led)
                LED.OFF(Ready_led)
                sleep(0.01)

            # Recuperation UID
            (status,uid) = RFID.MFRC522_Anticoll()

            if status == RFID.MI_OK:
                #print ("UID de la carte : "+str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3]))
                txt = str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3])
                MYSQL.Write(La_Table,txt,"UID")
                #mylcd.lcd_clear()
                #mylcd.lcd_display_string(str(uid[0])+"."+str(uid[1])+"."+str(uid[2])+"."+str(uid[3]), 2)
                # Clee d authentification par defaut
                key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

                # Selection du tag
                RFID.MFRC522_SelectTag(uid)

                # Authentification
                status = RFID.MFRC522_Auth(RFID.PICC_AUTHENT1A, id, key, uid)
                if lcd_lecture == False:
                    mylcd.lcd_clear()
                    mylcd.lcd_display_string("Lecture Carte...", 1)
                    lcd_lecture = True

                if status == RFID.MI_OK:
                    txt = str(RFID.MFRC522_Read(id))
                    RFID.MFRC522_StopCrypto1()
                    sleep(0.05)
                    MYSQL.Write(La_Table,txt,quoi)
                    break
                else:
                    #print ("Erreur d\'Authentification")
                    #mylcd.lcd_display_string("Lecture erronee", 2)
                    err_lcd = True
                    LED.OFF(Read_led)
                    LED.ON(Ready_led)
                    sleep(0.2)
                    LED.ON(Read_led)
                    LED.OFF(Ready_led)
                    sleep(0.2)
                    LED.OFF(Read_led)
                    LED.ON(Ready_led)
                    


            sleep(0.01)

    
######################
# Début du programme #
######################

# Allumer la LED Power
LED.ON(Power_led)
BKL_LCD.ON(LCD)
LCD_ON = True
LCD_IS_ON = True
LCD_timer = time.time()+LCD_Time_OUT
mylcd.lcd_clear()
mylcd.lcd_display_string("  Demarrage de  ", 1)
mylcd.lcd_display_string("BelSD CardReader", 2)
sleep(2)

if buzzer == True:
    BUZZER.ON(Buzzer_1)
    sleep(0.05)
    BUZZER.OFF(Buzzer_1)

MYSQL.Write(La_Table,"","UID")
MYSQL.Write(La_Table,"","date_creation")
MYSQL.Write(La_Table,"","nom")
MYSQL.Write(La_Table,"","prenom")
MYSQL.Write(La_Table,"","nr_client")
MYSQL.Write(La_Table,"","points")
MYSQL.Write(La_Table,"","date_visite")

    
signal.signal(signal.SIGINT, end_read)
RFID = BelSD_RFID.MFRC522()

err_lcd = False
lecture_lcd = False
read_ok = False
lcd_lecture = False

instruction = MYSQL.Write(La_Table,BASE_CFG.Client_Name(),"instruction")

while boucle:
    instruction = MYSQL.Read_Instruction(La_Table)
    if time.time()>LCD_timer and LCD_IS_ON == True:
        BKL_LCD.OFF(LCD)
        LCD_IS_ON = False
    mylcd.lcd_display_string(instruction, 1)
    mylcd.lcd_display_string(time.strftime("%H:%M %d/%m/%Y"), 2)
    if instruction == 'stop':
        a = fin()
    if instruction == 'Attente carte...': 
        mylcd.lcd_clear()
        BKL_LCD.ON(LCD)
        LCD_IS_ON = True
        MYSQL.Write(La_Table,"Lecture...","instruction")
        mylcd.lcd_display_string("Attente carte...", 1)
        mylcd.lcd_display_string(time.strftime("%H:%M %d/%m/%Y"), 2)
        LED.ON(Ready_led)
        LED.OFF(Read_led)
        lecture("UID")
        lecture("date_creation")
        lecture("nom")
        lecture("prenom")
        lecture("nr_client")
        lecture("points")
        lecture("date_visite")
        lcd_lecture = False
        LED.OFF(Read_led)
        LED.OFF(Ready_led)
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Lecture terminee", 1)
        if buzzer == True:
            BUZZER.ON(Buzzer_1)
        sleep(1)
        BUZZER.OFF(Buzzer_1)
        LCD_timer = time.time()+LCD_Time_OUT
        sleep(2)
        mylcd.lcd_clear()
        MYSQL.Write(La_Table,"   Jessynails   ","instruction")
        read_ok = True
    
    if read_ok == False:
        sleep(1)
    else:
        read_ok = False
