import random

round_num = 1000000                                                 # 總回合數
Captial  = 0          #10000                                        # 初始資金 ,0最後計算期望值比較方便
Earnings = 0                                                        # 獲利
Bet = 100                                                           # 賭金
Double = 1
Hi_Lo = 0                                                           # Hi-Lo算牌策略
Win_num  = 0                                                        # 計算勝利次數
Lose_num = 0                                                        # 計算輸的次數
Draw_num = 0
P_21points_num = 0
P_5Cards_num = 0

Player_points = 0                                                   # 玩家目前的數字總和(A = 1)
Player_points_withA = 0                                             # 當玩家有A時(A = 11)時的數字總和

Dealer_points       = 0                                             # 莊家目前的數字總和(A = 1)
Dealer_points_withA = 0                                             # 當莊家有A時(A = 11)時的數字總和

Poker = ['♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K','♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K','♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K','♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K']                                                   #定義一副撲克牌
Deck = 1                                                            # 牌組數

Poker_Convert = {
    "♣A" :  1 , "♦A" :  1, "♥A" :  1, "♠A" :  1,
    "♣2" :  2 , "♦2" :  2, "♥2" :  2, "♠2" :  2,
    "♣3" :  3 , "♦3" :  3, "♥3" :  3, "♠3" :  3,
    "♣4" :  4 , "♦4" :  4, "♥4" :  4, "♠4" :  4,
    "♣5" :  5 , "♦5" :  5, "♥5" :  5, "♠5" :  5,
    "♣6" :  6 , "♦6" :  6, "♥6" :  6, "♠6" :  6,
    "♣7" :  7 , "♦7" :  7, "♥7" :  7, "♠7" :  7,
    "♣8" :  8 , "♦8" :  8, "♥8" :  8, "♠8" :  8,
    "♣9" :  9 , "♦9" :  9, "♥9" :  9, "♠9" :  9,
    "♣10":  10, "♦10":  10,"♥10":  10,"♠10":  10,
    "♣J" :  10, "♦J" :  10,"♥J" :  10,"♠J" :  10,
    "♣Q" :  10, "♦Q" :  10,"♥Q" :  10,"♠Q" :  10,
    "♣K" :  10, "♦K" :  10,"♥K" :  10,"♠K" :  10,  0 : 0
}                                                                                       # 翻譯撲克牌點數



class BlackJack_Bet:                                            #定義賭金與選項的模組
    def __init__(self ,option ,bet):
        self.option = option
        self.bet = bet

Player_Bet = BlackJack_Bet
Player_Bet.bet = Bet
Player_Bet.option = 1

#Shuffle_Poker = random.sample(Poker *Deck,k= 52 *Deck)              # 進行一次洗牌
#print(str(Shuffle_Poker) + "\n")                                    # 顯示發牌順序做驗算

Player_poker = []
Dealer_poker = []

Shuffle_Poker = random.sample(Poker * Deck, k=50 * Deck)
print(str(Shuffle_Poker) + "\n")

#建立欄位表
print('%-12s'% "Round" + '%-40s'% "Player's Cards" +  '%-40s' % "Dealer's Cards" + '%-13s'% "Bets" + '%-25s'% "Captials(Casual)"  + '%-25s'%  "Win Ratio" + '%-18s'% "21Points" + '%-16s'% "5 Cards" + '%-18s'% "Expected value")


round = 1
n = 0
P_Bust = False
P_5Cards = False


