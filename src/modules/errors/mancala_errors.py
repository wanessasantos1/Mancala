class MancalaMovementInvalidError(Exception):
    """
        Exception raised when a player tries to make an invalid move.
    """
    pass

class MancalaLoadGameError(Exception):
    """
        Exception raised when a player tries to load a game that does not exist.
    """
    pass