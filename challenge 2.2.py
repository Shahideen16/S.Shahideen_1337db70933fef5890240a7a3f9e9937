class Player:

  def Play(self):
    print("The player is playing cricket")


class Batsman(Player):

  def Play(self):
    print("The Batsman is batting")


class Bowler(Player):

  def Play(self):
    print("The Bowler is bowling")


# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the Play method for each object
batsman.Play()
bowler.Play()