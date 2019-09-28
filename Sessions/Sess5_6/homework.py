#Magic Maze Homework
maze_status = True
possible_directions = ["N", "S", "E", "W"]
pathway = ""
moves = 0
total_moves = 0
lives = 3
escape = "SSNWES"

def makeMove():
    global lives
    global moves
    moves_available = 10-moves

    if lives == 0:
        return False

    if moves_available == 0:
        lives= lives-1
        print("      You lost a life.")
        moves=0

    else:
        print("      Health status: "+str(lives)+" lives")
        print("      Moves left: "+str(moves_available))

def updatePath(pathway, total_moves):
    counter = 0
    for i in pathway:
        if i != escape[counter]:
            print("      You returned to the beginning...")
            return False
            break
        counter = counter + 1

    if pathway == escape:
        print("You won with a total of " + str(total_moves) + " moves.")
        global maze_status
        maze_status = False

while maze_status:
    while True:
        print("You are in the magic maze. Which way do you wanna go? (N, S, E, W)")
        direction = input()

        if direction in possible_directions:
            moves = moves + 1
            total_moves = total_moves + 1

            pathway = pathway + direction
            if updatePath(pathway, total_moves)==False:
                pathway = ""
            else:
                print("      Your current pathway is: " + pathway)

            if makeMove()==False:
                print("You lost all of your lives.")
                maze_status = False

            False
            break

        print("The direction you entered cannot be accepted.")

print("Game exit.")