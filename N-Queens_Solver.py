# Mohamed Mahmoud

# math module
import math

# module to allow for shallow and deep copy an object
import copy

# Arrays, matrices, and high level mathematical functions
import numpy as np

# To calculate execution time
import time

# For move generation and validation
import chess

# Interpreter variables and functions
import sys

# Pseudo-random number generator for distributions
import random

# Function 1: Returns the solution as a list of N integers, zero-indexed and comma seperated
def getAnswer(board):
    
    # List that will be returned
    answer=[]
    
    # Iterate over each row in the board
    for row in board:
        
        # Use a counter to hold the current column
        counter = 0
        
        # Iterate over each variable in that row
        for index in row:
            
            # If a queen has been found
            if index==1:
                
                # Append the queens column number in the current row to the list
                answer.append(counter)
                
            # Increment the counter for each column
            counter+=1
    
    # Reverse the list to return the columns that have queens for each row in the board
    answer.reverse()
    
    # Return the answer
    return answer

# Function 2: Function to check if the current variable is valid in the board 
def validate(row,column):
    
    # Check if the current variable is between the specified row size and column size
    if (row>=0 and row<N and column>= 0 and column<N):
        
        # Return true if that is the case
        return True
    
    # Else
    else:
        
        # Return False
        return False

# Function 3: Function to check if the pair of queens in current pair
def checker(i,j,l,m,twoVariables):
    
    # check that they are in the pair
    if (i,j,l,m) in twoVariables:
        
        # return true
        return True
    
    # Case 2:
    if (l,m,i,j) in twoVariables:
        
        # return true
        return True
    
    # return false
    return False

# Function 4: Function to create the board
def generateChessBoard(board):
    
    # Generate a new chess board
    board = chess.Board()
    
    # Clear the chess board
    board.clear()
    
    # Iterate from 0 to the number of queens ~ rows
    for i in range(N):
        
        # Iterate from 0 to the number of queens ~ columns
        for j in range(N):
            
            # If the Set the queens at the diagonals
            if board[i][j]:
                
                # Set the queens at the specified square
                board.set_piece_at(chess.square(i,j),chess.Piece(5,chess.WHITE))
    
    # Return the generated board
    return board.fen()

# Function 5: Function to reset the board when a local optima is encountered
def resetPositions(board):
    
    # Iterate over each row in the board
    for row in board:
        
        # While there is more than 1 row in the board
        while row.count(1) > 1:
            
            # Iterate from 0 to the number of queens
            for i in range(N):
                
                # If the current row has no queens
                if board[i].count(1) == 0:
                    
                    # Set a variable to the value of the index containing the queen
                    j = row.index(1)
                    
                    # set the current index to the queen
                    board[i][j] = 1
                    
                    # set the index of the previous queen to 0
                    row[j] = 0
                    
                    # break after the current row contains no queens
                    break
    
    # return the reset board
    return board

# Function 6: Heuristic function: Number of pairs of queens attacking each other ~ Max value is N choose 2
def heuristicFunction(board):
    
    # Initial Value
    h = 0
    
    # Pairs of queens to check
    twoVariables = []
    
    # Iterate over the rows
    for i in range(N):
        
        # Iterate over the columns
        for j in range(N):
            
            # The value at that row column value pair
            if board[i][j]:

                # Calculate horizontal attacks
                
                # Constraint 1: no two queens in the same row
                for k in range(N):
                    
                    # If the current index is a queen
                    if board[i][k] == 1 and k != j and not checker(i,j,i,k,twoVariables):
                        
                        # add the queen to the two queens that will be checked
                        twoVariables.append((i,j,i,k))
                        
                        # increment the heuristic value by 1
                        h += 1

                # Constraint 2: no two queens in the same column
                for k in range(N):
                    
                    #If the current index is a queen
                    if board[k][j] == 1 and i != k and not checker(i,j,k,j,twoVariables):
                        
                        # add the queen to the two queens that will be checked
                        twoVariables.append((i,j,k,j))
                        
                        # incremenet the heuristic value by 1
                        h += 1

                # Constraint 3: Diagonals parallel to y=x
                
                # First go up the diagonal
                l, m = i-1, j+1
                
                # while inside the boards boundries
                while validate(l,m):
                    
                    # if the current index is a queen
                    if board[l][m] == 1 and not checker(i, j, l, m, twoVariables):
                        
                        # add the queen to the two queens that will be checked
                        twoVariables.append((i, j, l, m))
                        
                        # increment the heuristic value by 1
                        h += 1
                    
                    # check the next index of the diagonal to the right
                    l, m = l-1, m+1

                # Now go down the diagonal
                l, m = i+1, j-1
                
                # while inside the boards boundries
                while validate(l, m):
                    
                    # if the current index is a queen
                    if board[l][m] == 1 and not checker(i, j, l, m, twoVariables):
                        
                        # add the queen to the two queens that will be checked
                        twoVariables.append((i, j, l, m))
                        
                        # increment the heuristic value by 1
                        h += 1
                    
                    # check the next index of the diagonal to the left
                    l, m = l+1, m-1

                # Constraint 4: Diagonals parallel to y=-x
                
                # First go up the diagonal
                l, m = i-1, j-1
                
                # while inside the boards boundries
                while validate(l,m):
                    
                    # if the current index is a queen
                    if board[l][m] == 1 and not checker(i, j, l, m, twoVariables):
                        
                        # add the queen to the pair of queens that will be checked
                        twoVariables.append((i, j, l, m))
                        
                        
                        # increment the heuristic value by 1
                        h += 1
                    
                    # check the next index of the diagonal to the left
                    l, m = l-1, m-1

                # Now go down the diagonal
                l, m = i+1, j+1
                
                # while inside the boards boundries
                while validate(l, m):
                    
                    # if the current index is a queen
                    if board[l][m] == 1 and not checker(i, j, l, m, twoVariables):
                        
                        # add the queen to the pair of queens that will be checked
                        twoVariables.append((i, j, l, m))
                        
                        # increment the heuristic value by 1
                        h += 1
                    
                    # check the next index of the diagonal to the right
                    l, m = l+1, m+1
    
    # Return the value of the heuristic
    return h

