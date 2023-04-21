from Repository import Repository
from Service import Service
from UI import UI
board=Repository()
board2=Service(board)
game=UI(board2)
UI.main(game)