while round <= round_num:
    Player_poker.clear()                                                                            # 全部重置為0
    Dealer_poker.clear()
    P_Bust, D_Bust, P_5Cards, P_Stop, P_Double = False, False, False , False , False                # 爆牌 五龍 停牌 Flag全歸0
    P_21points, D_21points = False, False
    Player_points_withA,  Dealer_points_withA = 0, 0
    Double = 1
    i, j = 0, 0

    Player_poker.append(random.choice(Poker))           #Shuffle_Poker[n + 0])   #random.choice(Poker) 隨機撲克牌
    Dealer_poker.append(random.choice(Poker))           #Shuffle_Poker[n + 1])
    Player_poker.append(random.choice(Poker))           #Shuffle_Poker[n + 2])
    Dealer_poker.append(random.choice(Poker))           #Shuffle_Poker[n + 3])

    n += 3


    Player_points = Poker_Convert.get(Player_poker[0]) + Poker_Convert.get(Player_poker[1])
    Dealer_points = Poker_Convert.get(Dealer_poker[0]) + Poker_Convert.get(Dealer_poker[1])
    if '♣A' in Player_poker  or '♦A' in Player_poker  or '♥A' in Player_poker  or '♠A' in Player_poker:                           #判定玩家牌是否有A
        Player_points_withA = Player_points +10


    if '♣A' in Dealer_poker  or '♦A' in Dealer_poker  or '♥A' in Dealer_poker  or '♠A' in Dealer_poker:                           #判定莊家牌是否有A
        Dealer_points_withA = Dealer_points +10



    #print('%-8s' % str(round) + " P:" + '%-25s' % str(Player_poker) + "(" + '%-2s' % str(Player_points_withA) + "/" + '%-2s' % str(Player_points) + '%-8s' % ") " + "D:" + '%-25s' % str(Dealer_poker) + "(" + '%-2s' % str(Dealer_points_withA) + "/" + '%-2s' % str(Dealer_points)  + '%-11s' % ")" + "$" + '%-20s' % str(Bet) )  # + "$" + '%-27s' % str(Captial)
    print('%-9s' % str(round) + "P:" + '%-25s' % str(Player_poker) + "(" + '%-2s' % str(Player_points_withA) + "/" + '%-2s' % str(Player_points) + '%-8s' % ") " + "D:[' ?', '" + '%-2s' % str(Dealer_poker[1]) + '%-15s' % "']" + "(" + '%-2s' % str(Poker_Convert.get(Dealer_poker[1])) + '%-12s' % ")")    #+ "$" + '%-20s' % str(Bet)
    if Player_points_withA == 21:
        Player_points = Player_points_withA
        P_21points = True
    elif Player_points_withA >= 17:
        Player_points = Player_points_withA

    if Dealer_points_withA == 21:
        Dealer_points = Dealer_points_withA
        print('%-50s' % " " + "D:" + '%-25s' % str(Dealer_poker) + "(" + '%-2s' % str(Dealer_points) + '%-11s' % ")")
        D_21points = True
    elif Dealer_points_withA >= 17:
        Dealer_points = Dealer_points_withA




    #玩家補牌
    if 1 < Poker_Convert.get(Dealer_poker[1]) < 7 and 11 < Player_points < 17:                  #若莊家明牌<6點 則玩家不加牌
        P_Stop = True # 勝率提高到47.17%(從46.2%) 期望值:+0.0024 ~+ 0.0004


    while Player_points < 17 and Player_points_withA < 17 and not(D_21points) and not(P_5Cards) and not(P_Stop) and not(P_Double):
        if  i == 0 and   10 <= Player_points <= 11 and  1 < Poker_Convert.get(Dealer_poker[1]) < 10 :
            Double = 2
            P_Double = True
        Player_poker.append(random.choice(Poker))   #Shuffle_Poker[n + 1]   random.choice(Poker)
        Player_points += Poker_Convert.get(Player_poker[2+i])
        if '♣A' in Player_poker  or '♦A' in Player_poker  or '♥A'in Player_poker  or '♠A'in Player_poker:           #判定是否有A的牌型 有則+10
            Player_points_withA = Player_points + 10
            if  Player_points_withA > 21:                                      #如果有A牌型 但超過21 則回復原本牌點(-10)
                Player_points_withA = Player_points
            elif Player_points_withA <= 21:                                    #如果有A牌型 小於21  則保留A牌型點數(+10)
                Player_points = Player_points_withA
        if Player_points_withA >= 17:
                Player_points = Player_points_withA

        if Player_points > 21:  # 判定玩家是否爆牌
            P_Bust = True
        elif i == 2 and Player_points <= 21:  # 判定玩家過五關
            P_5Cards = True


        #if 1 < Poker_Convert.get(Dealer_poker[1]) < 6 and Player_points >= 12:  # 若莊家明牌<6點 則玩家不加牌
            #P_Stop = True #加入這行 勝率(47.38%)變高 但期望值(-0.0028)變低

        print('%-9s'% "" +"P:" + '%-25s'% str(Player_poker) + "(" +'%-2s'% str(Player_points) + ")" )
        i += 1
        n += 1


    if 21 > Dealer_points >= 17:
        print('%-50s' % " " + "D:" + '%-25s' % str(Dealer_poker) + "(" + '%-2s' % str(Dealer_points) + '%-11s' % ")")

    #莊家不足17點補牌
    while Dealer_points < 17 and Dealer_points_withA < 17 and not(P_Bust) and not(P_21points) and not(D_21points) and not(P_5Cards):
        Dealer_poker.append(random.choice(Poker))       #Shuffle_Poker[n + 1]
        Dealer_points += Poker_Convert.get(Dealer_poker[2+j])
        if '♣A' in Dealer_poker  or '♦A' in Dealer_poker  or '♥A'in Dealer_poker  or '♠A'in Dealer_poker:
            Dealer_points_withA = Dealer_points + 10
            if  Dealer_points_withA > 21:                                      #如果有A牌型 但超過21 則回復原本牌點(-10)
                Dealer_points_withA = Dealer_points
            elif Dealer_points_withA <= 21:                                    #如果有A牌型 小於21   則保留A牌型點數(+10)
                Dealer_points = Dealer_points_withA

        print('%-50s' % "  " + "D:" + '%-25s'% str(Dealer_poker) + "(" + '%-2s' % str(Dealer_points) + ")")
        j += 1
        n += 1
        if Dealer_points > 21:
            D_Bust = True
        else:
            D_Bust = False




    #判定勝負
    if P_21points and D_21points:
        print("Both get BlackJack ! (Draw...)")
        Draw_num += 1
    elif P_21points and not(D_21points) :
        print("Player gets BlackJack ! (WIN!)")
        P_21points_num += 1
        Earnings += Bet * 1.5  # BlackJack可以得到1.5倍 賭金
        Win_num += 1
    elif D_21points and not(P_21points):
        print("Dealer gets BlackJack ! (Lose...)")
        Earnings -= Bet
        Lose_num += 1
    elif P_5Cards :
        print("Player gets five card Charlie! (WIN!)")
        P_5Cards_num += 1
        Earnings += Bet* 3
        Win_num += 1
    elif P_Bust:                                            #勝負判斷
        print("Player Busts...(LOSE...)")
        Earnings -= Bet *Double
        Lose_num += 1
    elif D_Bust:
        print("Dealer Busts...(WIN!)")
        Earnings += Bet *Double
        Win_num += 1
    elif Dealer_points >  Player_points:
        print("Dealer gets bigger points (LOSE...)")
        Earnings -= Bet *Double
        Lose_num += 1
    elif Dealer_points == Player_points:
        print("Same points... (DRAW...)")
        Draw_num += 1
    elif Dealer_points <  Player_points:
        print("Player gets  bigger points (WIN!)")
        Earnings += Bet *Double
        Win_num += 1
    else:
        break

    Expected_Value  = (Win_num *1 + P_21points_num *0.5 + P_5Cards_num *2 - Lose_num *1) / (round-Draw_num)
    Expected_Value2 = (Captial + Earnings)/round

    if  Draw_num == round:
        print( '%-92s' % " " + "$" + '%-17s' % str(Bet * Double) + "$" + '%-17s' % str(Captial + Earnings) + str(Win_num) + "W/" + str(Draw_num) + "/" + str(Lose_num) + "L " + "(" + '%.4f' % float(Win_num /round) + ")" )
    else:
        print( '%-92s' % " " + "$" + '%-17s' % str(Bet * Double) + "$" + '%-17s' % str(Captial + Earnings) + str(Win_num) + "W/" + str(Draw_num) + "/" + str(Lose_num) + "L " + "(" + '%.4f' % float(Win_num/(round-Draw_num) * 100) + '%-15s' % "%)" + '%-18s' % str(P_21points_num) + '%-16s' % str(P_5Cards_num) + '%.4f' % float(Expected_Value2))
        
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    round += 1
    n += 1

