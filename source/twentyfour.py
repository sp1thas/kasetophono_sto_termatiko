# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#               twentyfour
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

from termcolor import colored
import playlist, home, exit, menu

def ListMenu():
    title = '24ωρο'
    CurrentMenu = menu.Menu(title)
    options =   [
                    {"name":"Πρωί","function":Morning},
                    {"name":"Μεσημέρι","function":Noon},
                    {"name":"Απόγευμα","function":AfterNoon},
                    {"name":"Νύχτα","function":Night},
                    {"name":colored("Home Menu","yellow"),"function":home.ListMenu},
                    {"name":colored("Έξοδος", "red"),"function":exit.exit}
                ]
    CurrentMenu.addOptions(options)
    CurrentMenu.open()

def Morning():
    playlist.FullList('Morning', 'twentyfour.ListMenu()')
def Noon():
    playlist.FullList('Noon', 'twentyfour.ListMenu()')
def AfterNoon():
    playlist.FullList('AfterNoon', 'twentyfour.ListMenu()')
def Night():
    playlist.FullList('Night', 'twentyfour.ListMenu()')
