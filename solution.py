assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

digits = cols

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

    # Select all box with two possibilities in it
    Value2Box = [ box for box in boxes if len(values[box])==2 ]
    for box in Value2Box:
        digitS = values[box]
        # Extract all present naked twins for this box 
        nakedTwins = [ peer for peer in peers[box] if peer in Value2Box and values[peer] == digitS]
        for nakedTwin in nakedTwins:
            # common peers
            commonPeers = [ peer for peer in peers[box] if peer in peers[nakedTwin] ]
            for commonPeer in commonPeers:
                # Remove the digits of the naked twins
                assign_value(values, commonPeer, ''.join( [ d for d in values[commonPeer] if d not in digitS ] ))
    return values
def cross(A, B):
    "Cross product of elements in A and elements in B."
    "Cross product of elements in A and elements in B."
#    return [a + b for a in A for b in B]

#BOXES = cross(ROWS, COLS)
#ROW_UNITS = [cross(r, COLS) for r in ROWS]
#COLUMN_UNITS = [cross(ROWS, c) for c in COLS]
#SQUARE_UNITS = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
#DIAGONAL_UNITS = [[row+col for (row,col) in zip(ROWS, COLS[::step])] for step in [-1,1]]
    return [s + t for s in A for t in B]

row_units = [cross(r, cols) for r in rows]

colum_units = [cross(rows, c) for c in cols]

square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]

diagonals = [[ rows[i] + cols[i] for i in range(len(rows)) ], [ rows[len(rows)-1-i] + cols[i] for i in range(len(rows)) ]] # main diagonals

unitlist = row_units + colum_units + square_units + diagonals # list of units, for each column, row and diagonals (only the two main diagonals)

boxes = cross(rows, cols) # every box

units = dict((s, [u for u in unitlist if s in u]) for s in boxes) # dictionary : row, colum and 3x3 for each box (included)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)  # dictionary : row, colum and 3x3 for each box (not included)

assignments = []

    

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = [ (digits if c == '.' else c) for c in grid ]
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        # Remove solved digit from the list of possible values for each peer
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = naked_twins(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
        return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    solved = search(values)
    if solved:
        return solved
    else:
        return False

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
