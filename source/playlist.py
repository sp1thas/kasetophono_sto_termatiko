# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#               playlist
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

from termcolor import colored
from subprocess import call
import AllPlaylists, menu, home,exit, time, ksena, categories, lovers, mood, twentyfour, greek

'''
    FullList returns a dict.
    Dictionary structure:
    ['playlist label name','playlist youtube id', ]
'''

def FullList(category, *ParentMenuFunc):
    print 'Οι playlist που υπάρχουν προς το παρόν ;\n'
    counter = 0
    FinalPlaylist = AllPlaylists.GetThem(category)

    # for i in allPlaylists:
    #     if allPlaylists[i][2] == category or allPlaylists[i][3] == category or allPlaylists[i][4] == category or allPlaylists[i][5]==category or allPlaylists[i][6] == category or allPlaylists[i][7]==category or allPlaylists[i][8]==category:
    #         counter += 1
    #         FinalPlaylist[i] = [allPlaylists[i][0], allPlaylists[i][1]]
    #         print counter,".",FinalPlaylist[i][0]
    #         FinalPlaylist[counter] = FinalPlaylist.pop(i)
    #         time.sleep(0.02)

    for i in FinalPlaylist:
        counter += 1
        if len(str(counter))==1:
            OutputStr = " "+str(counter)+". "+FinalPlaylist[i][0]
        else:
            OutputStr = str(counter)+". "+FinalPlaylist[i][0]
        print OutputStr
        time.sleep(0.1)
    if ParentMenuFunc:
        OutputStr = str(len(FinalPlaylist)+1)+". "+"Previous Menu"
        div = len(OutputStr) + 2
        print colored(OutputStr, "green")
        OutputStr1 = str(len(FinalPlaylist)+2)+". "+"Home Menu"
        div = len(OutputStr1) + 2
        print colored(OutputStr1,"yellow")
    else:
        OutputStr1 = str(len(FinalPlaylist)+1)+". "+"Home Menu"
        div = len(OutputStr1) + 2
        print colored(OutputStr1,"yellow")
    select = -1

    select = input("Επιλέξτε λίστα (για έξοδο δώστε 0)\n>>> ")
    if select == len(FinalPlaylist)+1:
        eval(*ParentMenuFunc)
    elif select == len(FinalPlaylist)+2:
        home.ListMenu()
    elif (select > 0 & select <len(FinalPlaylist)+1):
        Play(FinalPlaylist[select][1])
    elif select == 0:
        exit.exit()



def Play(id):

    IDwithArgus = id + ",dump,all"
    call(["mpsyt", "pl", IDwithArgus])
