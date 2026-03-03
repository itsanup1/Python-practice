class Scoreboard:
    def __init__(self, ser_num ,player_id,highest_score,playtime):
        self.rank= ser_num
        self.id = player_id
        self.high_score = highest_score
        self.time = playtime
players = []
player1= Scoreboard('1','3326','722','36 min')
players.append(player1)
player2= Scoreboard('2','4228','678','32 min')
players.append(player2)
player3= Scoreboard('3','7326' , "512", "28 min")
players.append(player3)
player4= Scoreboard('4','9256','336','42 min')
players.append(player4)
player5= Scoreboard('5','3935','248','30 min')
players.append(player5)
               
for i in range(5):
    print(f"Player{i + 1} , has scored {players[i].high_score}")                                             