COLORS = ["orange", "black"]  # piece colors

# Scores for each piece
# The scores are negative
# so that its easy to detect
# if the game has ended
# and to count the score
# eg, if all pieces exist, the
# score must be 0
# but if an opponent takes a piece
# then the value will be 0 + piece_value
PIECE_SCORE = {
    "pawn": -1,
    "knight": -3,
    "bishop": -3,
    "rook": -5,
    "queen": -9,
    "king": 39
}


# All board pieces
# This is the default board
# It's flipped, so that values nearest
# to the top of this file will be the
# values that are drawn first
base_board = (
    [["rook", COLORS[0]], ["knight", COLORS[0]], ["bishop", COLORS[0]], ["queen", COLORS[0]], ["king", COLORS[0]], ["bishop", COLORS[0]], ["knight", COLORS[0]], ["rook", COLORS[0]]],
    [["pawn", COLORS[0]], ["pawn", COLORS[0]], ["pawn", COLORS[0]], ["pawn", COLORS[0]], ["pawn", COLORS[0]], ["pawn", COLORS[0]], ["pawn", COLORS[0]], ["pawn", COLORS[0]]],
    [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]],
    [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]],
    [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]],
    [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]],
    [["pawn", COLORS[1]], ["pawn", COLORS[1]], ["pawn", COLORS[1]], ["pawn", COLORS[1]], ["pawn", COLORS[1]], ["pawn", COLORS[1]], ["pawn", COLORS[1]], ["pawn", COLORS[1]]],
    [["rook", COLORS[1]], ["knight", COLORS[1]], ["bishop", COLORS[1]], ["queen", COLORS[1]], ["king", COLORS[1]], ["bishop", COLORS[1]], ["knight", COLORS[1]], ["rook", COLORS[1]]]
)

# This is the data of the board
# It will be returned when called
# from the get_state function
data = [
    None,  # Board set to None because it has to be copied in the restart function
    (None, None),  # Store piece loc --; None just means its of type none
    "",  # Store what piece is focused
    "white"  # Store who is currently playing
]


def get_state():
    """
    Returns data about the state of the game
    """
    return (data[1], data[2], data[3], data[0])  # Return the state values as tuple so I can have tuple unpacking


def update_state(loc, hand, current, board):
    """
    Updates the state of the game

    :param (int, int) loc: game coord
    :param str hand: current piece
    :param str current: colour the player si
    :param [] board:
    """

    #### Update state variables with the params that are passed in
    data[0] = board
    data[1] = loc
    data[2] = hand
    data[3] = current
    ####
