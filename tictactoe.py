class Player:
  def __init__(self, name, token):
    self.name = name
    self.token = token

  def __repr__(self):
    return self.name

class Game:
  def __init__(self):
    self.board = [[" " for x in range(3)] for y in range(3)]

  def __repr__(self):
    display = "\n"
    for row in self.board:
      display += "|".join(row)
      display += "\n"
    return display

  def move(self, x, y, token):
    """checks the requested space on the board; if taken, returns message; if available, places player token at specified coordinates"""
    if self.board[x][y] != " ":
      return "Space already taken. Please try again."
    else:
      self.board[x][y] = token

  def calc_winner(self):
    # match = 0
    # for x in range(3):
    #   if self.board[x][y] = self.board[x][y]
    #   match = match + 1
    #   if match = 3
    #   win
    pass

  def is_full(self):
    """scans each row of the board and returns False, if any section is blank; otherwise, returns True"""
    for row in self.board:
      if any(item == " " for item in row):
        return False
    print("No more moves available. Game over.\n")
    quit()

  def is_game_over(self):
    """runs two methods to determine if game has concluded"""
    return self.calc_winner() or self.is_full()

# - - - - - - - END CLASSES - - - - - - - -

def get_current_player(current_round, player_one, player_two):
  if current_round % 2 == 0:
    return player_two
  else:
    return player_one

def main():
  board = Game()

  name_one = input("\nPlayer One - You will be 'X': What is your name? ")
  player_one = Player(name_one, "X")

  name_two = input("Player Two - You will be 'O': What is your name? ")
  player_two = Player(name_two, "O")

  print(f"\nOkay, {player_one.name} & {player_two.name}... let's play!")
  print(f"\nHere's the board...\n{board}")

  current_round = 1

  while True:

    current_player = get_current_player(current_round, player_one, player_two)

    board.is_game_over()
    x = int(input(f"{current_player.name}, select your horizontal location (0-2): "))
    y = int(input(f"Select your vertical location (0-2): "))
    if 0 <= x <= 2 and 0 <= y <= 2:
      board.move(x, y, current_player.token)
      print(board)
    else:
      print("\nNot a valid move. Please try again.\n")
      continue

    current_round += 1




main()


