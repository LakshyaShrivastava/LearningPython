import chess
import chess.svg
import chess.polyglot
import time
import traceback
import chess.pgn
import chess.engine
from flask import Flask, Response, request
import webbrowser
import pyttsx3

board = chess.Board()
print(board)

pawnTable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    100, 100, 100, 100, 100, 100, 100, 100]

knightsTable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]
bishopsTable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]
rooksTable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]
queensTable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]
kingsTable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]


def evaluate_board():
    if board.is_checkmate():
        if board.turn:
            return -99999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0
    # white pieces
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))

    # black pieces
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    # total material
    material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)

    # evaluate pawns based on their locations
    pawnSQ = sum([pawnTable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnSQ = pawnSQ + sum([-pawnTable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])

    # evaluate knights based on their locations
    knightSQ = sum([knightsTable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightSQ = knightSQ + sum([-knightsTable[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.BLACK)])

    # evaluate bishops based on their locations
    bishopSQ = sum([bishopsTable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopSQ = bishopSQ + sum([-bishopsTable[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])

    # evaluate rooks based on their locations
    rookSQ = sum([rooksTable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rookSQ = rookSQ + sum([-rooksTable[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.BLACK)])

    # evaluate queens based on their locations
    queenSQ = sum([queensTable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queenSQ = queenSQ + sum([-queensTable[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.BLACK)])

    # evaluate queens based on their locations
    kingSQ = sum([kingsTable[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingSQ = kingSQ + sum([-kingsTable[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])

    eval = material + pawnSQ + knightSQ + bishopSQ + rookSQ + queenSQ + kingSQ

    if board.turn:
        return eval
    else:
        return -eval


def selectMove(depth):
    try:
        move = chess.polyglot.MemoryMappedReader(
            "C:/Users/laksh_gbkifb1/PycharmProjects/chessEngine/books/human.bin").weighted_choice(board).move
        print("Book Move Found")
        return move
    except:
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in board.legal_moves:
            board.push(move)
            boardValue = -alphabeta(-beta, -alpha, depth - 1)
            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move
            if boardValue > alpha:
                alpha = boardValue
            board.pop()
        return bestMove

score = 0
def quiesce(alpha, beta):
    global score
    stand_pat = evaluate_board()
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiesce(-beta, -alpha)
            board.pop()
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    return alpha

def alphabeta(alpha, beta, depthLeft):
    bestScore = -9999
    if depthLeft == 0:
        return quiesce(alpha, beta)
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(-beta, -alpha, depthLeft - 1)
        board.pop()
        if score >= beta:
            return score
        if score > bestScore:
            bestScore = score
        if score > alpha:
            alpha = score
    return bestScore
# Speak Function for the Assistant to speak
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set index for voices currently 3 voices available
    engine.say(text)
    engine.runAndWait()

# Searching Dev-Zero's Move
def devmove():
    move = selectMove(3)
    speak(move)
    board.push(move)

# Searching Stockfish's Move
def stockfish():
    engine = chess.engine.SimpleEngine.popen_uci(
        "engines/stockfish.exe")
    move = engine.play(board, chess.engine.Limit(time=0.1))
    speak(move.move)
    board.push(move.move)

app = Flask(__name__)


# Front Page of the Flask Web Page
@app.route("/")
def main():
    global count, board
    if count == 1:
        count += 1
    ret = '<html><head>'
    ret += '<style>input {font-size: 20px; } button { font-size: 20px; }</style>'
    ret += '</head><body>'
    ret += '<img width=510 height=510 src="/board.svg?%f"></img></br>' % time.time()
    ret += '<form action="/game/" method="post"><button name="New Game" type="submit">New Game</button></form>'
    ret += '<form action="/undo/" method="post"><button name="Undo" type="submit">Undo Last Move</button></form>'
    ret += '<form action="/move/"><input type="submit" value="Make Human Move:"><input name="move" type="text"></input></form>'
    ret += '<form action="/recv/" method="post"><button name="Receive Move" type="submit">Receive Human Move</button></form>'
    ret += '<form action="/dev/" method="post"><button name="Comp Move" type="submit">Make Dev-Zero Move</button></form>'
    ret += '<form action="/engine/" method="post"><button name="Stockfish Move" type="submit">Make Stockfish Move</button></form>'
    ret += '<form action="/inst/" method="post"><button name="Instructions" type="submit">Instructions</button></form>'
    ret += '<form action="/cred/" method="post"><button name="Credits" type="submit">Credits</button></form>'
    if board.is_stalemate():
        speak("Its a draw by stalemate")
    elif board.is_checkmate():
        speak("Checkmate")
    elif board.is_insufficient_material():
        speak("Its a draw by insufficient material")
    elif board.is_check():
        speak("Check")
    return ret

# Display Board
@app.route("/board.svg/")
def board():
    return Response(chess.svg.board(board=board, size=700), mimetype='image/svg+xml')


# Human Move
@app.route("/move/")
def move():
    try:
        move = request.args.get('move', default="")
        speak(move)
        board.push_san(move)
    except Exception:
        traceback.print_exc()
    return main()

# Recieve Human Move
@app.route("/recv/", methods=['POST'])
def recv():
    try:
        None
    except Exception:
        None
    return main()


# Make Dev-Zero Move
@app.route("/dev/", methods=['POST'])
def dev():
    try:
        devmove()
    except Exception:
        traceback.print_exc()
        speak("illegal move, try again")
    return main()


# Make UCI Compatible engine's move
@app.route("/engine/", methods=['POST'])
def engine():
    try:
        stockfish()
        # cdrill()
        # deuterium()
    except Exception:
        traceback.print_exc()
        speak("illegal move, try again")
    return main()

# New Game
@app.route("/game/", methods=['POST'])
def game():
    speak("Board Reset, Best of Luck for the next game.")
    board.reset()
    return main()


# Undo
@app.route("/undo/", methods=['POST'])
def undo():
    try:
        board.pop()
    except Exception:
        traceback.print_exc()
        speak("Nothing to undo")
    return main()
@app.route("/inst/", methods=['POST'])
def inst():
    speak(
        "This is a simple chess game which works with chess san notations which you can get by browsing the net. For starters you can place a human move like e4, or Nf3. This game is also equipped with two chess engines namely dev-zero and stockfish 9 for learning process. There are more two engines available in the code named cdrill and deuterium but are not used in the gui, you can also check that out. The engines will search for the best possible move and then give it to you. The dev-zero engine was created by my creator and is still in beta mode. The stockfish 9 engine was created by Tord Romstad and his team and this engine is one of the best open source engine in the current era. Some times the engine gives the wrong notation and therefore no move has been returned, therefore you must try once more and check your luck. There are seven user friendly buttons and I am pretty sure that there is no need of explanation. A user can use the tool ngrok and play with any other user in the world by just sending the link provided by the ngrok tool. This server was created by the flask platform, so there are no restriction for one on one move and therefore its not so secure till now but still it works. In a two human's game, a user needs to make a human move then wait and click on the receive human move to receive the move from the person playing from the other side of the world. The users must communicate before and discuss who will play black and who will play white correspondingly. For starters you can make a human move by typing e4.")
    return main()


# Main Function
if __name__ == '__main__':
    count = 1
    board = chess.Board()
    app.run(host='0.0.0.0', port=81)

# AI Vs AI
# count = 0
# movehistory = []
# game = chess.pgn.Game()
# board = chess.Board()
#
# while not board.is_game_over(claim_draw=True):
#     if board.turn:
#         count += 1
#         print(f'\n{count}]\n')
#         move = selectMove(1)
#         board.push(move)
#         print(board)
#         print()
#     else:
#         move = selectMove(3)
#         board.push(move)
#         print(board)
# game.add_line(movehistory)
# game.headers["Event"] = "Self Tournament 2022"
# game.headers["Site"] = "Milpitas"
# game.headers["Date"] = str(datetime.now().date())
# game.headers["Round"] = 1
# game.headers["White"] = "Ai"
# game.headers["Black"] = "Ai"
# game.headers["Result"] = str(board.result(claim_draw=True))
# print(game)
# SVG(chess.svg.board(board=board,size=400))

# AI VS Stockfish

# count = 0
# movehistory = []
# game = chess.pgn.Game()
# board = chess.Board()
# engine = chess.engine.SimpleEngine.popen_uci("engines/stockfish.exe")
# while not board.is_game_over(claim_draw=True):
#     if board.turn:
#         count += 1
#         print(f'\n{count}]\n')
#         move = engine.play(board, chess.engine.Limit(time=0.1))
#         movehistory.append(move.move)
#         board.push(move.move)
#         print(board)
#     else:
#         move = selectMove(5)
#         movehistory.append(move)
#         board.push(move)
#         print(board)
#
# game.add_line(movehistory)
# game.headers["Result"] = str(board.result(claim_draw=True))
# print(game)
# SVG(chess.svg.board(board=board, size=400))


