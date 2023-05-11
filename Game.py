# Here Is the game that you and Ai and Multiplayer Can Play
def ConstBoard(Board):
  print("Current State of The Board: \n \n");
  for i in range(0, 9):
    if ((i > 0) and ((i % 3) == 0)):  # Here it will move to new line
      print("\n");
    if (Board[i] == 0):
      print("_ ", end=" ");
    if (Board[i] == -1):
      print("X", end=" ");
    if (Board[i] == 1):
      print("O", end=" ");
  print("\n\n");

def User1Turn(Board):
  pos = input("Enter X position from 0 to 9: ");
  pos = int(pos);
  if (Board[pos-1] != 0):
    print("Wrong Move");
    exit(0);
  Board[pos-1] = -1;

def User2Turn(Board):
  pos=input("Enter 0s position from 0 to 9");
  pos=int(pos);
  if(Board[pos-1]!=0):
    print("Wrong Move");
    exit(0);
  Board[pos-1]=1;

  #This is MinMax Algorithm where we have Code the AI

def minmax(Board,player):
  x=analyzeBoard(Board);
  if(x!=0):
    return (x*player);
  pos=-1
  value=-2;
  for i in range (0,9):
    if(Board[i]==0):
      Board[i]=player;
      score=-minmax(Board,player*-1);
      Board[i]=0;
      if(score>value):
        value=score;
        pos=i;
  if(pos==-1):
    return 0;
  return value;

def CompTurn(Board):
  pos=-1
  value=-2;
  for i in range (0,9):
    if(Board[i]==0):
      Board[i]=1;
      score=-minmax(Board,-1);
      Board[i]=0;
      if(score>value):
        value=score;
        pos=i;
  Board[pos]=1;

  #Here It will analyze and all the condition are given
  # in which a user can win

def analyzeBoard(Board):
  cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8],[2,4,6]]
  for i in range(0, 8):
    if (Board[cb[i][0]] != 0 and
        Board[cb[i][0]] == Board[cb[i][1]] and
        Board[cb[i][0]] == Board[cb[i][2]]):
      return Board[cb[i][0]];
  return 0;

  #This is the main Function where all the function are called

def main():
  choice = input("enter 1 for single player and 2 for multiplayer:");
  choice = int(choice);
  Board = [0, 0, 0, 0, 0, 0, 0, 0, 0];
  if (choice == 1):
    print("computer:O vs You:X");
    player = input("Enter to play 1(st) or 2(nd): ");
    player = int(player);
    for i in range(0, 9):
      if (analyzeBoard(Board) != 0):
        break;
      if ((i+player) % 2 == 0):
        CompTurn(Board);
      else:
        ConstBoard(Board);
        User1Turn(Board);
  else:
    for i in range(0, 9):
      if (analyzeBoard(Board) != 0):
         break;
      if (i % 2 == 0):
         ConstBoard(Board);
         User1Turn(Board);
      else:
         ConstBoard(Board);
         User2Turn(Board);

#Here It Will analyze the board and check who has win
                    
  x =analyzeBoard(Board);
  if (x == 0):
    ConstBoard(Board);
    print("Well Played Bot O You Alas But its a Draw");
  if (x == -1):
    ConstBoard(Board);
    print("Player x Win and O Looses !!");
  if (x == 1):
    ConstBoard(Board);
    print("Player O Win and X Looses !!");
#Main Function is called becauese it is main part of this game as all fuction are called here
main();
