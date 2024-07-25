import random


Poker = tuple(['♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣T','♣J','♣Q','♣K','♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦T','♦J','♦Q','♦K','♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥T','♥J','♥Q','♥K','♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠T','♠J','♠Q','♠K'])
Poker_Convert = {"♣A": 1,"♦A": 1,"♥A": 1,"♠A": 1,"♣2": 2,"♦2": 2,"♥2": 2,"♠2": 2,"♣3": 3,"♦3": 3,"♥3": 3,"♠3": 3,"♣4": 4,"♦4": 4,"♥4": 4,"♠4": 4,"♣5": 5,"♦5": 5,"♥5": 5,"♠5": 5,"♣6": 6,"♦6": 6,"♥6": 6,"♠6": 6,"♣7": 7,"♦7": 7,"♥7": 7,"♠7": 7,"♣8": 8,"♦8": 8,"♥8": 8,"♠8": 8,"♣9": 9,"♦9": 9,"♥9": 9,"♠9": 9,"♣T":10,"♦T":10,"♥T":10,"♠T":10,"♣J": 10,"♦J": 10,"♥J": 10,"♠J": 10,"♣Q": 10,"♦Q": 10,"♥Q": 10,"♠Q": 10,"♣K": 10,"♦K": 10,"♥K": 10,"♠K": 10, 0: 0,'⧭A': 1}                                                                                       #翻譯撲克牌點數
#翻譯撲克牌點數



class BlackJack_Bet:                                            #定義賭金與選項的模組
    def __init__(self ,option ,bet):
        self.option = option
        self.bet = bet


def Shuffle(Deck = 1):
    return random.sample(Poker * Deck,k=52 * Deck)


def Deal(Card_list, Card_all, poker_num):
    for _ in range(poker_num):
        Card_list.append(Card_all.pop(0))
    return Card_list, Card_all


def Card_Point(Card_list):
    poker_point = 0
    for i in range(len(Card_list)):
        poker_point += Poker_Convert.get(Card_list[i])
    return poker_point


def Card_with_A(Card_list, Card_Point):
    for poker in (Card_list):
        if Poker_Convert.get(poker) == 1:
            return Card_Point + 10
        else:
            return 0



def Point21(One_State):
    if One_State[2] == 21:  # 如果玩家點數 21點 將'21點'狀態 = True
        One_State[1] = One_State[2]
        One_State[3] = True

    elif One_State[2] >= 17:  # 如果玩家點數 超過17點 將'停牌'狀態 = True
        One_State[1] = One_State[2]
        One_State[6] = True

    return One_State



def Game_Result(Game_Statistics, Player_State, Dealer_State, Capital_Statistics, Show_Process=True):

    if Player_State[3] and Dealer_State[3]:
        if Show_Process:
            print("Both get BlackJack ! (Draw...)")
        Game_Statistics[1] += 1

    elif Player_State[3] and not (Dealer_State[3]):
        if Show_Process:
            print("Player gets BlackJack ! (WIN!)")
        Game_Statistics[3] += 1
        Capital_Statistics[1] += Capital_Statistics[2] * 1.5  # BlackJack可以得到1.5倍 賭金
        Game_Statistics[0] += 1

    elif Dealer_State[3] and not (Player_State[3]):
        if Show_Process:
            print("Dealer gets BlackJack ! (Lose...)")
        Capital_Statistics[1] -= Capital_Statistics[2]
        Game_Statistics[2] += 1

    elif Player_State[5]:
        if Show_Process:
            print("Player gets five card Charlie! (WIN!)")
        Game_Statistics[4] += 1
        Capital_Statistics[1] += Capital_Statistics[2] * 3
        Game_Statistics[0] += 1

    elif Player_State[4]:  # 勝負判斷
        if Show_Process:
            print("Player Busts...(LOSE...)")
        Capital_Statistics[1] -= Capital_Statistics[2] * Capital_Statistics[3]
        Game_Statistics[2] += 1

    elif Dealer_State[4]:
        if Show_Process:
            print("Dealer Busts...(WIN!)")
        Capital_Statistics[1] += Capital_Statistics[2] * Capital_Statistics[3]
        Game_Statistics[0] += 1

    elif Dealer_State[1] > Player_State[1]:
        if Show_Process:
            print("Dealer gets bigger points (LOSE...)")
        Capital_Statistics[1] -= Capital_Statistics[2] * Capital_Statistics[3]
        Game_Statistics[2] += 1

    elif Dealer_State[1] == Player_State[1]:
        if Show_Process:
            print("Same points... (DRAW...)")
        Game_Statistics[1] += 1

    elif Dealer_State[1] < Player_State[1]:
        if Show_Process:
            print("Player gets  bigger points (WIN!)")
        Capital_Statistics[1] += Capital_Statistics[2] * Capital_Statistics[3]
        Game_Statistics[0] += 1

    return Game_Statistics, Player_State, Dealer_State, Capital_Statistics

