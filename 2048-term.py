#!/bin/env python

# Coded by @AbirHasan2005
# If you are using any codes from here than must give me credits.
# My Hard Work. So Credits are must.

# Telegram Group: http://t.me/linux_repo
# Join Telegram Group for feedback, help and chat.

# Small Python3 coded game. No need to install any extra python module.
# Don't edit anything. Read LICENSE before everything.
# If you want to edit anything than first ask in Telegram Group.

# ============================================================================

# Imports:
import os
from random import randint
from copy import deepcopy


ll=[0]*4
l=[]
for i in range(4):
    l.append(ll[:])
score=0

def printl():
    global l
    global score
    print('\033[1;95m')
    print('===============[\033[1;94m2048\033[1;95m]===============')
    print('=========[\033[1;96mby AbirHasan2005\033[1;95m]=========')
    print('\033[1;93mScore:''{:30d}'.format(score))
    print('\033[1;92m')
    print('┌──────────────────────────────────┐')
    for i in range(4):
        print('│                                  │')
        pts='│ '
        for j in range(4):
            pts+='{:^8d}'.format(l[i][j])
        pts+=' │'
        print(pts)
    print('└──────────────────────────────────┘')

def randnum():
    global l
    rl=[]
    
    for i in range(4):
        for j in range(4):
            if l[i][j]==0:
                rl.append((i,j))
    if len(rl)>0:
        i,j=rl[randint(0,len(rl)-1)]
        l[i][j]=randint(1,2)*2

def left():
    global score
    global l
    for i in range(4):
        for j in range(3):
            for k in range(j+1,4):
                if l[i][k]!=0:
                    if l[i][j]==0:
                        l[i][j],l[i][k]=l[i][k],l[i][j]
                    elif l[i][j]==l[i][k]:
                        l[i][j]*=2
                        l[i][k]=0
                        score+=l[i][j]
                        break
                    else:
                        break

def up():
    global score
    global l
    for i in range(4):
        for j in range(3):
            for k in range(j+1,4):
                if l[k][i]!=0:
                    if l[j][i]==0:
                        l[j][i],l[k][i]=l[k][i],l[j][i]
                    elif l[j][i]==l[k][i]:
                        l[j][i]*=2
                        l[k][i]=0
                        score+=l[j][i]
                        break
                    else:
                        break

randnum()
randnum()

while True:
    printl()
    s=input('\033[1;96mInput: ').upper()
    os.system("clear")
    lt=deepcopy(l)
    if s=='E':
        break
    elif s=='A':
        left()
    elif s=='D':
        for i in range(4):
            l[i].reverse()
        left()
        for i in range(4):
            l[i].reverse()
    elif s=='W':
        up()
    elif s=='S':
        for i in range(4):
            for j in range(2):
                l[j][i],l[3-j][i]=l[3-j][i],l[j][i]
        up()
        for i in range(4):
            for j in range(2):
                l[j][i],l[3-j][i]=l[3-j][i],l[j][i]
    else:
        print('\n\033[1;91mWASD to move, E to exit')
    if lt!=l:
        randnum()

# ============================================================================

# I know that this game is very hard to operate.
# But a new version of this game is coming soon.

# ============================================================================

# If you find any problems than please report in my Telegram Group
# My Telegram Group: http://t.me/linux_repo
