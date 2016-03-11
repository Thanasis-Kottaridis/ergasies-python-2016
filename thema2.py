pinakas =["0","1","2","3","4","5","6","7","8","9"]
player1 = [[2,"a"],[2,"b"],[2,"c"]]
player2 = [[2,"x"],[2,"y"],[2,"z"]]
p1=["a","b","c"]
p2=["x","y","z"]
def board():
    print "|"+pinakas[1]+"|"+pinakas[2]+"|"+pinakas[3]+"|"
    print "-------"
    print "|"+pinakas[4]+"|"+pinakas[5]+"|"+pinakas[6]+"|"
    print "-------"
    print "|"+pinakas[7]+"|"+pinakas[8]+"|"+pinakas[9]+"|"
def win(x):
        if pinakas[1] in x and pinakas[2] in x and pinakas[3] in x:
            return 1
        elif pinakas[4] in x and pinakas[5] in x and pinakas[6] in x:
            return 1
        elif pinakas[7] in x and pinakas[8] in x and pinakas[9] in x:
            return 1
        elif pinakas[1] in x and pinakas[4] in x and pinakas[7] in x:
            return 1
        elif pinakas[3] in x and pinakas[6] in x and pinakas[9] in x:
            return 1
        elif pinakas[2] in x and pinakas[5] in x and pinakas[8] in x:
            return 1
        elif pinakas[1] in x and pinakas[5] in x and pinakas[9] in x:
            return 1
        elif pinakas[3] in x and pinakas[5] in x and pinakas[7] in x:
            return 1
        elif pinakas[1] != "1" and pinakas[2]!="2" and pinakas[3]!="3"and pinakas[4]!="4"and pinakas[5] != 5 and pinakas[6]!="6"and pinakas[7]!="7"and pinakas[8]!="8"and pinakas[9]!="9":
            return 0
        else:
            return -1

        pass
def reset():
    pinakas[1]="1"
    pinakas[2]="2"
    pinakas[3]="3"
    pinakas[4]="4"
    pinakas[5]="5"
    pinakas[6]="6"
    pinakas[7]="7"
    pinakas[8]="8"
    pinakas[9]="9"