# Function 7: Using hill climbing optimization local search
def hillClimbingOptimization(board):
    
    # Find the least cost successor for the given board state
    smallestHeuristicBoard = board
    
    # set the current heuristic value to the maximum int value
    currentHeuristicValue = 9223372036854775806
    
    # set two variables for the different positions and the number of movements on the board
    global differentPositions, movesOnBoard
    
    # Number of steps taken
    movesOnBoard += 1

    # Check if number of side moves has reached a limit
    if differentPositions == 100:
        
        # return -1 to indicate that the goal has not been reached
        return -1
    
    # variable to indicate if another move for the queen is still possible
    movesStillPossible = False
    
    # iterate over the rows
    for i in range(N):
        
        # Find index of queen in current row
        queen = board[i].index(1)
        
        # set the current index to 0 and look for a new position for the queen
        board[i][queen] = 0
        
        # iterate over the columns
        for k in range(N):
           
           # if the current index does not contain a queen
            if k != queen:
                
                # set the current index to the queen
                board[i][k] = 1
                
                # calculate the heuristic value of the board
                h = heuristicFunction(board)
                
                # if the heuristic is higher than the current heuristic value
                if h < currentHeuristicValue:
                    
                    # set the current heuristic value to the new heuristic value
                    currentHeuristicValue = h
                    
                    # set the smallest heuristic board to the current board
                    smallestHeuristicBoard = copy.deepcopy(board)
                
                # if the current heuristic value is equal to the new heurisitic value
                if h == currentHeuristicValue:
                    
                    # set the current heuristic value to the new heuristic value
                    currentHeuristicValue = h
                    
                    # set the smallest heuristic board to the current board
                    smallestHeuristicBoard = copy.deepcopy(board)
                    
                    # indicate that it is still possible to get a better heuristic
                    movesStillPossible = True
                
                # set the current index to 0 after the queen has been moved to a new position
                board[i][k] = 0
        
        # set the new index to hold the queen
        board[i][queen] = 1
    
    # if it is still possible to get a better heuristic
    if movesStillPossible:
        
        # increment the current different positions counter
        differentPositions += 1
    
    # if the the goal has been reached
    if currentHeuristicValue == 0:
        
        # return the board
        return smallestHeuristicBoard
    
    # else recursively call the hill climbing optimization on the better board
    return hillClimbingOptimization(smallestHeuristicBoard)


# START OF MAIN ------------------------------------------------------------------------------------------------------------------------------------

# Enter desired N
N = int(input())

# compute the start time
startTime = time.time()

# Variable to hold the number of tries
tries=0

# Maximum tries set to 100 according to the value in Page 240 of the textbook
maximumTries=100

# Try to find answer to the N queens problem
while tries<(maximumTries+1):
    
    # If N is 1, then return 1
    if N==1:
         
        #
        print("[1]")
        break
    
    # NxN board
    board = []
    
    # variable for the different number of positions
    differentPositions = 0
    
    # variable for the number of moves on board
    movesOnBoard = 0
    
    # Iterate over the chosen value for N
    for i in range(N):
        
        # Create a row of empty zeros
        row = [0]*N
        
        # Chose a random location for the placement of the queen
        randomIndex=random.randint(0,N-1)
        
        # Set the value
        row[randomIndex]=1
        
        # Add the row to the board
        board.append(row)
    
    # set up the initial board
    board = resetPositions(board)
    
    # try to find a correct target state that satisfies the constraints
    smallestHeuristicBoard = hillClimbingOptimization(board)
    
    # if a correct state is found
    if smallestHeuristicBoard != -1:
        
        # turn the board to the correct output form
        correctAnswer = getAnswer(smallestHeuristicBoard)
        
        # print the correct answer
        print(correctAnswer)
        
        # End if the solution has been found
        break
    
    # If the solution has not been found
    else:
        
        # If maximum number of tries has been reached
        if tries==maximumTries:
            print("Could not solve")
    
    # Increment the counter for the current trial number
    tries+=1

# Program ended
endTime = time.time()

# Calculate the execution time
executionTime = endTime - startTime

# Print the execution state
print("The execution time is:",format(executionTime,'.32f'))
