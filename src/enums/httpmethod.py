from enum import Enum

class HttpMethod(Enum):
    GET
    POST
    PUT
    DELETE

    @classmethod
    def get_query_params(key: str) -> Dict:
        try:
            return {key: OBJECTS[key]}
        except KeyError:
            raise NotFoundError(key)
 
    @classmethod
    def get_from_player_name(self, player_name) -> Enum:
        """ PlayerType を player name より逆引きする        
        :param player_name: プレイヤー名
        :return: PlayerType名
        """
        for s in [*self.__members__.values()]:
            if s.player_name == player_name:
                return s
        return None
