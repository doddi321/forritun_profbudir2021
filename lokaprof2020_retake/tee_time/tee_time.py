
class TeeTime:
    __MAX_PLAYERS = 4
    def __init__(self, time: str) -> None:
        self.__time = time 
        self.__players = []

    def add_player(self, player: str) -> str:
        if len(self.__players) < TeeTime.__MAX_PLAYERS:
            self.__players.append(player)
            return True 
        else:
            return False

    def remove_player(self, player: str):
        if player in self.__players:
            self.__players.remove(player)
    
    def merge(self, other: "TeeTime"):
        players_to_remove = []
        for player in other.__players:
            if (self.add_player(player)):
                players_to_remove.append(player)

        for player in players_to_remove:
            other.remove_player(player)


    def __str__(self) -> str:
        string = f'{self.__time}'
        if (len(self.__players) > 0):
            string += f' {" ".join(self.__players)}'
        return string

    def get_time(self):
        return self.__time