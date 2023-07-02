"""
Introduction to Programming: Coursework 1
Please write your name
@author:Rhea Prakash
"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle, wordlist):
    if valid_puzzle(puzzle) and valid_wordlist(wordlist):
        c = 0
        if c < len(wordlist):
            coloured_display(puzzle, get_positions(puzzle, wordlist[c]))
            c += 1
    else:
        print("ValueError, invalid puzzle or wordlist")


def valid_puzzle(lst_1):
    j = 1
    c = 0
    i = 0

    # Checking whether the length of each string in the puzzle is same
    for j in lst_1:
        if (len(lst_1[i]) == len(j)):
            continue
        else:
            c += 1
            break
    # Returing true if every condition is satisfied
    if j == lst_1[-1] and c == 0:

        return True
    else:
        return False


def valid_wordlist(string):
    c = 0
   # Using a loop to check if all words given in the wordlist are strings
    for i in string:
        if type(i) == str:
            continue
        else:
            c += 1

    if c > 0:
        return False
    else:
        return True


def get_positions(puzzle, word):
    word = word.upper()
    pos = []
    c = 1
    
  
    # finding the first letter of the word in the puzzle
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            for m in word:
                if m == puzzle[i][j]:
                   if  get_positions_down(puzzle, word, i, j, pos) != False :
                       return pos
    
    return word+" not found"             
          
             

def get_positions_down(puzzle, word, i, j, pos):
    for m in word:
         if m == puzzle[i][j]:
             p = (i, j)
             pos.append(p)
             if len(pos)==len(word):
              return pos
          
             i=i+1
             
             if i == len(puzzle):
                return False
             
             
         else:
            pos.clear()
            return False
    
    

def basic_display(lst_2):
    # Using two loops to display the given puzzle appropriately
    for i in lst_2:
        for j in i:
            j = j.upper()
            print("  ", j, end=" ")

        print("\n")


def coloured_display(puzzle, positions):
    # To print all letters at 'positions' in green in the grid
    flag=0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            for k in positions:
               for l in k:
                   if (i,j) == l:
                     print(f"\033[42m {puzzle[i][j]} \033[0m ", end=" ")
                    
            print("  ", puzzle[i][j], end=" ") 
            
        print("\n")      
                    
       
       


# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print(get_positions(puzzle1, "TESTING"))
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    # good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    good_wordlist2 = [ "tray" ]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually

    # basic solution
    test_valid_puzzle()
    test_valid_wordlist()
    # test_basic_display()
    

    # full solution
    test_coloured_display()
    test_get_positions()
    # test_wordsearch()