playagean="y"
while playagean=="y":
    player=player1
    i = -1
    while i==-1:
        board()
        corect=0
        while corect==0:
            if player==player1:
                print p1,"paizi"
                pioni= raw_input("ti poioni thes?(megalo,meseo,mikro)")
                if pioni == "megalo" and player1[2][0]!=0:
                    grapse=player1[2][1]
                    player1[2][0]-=1
                    kouti=raw_input("pou to vazis?")
                    if kouti == "1" and pinakas[1]=="1" or kouti =="1"and pinakas[1]!=player2[2][1]:
                        pinakas[1]=grapse
                        corect=1
                    elif kouti == "2" and pinakas[2]=="2" or kouti =="2"and pinakas[2]!=player2[2][1]:
                        pinakas[2]=grapse
                        corect=1
                    elif kouti == "3" and pinakas[3]=="3" or kouti =="3"and pinakas[3]!=player2[2][1]:
                        pinakas[3]=grapse
                        corect=1
                    elif kouti == "4" and pinakas[4]=="4" or kouti =="4"and pinakas[4]!=player2[2][1]:
                        pinakas[4]=grapse
                        corect=1
                    elif kouti == "5" and pinakas[5]=="5" or kouti =="5"and pinakas[5]!=player2[2][1]:
                        pinakas[5]=grapse
                        corect=1
                    elif kouti == "6" and pinakas[6]=="6" or kouti =="6"and pinakas[6]!=player2[2][1]:
                        pinakas[6]=grapse
                        corect=1
                    elif kouti == "7" and pinakas[7]=="7" or kouti =="7"and pinakas[7]!=player2[2][1]:
                        pinakas[7]=grapse
                        corect=1
                    elif kouti == "8" and pinakas[8]=="8" or kouti =="8"and pinakas[8]!=player2[2][1]:
                        pinakas[8]=grapse
                        corect=1
                    elif kouti == "9" and pinakas[9]=="9" or kouti =="9"and pinakas[9]!=player2[2][1]:
                        pinakas[9]=grapse
                        corect=1
                    else:
                        print "lathos kinisi"
                elif pioni == "meseo" and player1[1][0]!=0:
                    grapse=player1[1][1]
                    player1[1][0]-=1
                    kouti=raw_input("pou to vazis?")
                    if kouti == "1" and pinakas[1]=="1" or kouti =="1"and pinakas[1]!=player2[2][1] or kouti=="1" and pinakas[1]!=player2[1][1]:
                        pinakas[1]=grapse
                        corect=1
                    elif kouti == "2" and pinakas[2]=="2" or kouti =="2"and pinakas[2]!=player2[2][1] or kouti=="2" and pinakas[2]!=player2[1][1]:
                        pinakas[2]=grapse
                        corect=1
                    elif kouti == "3" and pinakas[3]=="3" or kouti =="3"and pinakas[3]!=player2[2][1] or kouti=="3" and pinakas[3]!=player2[1][1]:
                        pinakas[3]=grapse
                        corect=1
                    elif kouti == "4" and pinakas[4]=="4" or kouti =="4"and pinakas[4]!=player2[2][1] or kouti=="4" and pinakas[4]!=player2[1][1]:
                        pinakas[4]=grapse
                        corect=1
                    elif kouti == "5" and pinakas[5]=="5" or kouti =="5"and pinakas[5]!=player2[2][1] or kouti=="5" and pinakas[5]!=player2[1][1]:
                        pinakas[5]=grapse
                        corect=1
                    elif kouti == "6" and pinakas[6]=="6" or kouti =="6"and pinakas[6]!=player2[2][1] or kouti=="6" and pinakas[6]!=player2[1][1]:
                        pinakas[6]=grapse
                        corect=1
                    elif kouti == "7" and pinakas[7]=="7" or kouti =="7"and pinakas[7]!=player2[2][1] or kouti=="7" and pinakas[7]!=player2[1][1]:
                        pinakas[7]=grapse
                        corect=1
                    elif kouti == "8" and pinakas[8]=="8" or kouti =="8"and pinakas[8]!=player2[2][1] or kouti=="8" and pinakas[8]!=player2[1][1]:
                        pinakas[8]=grapse
                        corect=1
                    elif kouti == "9" and pinakas[9]=="9" or kouti =="8"and pinakas[9]!=player2[2][1] or kouti=="9" and pinakas[9]!=player2[1][1]:
                        pinakas[9]=grapse
                        corect=1
                    else:
                        print "lathos kinisi"
                elif pioni == "mikro" and player1[0][0]!=0:
                    grapse=player1[0][1]
                    player1[0][0]-=1
                    kouti=raw_input("pou to vazis?")
                    if kouti == "1" and pinakas[1]=="1":
                        pinakas[1]=grapse
                        corect=1
                    elif kouti == "2" and pinakas[2]=="2":
                        pinakas[2]=grapse
                        corect=1
                    elif kouti == "3" and pinakas[3]=="3":
                        pinakas[3]=grapse
                        corect=1
                    elif kouti == "4" and pinakas[4]=="4":
                        pinakas[4]=grapse
                        corect=1
                    elif kouti == "5" and pinakas[5]=="5":
                        pinakas[5]=grapse
                        corect=1
                    elif kouti == "6" and pinakas[6]=="6":
                        pinakas[6]=grapse
                        corect=1
                    elif kouti == "7" and pinakas[7]=="7":
                        pinakas[7]=grapse
                        corect=1
                    elif kouti == "8" and pinakas[8]=="8":
                        pinakas[8]=grapse
                        corect=1
                    elif kouti == "9" and pinakas[9]=="9":
                        pinakas[9]=grapse
                        corect=1
                    else:
                        print "lathos kinisi"
                else:
                    print "den iparxoun diathesima pionia"
                i=win(p1)
            else:
                print p2,"paizi"
                pioni= raw_input("ti poioni thes?")
                if pioni == "megalo" and player2[2][0]!=0:
                    grapse=player2[2][1]
                    player2[2][0]-=1
                    kouti=raw_input("pou to vazis?")
                    if kouti == "1" and pinakas[1]=="1" or kouti =="1"and pinakas[1]!=player1[2][1]:
                        pinakas[1]=grapse
                        corect=1
                    elif kouti == "2" and pinakas[2]=="2" or kouti =="2"and pinakas[2]!=player1[2][1]:
                        pinakas[2]=grapse
                        corect=1
                    elif kouti == "3" and pinakas[3]=="3" or kouti =="3"and pinakas[3]!=player1[2][1]:
                        pinakas[3]=grapse
                        corect=1
                    elif kouti == "4" and pinakas[4]=="4" or kouti =="4"and pinakas[4]!=player1[2][1]:
                        pinakas[4]=grapse
                        corect=1
                    elif kouti == "5" and pinakas[5]=="5" or kouti =="5"and pinakas[5]!=player1[2][1]:
                        pinakas[5]=grapse
                        corect=1
                    elif kouti == "6" and pinakas[6]=="6" or kouti =="6"and pinakas[6]!=player1[2][1]:
                        pinakas[6]=grapse
                        corect=1
                    elif kouti == "7" and pinakas[7]=="7" or kouti =="7"and pinakas[7]!=player1[2][1]:
                        pinakas[7]=grapse
                        corect=1
                    elif kouti == "8" and pinakas[8]=="8" or kouti =="8"and pinakas[8]!=player1[2][1]:
                        pinakas[8]=grapse
                        corect=1
                    elif kouti == "9" and pinakas[9]=="9" or kouti =="9"and pinakas[9]!=player1[2][1]:
                        pinakas[9]=grapse
                        corect=1
                    else:
                        print "lathos kinisi"
                elif pioni == "meseo" and player2[1][0]!=0:
                    grapse=player2[1][1]
                    player2[1][0]-=1
                    kouti=raw_input("pou to vazis?")
                    if kouti == "1" and pinakas[1]=="1" or kouti =="1"and pinakas[1]!=player1[2][1] or kouti=="1" and pinakas[1]!=player1[1][1]:
                        pinakas[1]=grapse
                        corect=1
                    elif kouti == "2" and pinakas[2]=="2" or kouti =="2"and pinakas[2]!=player1[2][1] or kouti=="2" and pinakas[2]!=player1[1][1]:
                        pinakas[2]=grapse
                        corect=1
                    elif kouti == "3" and pinakas[3]=="3" or kouti =="3"and pinakas[3]!=player1[2][1] or kouti=="3" and pinakas[3]!=player1[1][1]:
                        pinakas[3]=grapse
                        corect=1
                    elif kouti == "4" and pinakas[4]=="4" or kouti =="4"and pinakas[4]!=player1[2][1] or kouti=="4" and pinakas[4]!=player1[1][1]:
                        pinakas[4]=grapse
                        corect=1
                    elif kouti == "5" and pinakas[5]=="5" or kouti =="5"and pinakas[5]!=player1[2][1] or kouti=="5" and pinakas[5]!=player1[1][1]:
                        pinakas[5]=grapse
                        corect=1
                    elif kouti == "6" and pinakas[6]=="6" or kouti =="6"and pinakas[6]!=player1[2][1] or kouti=="6" and pinakas[6]!=player1[1][1]:
                        pinakas[6]=grapse
                        corect=1
                    elif kouti == "7" and pinakas[7]=="7" or kouti =="7"and pinakas[7]!=player1[2][1] or kouti=="7" and pinakas[7]!=player1[1][1]:
                        pinakas[7]=grapse
                        corect=1
                    elif kouti == "8" and pinakas[8]=="8" or kouti =="8"and pinakas[8]!=player1[2][1] or kouti=="8" and pinakas[8]!=player1[1][1]:
                        pinakas[8]=grapse
                        corect=1
                    elif kouti == "9" and pinakas[9]=="9" or kouti =="9"and pinakas[9]!=player1[2][1] or kouti=="9" and pinakas[9]!=player1[1][1]:
                        pinakas[9]=grapse
                        corect=1
                    else:
                        print "lathos kinisi"
                elif pioni == "mikro" and player2[0][0]!=0:
                        grapse=player2[0][1]
                        player2[0][0]-=1
                        kouti=raw_input("pou to vazis?")
                        if kouti == "1" and pinakas[1]=="1":
                            pinakas[1]=grapse
                        elif kouti == "2" and pinakas[2]=="2":
                            pinakas[2]=grapse
                            corect=1
                        elif kouti == "3" and pinakas[3]=="3":
                            pinakas[3]=grapse
                            corect=1
                        elif kouti == "4" and pinakas[4]=="4":
                            pinakas[4]=grapse
                            corect=1
                        elif kouti == "5" and pinakas[5]=="5":
                            pinakas[5]=grapse
                            corect=1
                        elif kouti == "6" and pinakas[6]=="6":
                            pinakas[6]=grapse
                            corect=1
                        elif kouti == "7" and pinakas[7]=="7":
                            pinakas[7]=grapse
                            corect=1
                        elif kouti == "8" and pinakas[8]=="8":
                            pinakas[8]=grapse
                            corect=1
                        elif kouti == "9" and pinakas[9]=="9":
                            pinakas[9]=grapse
                            corect=1
                        else:
                            print "lathos kinisi"
                else:
                    print "den iparxoun diathesima pionia"
                i=win(p2)
                pass

        if player==player1 and i==-1:
            player=player2
        elif player==player2 and i==-1:
            player=player1
            pass
    if i==1:
        board()
        print "o paixtis",player,"einai o nikitis."
    else:
        board()
        print "isopalia"
    playagean= raw_input("thes na pai3is pali?")
    if playagean=="y":
         print "den ta paratas vlepo"
         reset()
    else:
        print "popo mia kotoula :P"
    pass
#print player1,player2
#board()
raw_input()
