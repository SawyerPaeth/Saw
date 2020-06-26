#Sawyer Paeth
#5/26/2020
#Description: Abstract board game called Gess. Uses GessGame class.



class GessGame:
    '''Creates the GessGame object.  Is the only class being used in this program. Interacts with no other classes.'''
    def __init__(self):
        '''Initializes a game board to self._board. Initializes current_state to "UNFINISHED". Initializes a list of letters
        used throughout the GessGame class to give numbered positions to each letter.  Sets current player to "BLACK."'''
        self._board = {'a':['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                       'b':['-', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', '-', '-'],
                       'c':['-', 'x', 'x', 'x', '-', '-', 'x', '-', '-', '-', '-', '-', '-', 'o', '-', '-', 'o', 'o', 'o', '-'],
                       'd':['-', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', '-', '-'],
                       'e':['-', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', '-', 'o', '-'],
                       'f':['-', '-', 'x', '-', '-', '-', 'x', '-', '-', '-', '-', '-', '-', 'o', '-', '-', '-', 'o', '-', '-'],
                       'g':['-', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', '-', 'o', '-'],
                       'h':['-', 'x', 'x', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', 'o', 'o', '-'],
                       'i':['-', 'x', 'x', 'x', '-', '-', 'x', '-', '-', '-', '-', '-', '-', 'o', '-', '-', 'o', 'o', 'o', '-'],
                       'j':['-', 'x', 'x', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', 'o', 'o', '-'],
                       'k':['-', 'x', 'x', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', 'o', 'o', '-'],
                       'l':['-', 'x', '-', 'x', '-', '-', 'x', '-', '-', '-', '-', '-', '-', 'o', '-', '-', 'o', '-', 'o', '-'],
                       'm':['-', 'x', 'x', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', 'o', 'o', '-'],
                       'n':['-', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', '-', 'o', '-'],
                       'o':['-', '-', 'x', '-', '-', '-', 'x', '-', '-', '-', '-', '-', '-', 'o', '-', '-', '-', 'o', '-', '-'],
                       'p':['-', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', '-', 'o', '-'],
                       'q':['-', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', '-', '-'],
                       'r':['-', 'x', 'x', 'x', '-', '-', 'x', '-', '-', '-', '-', '-', '-', 'o', '-', '-', 'o', 'o', 'o', '-'],
                       's':['-', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'o', '-', '-'],
                       't':['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']}

        self._current_state = "UNFINISHED"
        self._letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        self._current_player = "BLACK"
        self._not_current_player = "WHITE"

    def get_game_state(self):
        '''Returns the current game state.'''
        return self._current_state

    def get_current_player(self):
        '''Returns the current player.'''
        return self._current_player

    def resign_game(self):
        '''Checks to see whose turn it is. If its black's turn, sets current state to "WHITE_WON" and return current state.
        If it is white's turn, returns current state with black as winner.'''

        if self._current_player == "BLACK":
            self._current_state = "WHITE_WON"
            return self._current_state
        else:
            self._current_state = "BLACK_WON"
            return self._current_state


    def make_move(self, piece_loc, location):
        '''(Partially complete method).  Is called when user wants to make a move.  Uses piece and location parameter.
         Interacts with adjust_coordinate, game_piece, check_if_legal_piece, find_possible_moves, find_unobstructed_moves, replace, check_for_ring, and
         empty_outer_ring methods. Also calls current_player method to change who the current player is after one player makes a move.
         Checks to see if current state is "UNFINISHED",  if its not, move is not allowed and False is returned.'''

        if self._current_state != "UNFINISHED":

            return False

        piece = self.adjust_coordinate(piece_loc)
        adjust_location = self.adjust_coordinate(location)

        game_piece = self.game_piece(piece)
        piece_at_location = self.game_piece(adjust_location)

        if self.check_if_legal_piece(game_piece):

            legal_moves = self.find_possible_moves(game_piece, piece)

            replacement = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
            self.replace(piece, replacement, self._board)
            legal_moves_2 = self.find_unobstructed_moves(piece)
            self.replace(piece, game_piece, self._board)


            if adjust_location in legal_moves and adjust_location in legal_moves_2:


                replacement = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


                self.replace(piece, replacement, self._board)
                self.replace(adjust_location, game_piece, self._board)

                if self.check_for_ring(self._current_player, self._board):

                    self.empty_outer_ring()

                    if not self.check_for_ring(self._not_current_player, self._board):
                        self.set_current_state()

                    self.current_player()
                    return True

                else:

                    self.replace(piece, game_piece, self._board)
                    self.replace(adjust_location, piece_at_location, self._board)

                    return False
            else:

                return False
        else:

            return False


    def find_unobstructed_moves(self,piece):
        '''Finds all the unobstructed moves possible for a piece at a specific location.  Calls get_letter_num.'''

        moves = []

        letter_number = self.get_letter_num(piece)
        piece_num = int(piece[1:])
        new_piece_num1 = piece_num
        num1 = 2
        moves.append(self._letters[letter_number] + str(new_piece_num1 + 1))

        while new_piece_num1 < 18:
            if self._board[self._letters[letter_number-1]][piece_num + num1]== '-' and \
                self._board[self._letters[letter_number]][piece_num + num1] == '-' and \
                self._board[self._letters[letter_number +1]][piece_num + num1] == '-':

                moves.append(self._letters[letter_number] + str(piece_num + num1))
                num1 += 1
                new_piece_num1 +=1
            else:
                break




        new_piece_num2 = piece_num
        num2 = 2
        moves.append(self._letters[letter_number] + str(new_piece_num2 - 1))

        while new_piece_num2 > 1:
            if self._board[self._letters[letter_number - 1]][piece_num - num2] == '-' and \
                    self._board[self._letters[letter_number]][piece_num - num2] == '-' and \
                    self._board[self._letters[letter_number + 1]][piece_num - num2] == '-':

                moves.append(self._letters[letter_number] + str(piece_num - num2))
                num2 += 1
                new_piece_num2 -= 1
            else:
                break




        new_let_num3 = letter_number
        num3 = 2
        moves.append(self._letters[letter_number - 1] + str(piece_num))

        while new_let_num3 > 2:
            if self._board[self._letters[letter_number - num3]][piece_num - 1] == '-' and \
                    self._board[self._letters[letter_number - num3]][piece_num] == '-' and \
                    self._board[self._letters[letter_number - num3]][piece_num + 1] == '-':

                moves.append(self._letters[letter_number - num3] + str(piece_num))
                num3 += 1
                new_let_num3 -= 1
            else:
                break




        new_let_num4 = letter_number
        num4 = 2
        moves.append(self._letters[letter_number + 1] + str(piece_num))

        while new_let_num4 < 17:
            if self._board[self._letters[letter_number + num4]][piece_num - 1] == '-' and \
                    self._board[self._letters[letter_number + num4]][piece_num] == '-' and \
                    self._board[self._letters[letter_number + num4]][piece_num + 1] == '-':

                moves.append(self._letters[letter_number + num4] + str(piece_num))
                num4 += 1
                new_let_num4 += 1
            else:
                break


        new_let_num5 = letter_number
        new_piece_num5= piece_num
        num5 = 2
        num51 = 1
        num52 = 0
        moves.append(self._letters[letter_number - 1] + str(piece_num - 1))

        while new_let_num5 > 2 and new_piece_num5 > 1:
            if self._board[self._letters[letter_number - num52]][piece_num - num5] == '-' and \
                self._board[self._letters[letter_number - num51]][piece_num - num5] == '-' and \
                self._board[self._letters[letter_number - num5]][piece_num -num5] == '-' and \
                self._board[self._letters[letter_number - num5]][piece_num - num51] == '-' and \
                self._board[self._letters[letter_number - num5]][piece_num - num52] == '-':

                moves.append(self._letters[letter_number - num5] + str(piece_num-num5))
                num5 += 1
                num51 += 1
                num52 += 1
                new_let_num5 -= 1
                new_piece_num5 -= 1
            else:
                break



        new_let_num6 = letter_number
        new_piece_num6 = piece_num
        num6 = 2
        num61 = 1
        num62 = 0
        moves.append(self._letters[letter_number + 1] + str(piece_num + 1))

        while new_let_num6 < 17 and new_piece_num6 < 18:
            if self._board[self._letters[letter_number + num62]][piece_num + num6] == '-' and \
                    self._board[self._letters[letter_number + num61]][piece_num + num6] == '-' and \
                    self._board[self._letters[letter_number + num6]][piece_num + num6] == '-' and \
                    self._board[self._letters[letter_number + num6]][piece_num + num61] == '-' and \
                    self._board[self._letters[letter_number + num6]][piece_num + num62] == '-':

                moves.append(self._letters[letter_number + num6] + str(piece_num + num6))
                num6 += 1
                num61 += 1
                num62 += 1
                new_let_num6 += 1
                new_piece_num6 += 1
            else:
                break



        new_let_num7 = letter_number
        new_piece_num7 = piece_num
        num7 = 2
        num71 = 1
        num72 = 0
        moves.append(self._letters[letter_number - 1] + str(piece_num + 1))

        while new_let_num7 > 2 and new_piece_num7 < 18:
            if self._board[self._letters[letter_number - num72]][piece_num + num7] == '-' and \
                    self._board[self._letters[letter_number - num71]][piece_num + num7] == '-' and \
                    self._board[self._letters[letter_number - num7]][piece_num + num7] == '-' and \
                    self._board[self._letters[letter_number - num7]][piece_num + num71] == '-' and \
                    self._board[self._letters[letter_number - num7]][piece_num + num72] == '-':

                moves.append(self._letters[letter_number - num7] + str(piece_num + num7))
                num7 += 1
                num71 += 1
                num72 += 1
                new_let_num7 -= 1
                new_piece_num7 += 1
            else:
                break



        new_let_num8 = letter_number
        new_piece_num8 = piece_num
        num8 = 2
        num81 = 1
        num82 = 0
        moves.append(self._letters[letter_number + 1] + str(piece_num - 1))

        while new_let_num8 < 17 and new_piece_num8 > 1:
            if self._board[self._letters[letter_number + num82]][piece_num - num8] == '-' and \
                    self._board[self._letters[letter_number + num81]][piece_num - num8] == '-' and \
                    self._board[self._letters[letter_number + num8]][piece_num - num8] == '-' and \
                    self._board[self._letters[letter_number + num8]][piece_num - num81] == '-' and \
                    self._board[self._letters[letter_number + num8]][piece_num - num82] == '-':

                moves.append(self._letters[letter_number + num8] + str(piece_num - num8))
                num8 += 1
                num81 += 1
                num82 += 1
                new_let_num8 += 1
                new_piece_num8 -= 1
            else:
                break

        return moves



    def set_current_state(self):
        '''Sets the current state to current player won.'''
        if self._current_player == "BLACK":
            self._current_state = "BLACK_WON"

        if self._current_player == "WHITE":
            self._current_state = "WHITE_WON"



    def find_possible_moves(self, game_piece, piece_loc):
        '''Called by make_move using a game_piece parameter.  Finds all legal moves depending on layout of game_piece.
          Returns false if attempted move is not one of the allowed moves.'''
        moves = []
        letter_number = self.get_letter_num(piece_loc)
        piece_num = int(piece_loc[1:])

        if game_piece[1][1] != "-":
            return self.find_poss_center_moves(game_piece, piece_loc)

        if game_piece[0][0] != "-":
            new_let_num1 = letter_number
            new_piece_num1 = piece_num
            counter1 = 0
            num1=1

            while counter1 < 3 and new_let_num1 > 0 and new_piece_num1 >0:
                counter1 += 1
                moves.append(self._letters[letter_number-num1] + str(piece_num-num1))
                num1 +=1
                new_let_num1 -= 1
                new_piece_num1 -= 1


        if game_piece[0][1] != "-":

            new_let_num2 = letter_number
            counter2 = 0
            num2 = 1
            while counter2 < 3 and new_let_num2 > 0:
                counter2 += 1
                moves.append(self._letters[letter_number - num2] + str(piece_num))
                num2 += 1
                new_let_num2 -= 1


        if game_piece[0][2] != "-":

            new_let_num3 = letter_number
            new_piece_num3 = piece_num
            counter3 = 0
            num3 = 1

            while counter3 < 3 and new_let_num3 > 0 and new_piece_num3 < 19:
                counter3 += 1
                moves.append(self._letters[letter_number - num3] + str(piece_num + num3))
                num3 += 1
                new_let_num3 -= 1
                new_piece_num3 += 1


        if game_piece[1][0] != "-":


            new_piece_num4 = piece_num
            counter4 = 0
            num4 = 1

            while counter4 < 3 and new_piece_num4 > 0:
                counter4 += 1
                moves.append(self._letters[letter_number] + str(piece_num - num4))
                num4 += 1
                new_piece_num4 -= 1



        if game_piece[1][2] != "-":


            new_piece_num6 = piece_num
            counter6 = 0
            num6 = 1

            while counter6 < 3 and new_piece_num6 < 19:
                counter6 += 1
                moves.append(self._letters[letter_number] + str(piece_num + num6))
                num6 += 1
                new_piece_num6 += 1

        if game_piece[2][0] != "-":

            new_let_num7 = letter_number
            new_piece_num7 = piece_num
            counter7 = 0
            num7 = 1

            while counter7 < 3 and new_let_num7 < 19 and new_piece_num7 > 0:
                counter7 += 1
                moves.append(self._letters[letter_number + num7] + str(piece_num - num7))
                num7 += 1
                new_let_num7 += 1
                new_piece_num7 -= 1


        if game_piece[2][1] != "-":

            new_let_num8 = letter_number
            counter8 = 0
            num8 = 1

            while counter8 < 3 and new_let_num8 < 19:
                counter8 += 1
                moves.append(self._letters[letter_number + num8] + str(piece_num))
                num8 += 1
                new_let_num8 += 1



        if game_piece[2][2] != "-":

            new_let_num9 = letter_number
            new_piece_num9 = piece_num
            counter9 = 0
            num9 = 1

            while counter9 < 3 and new_let_num9 < 19 and new_piece_num9 < 19:

                counter9 += 1
                moves.append(self._letters[letter_number + num9] + str(piece_num + num9))
                num9 += 1
                new_let_num9 += 1
                new_piece_num9 += 1

        return moves


    def find_poss_center_moves(self, game_piece, piece_loc):
        '''Finds all moves if game_piece has a center piece.  Center piece allows for moving more than just 3 spaces.'''
        moves = []
        letter_number = self.get_letter_num(piece_loc)
        piece_num = int(piece_loc[1:])

        if game_piece[0][0] != "-":
            new_let_num1 = letter_number
            new_piece_num1 = piece_num
            num1 = 1

            while new_let_num1 > 0 and new_piece_num1 > 0:
                moves.append(self._letters[letter_number - num1] + str(piece_num - num1))
                num1 += 1
                new_let_num1 -= 1
                new_piece_num1 -= 1

        if game_piece[0][1] != "-":

            new_let_num2 = letter_number

            num2 = 1
            while new_let_num2 > 0:

                moves.append(self._letters[letter_number - num2] + str(piece_num))
                num2 += 1
                new_let_num2 -= 1

        if game_piece[0][2] != "-":

            new_let_num3 = letter_number
            new_piece_num3 = piece_num

            num3 = 1

            while new_let_num3 > 0 and new_piece_num3 < 19:

                moves.append(self._letters[letter_number - num3] + str(piece_num + num3))
                num3 += 1
                new_let_num3 -= 1
                new_piece_num3 += 1

        if game_piece[1][0] != "-":

            new_piece_num4 = piece_num

            num4 = 1

            while new_piece_num4 > 0:
                moves.append(self._letters[letter_number] + str(piece_num - num4))
                num4 += 1
                new_piece_num4 -= 1

        if game_piece[1][2] != "-":

            new_piece_num6 = piece_num

            num6 = 1

            while new_piece_num6 < 19:

                moves.append(self._letters[letter_number] + str(piece_num + num6))
                num6 += 1
                new_piece_num6 += 1

        if game_piece[2][0] != "-":

            new_let_num7 = letter_number
            new_piece_num7 = piece_num

            num7 = 1

            while new_let_num7 < 19 and new_piece_num7 > 0:

                moves.append(self._letters[letter_number + num7] + str(piece_num - num7))
                num7 += 1
                new_let_num7 += 1
                new_piece_num7 -= 1

        if game_piece[2][1] != "-":

            new_let_num8 = letter_number

            num8 = 1

            while new_let_num8 < 19:

                moves.append(self._letters[letter_number + num8] + str(piece_num))
                num8 += 1
                new_let_num8 += 1

        if game_piece[2][2] != "-":

            new_let_num9 = letter_number
            new_piece_num9 = piece_num

            num9 = 1

            while new_let_num9 < 19 and new_piece_num9 < 19:

                moves.append(self._letters[letter_number + num9] + str(piece_num + num9))
                num9 += 1
                new_let_num9 += 1
                new_piece_num9 += 1

        return moves


    def adjust_coordinate(self, xy):
        '''Is called through make_move, takes an xy coordinate and subtracts one from the number value on coordinate.
        This is done because list positioning starts at 0 but the game board starts at 1.'''
        num = int(xy[1:])
        num_str = str(num - 1)
        p = xy[0] + num_str
        return p


    def replace(self, location, game_piece, board):
        '''Is called by make_move.  Takes location and game_piece parameters.  calls get_letter_num method.
          replaces first 3x3 parameters with second 3x3 parameter'''
        let_num = self.get_letter_num(location)

        piece_num = int(location[1:])


        board[self._letters[let_num - 1]][piece_num - 1] = game_piece[0][0]
        board[self._letters[let_num - 1]][piece_num] = game_piece[0][1]
        board[self._letters[let_num - 1]][piece_num + 1] = game_piece[0][2]

        board[self._letters[let_num]][piece_num - 1] = game_piece[1][0]
        board[self._letters[let_num]][piece_num] = game_piece[1][1]
        board[self._letters[let_num]][piece_num + 1] = game_piece[1][2]

        board[self._letters[let_num + 1]][piece_num - 1] = game_piece[2][0]
        board[self._letters[let_num + 1]][piece_num] = game_piece[2][1]
        board[self._letters[let_num + 1]][piece_num + 1] = game_piece[2][2]


    def game_piece(self, piece):
        '''Called by make_move. Takes a piece parameter.  Creates a 3x3 game piece using a list of lists.  Calls method get_letter_num to find position of letter in alphabet.
          Uses self._board to take 3x3 square form board and add it to new list. which serves as the game_piece.'''
        letter_num = self.get_letter_num(piece)
        piece_num = int(piece[1:])

        new_piece = []

        row1 = []
        row2 = []
        row3 = []

        row1.append(self._board[self._letters[letter_num - 1]][piece_num - 1])
        row1.append(self._board[self._letters[letter_num - 1]][piece_num])
        row1.append(self._board[self._letters[letter_num - 1]][piece_num + 1])

        row2.append(self._board[self._letters[letter_num]][piece_num - 1])
        row2.append(self._board[self._letters[letter_num]][piece_num])
        row2.append(self._board[self._letters[letter_num]][piece_num + 1])

        row3.append(self._board[self._letters[letter_num + 1]][piece_num - 1])
        row3.append(self._board[self._letters[letter_num + 1]][piece_num])
        row3.append(self._board[self._letters[letter_num + 1]][piece_num + 1])

        new_piece.append(row1)
        new_piece.append(row2)
        new_piece.append(row3)

        return new_piece

    def check_if_legal_piece(self, piece):
        '''Called by make_move. Takes a piece parameter. Checks to see if stones from opposite team is in 3x3 game piece.  If opposing stone is
        in piece then False is returned.'''
        if self._current_player == "BLACK":
            for x in range(3):
                if "o" in piece[x]:
                    return False
        else:
            for x in range(3):
                if "x" in piece[x]:
                    return False

        return True

    def get_letter_num(self,coordinate):
        '''Returns number position of letter in alphabet. Takes coordinate parameter'''
        x = self._letters[0]
        counter = 0
        while x != coordinate[0]:
            counter += 1
            x = self._letters[counter]

        return counter

    def print_board(self):
        '''Prints the board.'''
        for key in self._board.keys():
            print(key, self._board[key])

    def check_for_ring(self, user, board):
        '''Called by make_move with user parameter.  iterates through self._board until it hits a stone of the user then calls ring method.
        returns true at the end if a ring is found otherwise False.'''

        if user == "BLACK":
            stone = 'x'

        if user == "WHITE":
            stone = "o"

        for letter in 'abcdefghijklmnopqr':
            list = [i for i in range(len(board[letter])) if board[letter][i] in stone]

            if self.ring(list, letter, stone, board):
                return True
        return False




    def current_player(self):
        '''Called by make_move.  Changes current player to the opposing player.'''

        if self._current_player == "BLACK":
            self._current_player = "WHITE"
            self._not_current_player = "BLACK"
            return

        if self._current_player == "WHITE":
            self._current_player = "BLACK"
            self._not_current_player = "WHITE"
            return

    def empty_outer_ring(self):
        '''At the end of each turn, removes all pieces in the outer ring of the game board.  Pieces can be moved there
        on a turn, but they are removed at the end of the turn.'''
        for x in range(0,20):
            self._board['a'][x] = '-'

        for y in range(0,20):
            self._board['t'][y] = '-'

        l=[0,19]
        for z in l:
            for letter in 'bcdefghijklmnopqrs':
                self._board[letter][z]= '-'

    def ring(self, list, letter, stone, board):
        '''Called by check_for_ring.  Takes location of stone and checks the layout of surrounding stones on self._board
        to see if there is a ring.  returns true if there is otherwise False.'''


        let_num = self.get_letter_num(letter)

        for i in list:

            if board[self._letters[let_num]][i] == stone and board[self._letters[let_num]][i+1] == stone and \
                board[self._letters[let_num]][i + 2] == stone and board[self._letters[let_num + 1]][i] == stone and \
                board[self._letters[let_num + 1]][i + 1] == '-' and board[self._letters[let_num + 1]][i + 2] == stone \
                and board[self._letters[let_num + 2]][i] == stone and board[self._letters[let_num + 2]][i + 1] == stone \
                and board[self._letters[let_num + 2]][i + 2] == stone:



                return True

        return False