def Game_Process():
    pass

def BlackJack_Backtesting(Player_Card=[], Dealer_Card=[], round_num = 100, Show_Process = True):
    Capital_Statistics = [0, 0, 100, 1]                                    # 0.Capital 初始資金 0最後計算期望值比較方便   # 1.Earning 獲利   # 2.Bet 基本賭金,  3. Double  加注
    Hi_Lo = 0  # Hi-Lo算牌策略
    Game_Statistics = [0, 0, 0, 0, 0]                                     # 紀錄 勝 ,和 ,負, 21點次數, 五龍次數
    Deck = 5

    Player_Bet = BlackJack_Bet
    Player_Bet.bet = Capital_Statistics[2]
    Player_Bet.option = 1

    ## 固定牌組數情況下
    # Shuffle_Poker = Shuffle(Deck=Deck)
    # print(str(Shuffle_Poker) + "\n")

    if Show_Process:
        # 建立欄位表
        print("{:<10}{:<50}{:<50}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format('Round', "Player's Cards", "Dealer's Cards", "Bets", "Captials", "Win Ratio", "21Points", "5 Cards", "Expected value"))

    n = 0
    for round in range(1, round_num+1):
        Player_State = [[], 0, 0, False, False, False, False, False]                                    # 玩家: 0. 手牌 1.點數  2.有A時點數  3.21點  4. 爆牌  5. 五龍  6. 停牌  4. 加注
        Dealer_State = [[], 0, 0, False, False, False, False, False]                                    # 莊家: 0. 手牌 1.點數  2.有A時點數  3.21點  4. 爆牌          6. 停牌
        Capital_Statistics[3] = 1
        i,j = 0,0

        # 完全隨激發牌的情況
        Player_State[0] = Player_Card.copy()
        Dealer_State[0] = Dealer_Card.copy()

        for _ in range(2 - len(Player_State[0])):
            Player_State[0].append(random.choice(Poker))
        for _ in range(2 - len(Dealer_State[0])):
            Dealer_State[0].append(random.choice(Poker))

        # 總牌數固定的情況
        # for _ in range(2):
        #     Player_State[0], Shuffle_Poker = Deal(Player_State[0], Shuffle_Poker, 1)
        #     Dealer_State[0], Shuffle_Poker = Deal(Dealer_State[0], Shuffle_Poker, 1)

        Player_State[1] = Card_Point(Player_State[0])
        Dealer_State[1] = Card_Point(Dealer_State[0])

        Player_State[2] = Card_with_A(Player_State[0], Player_State[1])
        Dealer_State[2] = Card_with_A(Dealer_State[0], Dealer_State[1])

        Player_State = Point21(Player_State)
        Dealer_State = Point21(Dealer_State)

        if Show_Process:
            print("{:<10}{:<40}{:<10}{:<40}{:<10}".format(str(round), "P:" + str(Player_State[0]), str(Player_State[1]),
                                                          "D:['?', '" + str(Dealer_State[0][1]) + "']",
                                                          str(Poker_Convert.get(Dealer_State[0][1]))))

        if Dealer_State[3]:  # 如果莊家不是21點 則顯示單張牌
            if Show_Process:
                print("{:<10}{:<40}{:<10}{:<40}{:<10}".format('', '', '', "D:['?', '" + str(Dealer_State[0][1]) + "']",
                                                              str(Poker_Convert.get(Dealer_State[0][1]))))

        # 玩家補牌
        if 1 < Poker_Convert.get(Dealer_State[0][1]) < 7 and 11 < Player_State[1] < 17:  # 若莊家明牌<6點 則玩家不加牌
            Player_State[6] = True  # 勝率提高到47.17%(從46.2%) 期望值:+0.0024 ~+ 0.0004

        while Player_State[1] < 17 and Player_State[2] < 17 and not (Dealer_State[3]) and not (
        Player_State[5]) and not (
                Player_State[6]) and not (Player_State[7]):
            if i == 0 and 10 <= Player_State[1] <= 11 and 1 < Poker_Convert.get(Dealer_State[0][1]) < 10:
                Capital_Statistics[3] = 2
                Player_State[7] = True

            Player_State[0].append(random.choice(Poker))  # Shuffle_Poker[n + 1]   random.choice(Poker)
            Player_State[1] += Poker_Convert.get(Player_State[0][2 + i])

            if '♣A' in Player_State[0] or '♦A' in Player_State[0] or '♥A' in Player_State[0] or '♠A' in Player_State[
                0]:  # 判定是否有A的牌型 有則+10
                Player_State[2] = Player_State[1] + 10

                if Player_State[2] > 21:  # 如果有A牌型 但超過21 則回復原本牌點(-10)
                    Player_State[2] = Player_State[1]
                elif Player_State[2] <= 21:  # 如果有A牌型 小於21  則保留A牌型點數(+10)
                    Player_State[1] = Player_State[2]

            if Player_State[2] >= 17:
                Player_State[1] = Player_State[2]

            if Player_State[1] > 21:  # 判定玩家是否爆牌
                Player_State[4] = True

            elif i == 2 and Player_State[1] <= 21:  # 判定玩家過五關
                Player_State[5] = True

            # if 1 < Poker_Convert.get(Dealer_State[0][1]) < 6 and Player_State[1] >= 12:  # 若莊家明牌<6點 則玩家不加牌
            # P_Stop = True #加入這行 勝率(47.38%)變高 但期望值(-0.0028)變低
            if Show_Process:
                print("{:<10}{:<40}{:<10}".format('', "P:" + str(Player_State[0]), str(Player_State[1])))
            i += 1
            n += 1

        if 21 > Dealer_State[1] >= 17:
            if Show_Process:
                print("{:<10}{:<40}{:<10}{:<40}{:<10}".format('', '', '', "D:[" + str(Dealer_State[0]) + "']",
                                                              str(Dealer_State[1])))

        # 莊家不足17點補牌
        while Dealer_State[1] < 17 and Dealer_State[2] < 17 and not (Player_State[4]) and not (
        Player_State[3]) and not (
                Dealer_State[3]) and not (Player_State[5]):
            Dealer_State[0].append(random.choice(Poker))  # Shuffle_Poker[n + 1]
            Dealer_State[1] += Poker_Convert.get(Dealer_State[0][2 + j])
            if '♣A' in Dealer_State[0] or '♦A' in Dealer_State[0] or '♥A' in Dealer_State[0] or '♠A' in Dealer_State[0]:
                Dealer_State[2] = Dealer_State[1] + 10
                if Dealer_State[2] > 21:  # 如果有A牌型 但超過21 則回復原本牌點(-10)
                    Dealer_State[2] = Dealer_State[1]
                elif Dealer_State[2] <= 21:  # 如果有A牌型 小於21   則保留A牌型點數(+10)
                    Dealer_State[1] = Dealer_State[2]
            if Show_Process:
                print("{:<10}{:<40}{:<10}{:<40}{:<10}".format('', '', '', "D:[" + str(Dealer_State[0]) + "']",
                                                              str(Dealer_State[1])))

            j += 1
            n += 1

            # 判斷莊家是否爆牌
            if Dealer_State[1] > 21:
                Dealer_State[4] = True
            else:
                Dealer_State[4] = False

        # 判定勝負
        Game_Statistics, Player_State, Dealer_State, Capital_Statistics = Game_Result(Game_Statistics, Player_State,
                                                                                      Dealer_State, Capital_Statistics,
                                                                                      Show_Process)

        try:
            win_ratio = str(float(Game_Statistics[0] / (round - Game_Statistics[1]) * 100))[:5]
        except:
            win_ratio = 0

        try:
            Expected_Value = str(
                (Game_Statistics[0] * 1 + Game_Statistics[3] * 0.5 + Game_Statistics[4] * 2 - Game_Statistics[
                    2] * 1) / (
                        round - Game_Statistics[1]))[:8]
        except:
            Expected_Value = 0

        if Show_Process:
            print("{:<110}{:<20}{:<20}{:<20}{:<20}{:<20}{}".format('', "$" + str(
                Capital_Statistics[2] * Capital_Statistics[3]), "$" + str(
                Capital_Statistics[0] + Capital_Statistics[1]), str(Game_Statistics[0]) + "W/" + str(
                Game_Statistics[1]) + "/" + str(Game_Statistics[2]) + "L " + "(" + str(win_ratio) + "%)",
                                                                   Game_Statistics[3], Game_Statistics[4],
                                                                   Expected_Value))
            print(
                '------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    if Show_Process == False:
        print("Capital:{:<20} Win Ratio : {:<30}  BlackJack : {:<20}  Five :{:<20} Expected_Value: {:<8}%".format("$" + str(Capital_Statistics[0] + Capital_Statistics[1]),str(Game_Statistics[0]) + "W/" + str(Game_Statistics[1]) + "/" + str(Game_Statistics[2]) + "L " + "(" + str(win_ratio) + "%)", Game_Statistics[3],Game_Statistics[4], Expected_Value))


if __name__ == "__main__":
    BlackJack_Backtesting(Player_Card=[], Dealer_Card=[], round_num=100, Show_Process = True)