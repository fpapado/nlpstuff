#!/bin/python3
import click

# Minimum edit distance implementation that fills out and prints the costs
# table. Does not keep backpointers at the moment.

# This script is particularly suited for ANLP students that have not taken many
# programming classes and might be wondering how to implement this with simple
# Python constructs. I'm sure you could be smarter / more efficient, but the
# focus is on a simple implementation that follows the logic in the slides.

# Any python sidenotes are prefixed as 'PX' and presented at the end

# Sample usage:
# $python
# from find_edit import find_edit_distance
# find_edit_distance('stall', 'table')
# Or use the command line:
# python find_edit_distance --w1="word1" --w2="word2"

# Costs are placed here for customisation.
# Might want to try 'rep': 1 for Levenshtein distance
costs = {'del': 1, 'ins': 1, 'rep': 2}


# Main function and loop; using click annotations for cli use, but feel free
# to just use the interpreter
@click.command()
@click.option('--w1', prompt="First word", help='First word')
@click.option('--w2', prompt="Second word", help='Second word')
@click.option('--log', default=True, help='Logging')
@click.option('--printfinal', default=True, help='Print final costs')
def find_edit_distance(w1, w2, log=True, printfinal=True):
    # Need to initialise the table first
    costs_table = init_costs_table(w1, w2)

    # Visualise
    if (log is True):
        pretty_print_table(costs_table)

    # P1
    # Loop over the columns, row-by-row
    for column_i in range(len(costs_table)):
        for row_i in range(len(costs_table[column_i])):
            costs_table[row_i][column_i] = min_distance(
                costs_table, row_i, column_i, w1, w2)
            if (log is True):
                pretty_print_table(costs_table)

    # Visualise the table at the end
    if (printfinal is True):
        pretty_print_table(costs_table)

    return costs_table


# Find minimum distance given the three possible moves and "previous" costs
def min_distance(costs_table, row_i, column_i, w1, w2):
    candidates = []

    # Moving down means we have a deletion cost, plus previous cost
    # Does nothing if first row
    if (row_i != 0):
        cost_from_up = costs_table[row_i - 1][column_i] + costs['del']
        candidates.append(cost_from_up)

    # Moving right means we have an insertion cost, plus previous cost
    # Does nothing if first column
    if (column_i != 0):
        cost_from_left = costs_table[row_i][column_i - 1] + costs['ins']
        candidates.append(cost_from_left)

    # Moving diagonally has two cases
    if (row_i != 0 and column_i != 0):

        # P2, P3
        # If the letters match ('identity')
        if(w1[row_i - 1] == w2[column_i - 1]):
            cost_topleft = costs_table[row_i - 1][column_i - 1]

        # Else, we replace
        else:
            cost_topleft = costs_table[row_i - 1][column_i - 1] + costs['rep']

        candidates.append(cost_topleft)

    # Return the minimum cost; this is a built-in Python function on list
    if (candidates):
        return min(candidates)

    # If no candidates (top-left-most corner), we return 0
    else:
        return 0


# Construct table with identities and empty start
def init_costs_table(w1, w2):
    costs_table = []

    # Notice we add 1, to account for the 'empty' cell at the start
    for i in range(len(w1) + 1):
        row = []

        for j in range(len(w1) + 1):
            row.append(0)

        costs_table.append(row)

    return costs_table


# Print each row on its own line
def pretty_print_table(table):
    for row in table:
        print(row)

    # Empty line, for good measure
    print()


if __name__ == '__main__':
    find_edit_distance()


# === Sidenotes ===
# P1: Range(x, y) is a Python function that produces an iterable series of
# numbers (in this case, the indices). We can easily iterate over such a
# series with the for ... in ... notation

# P2: We can index strings in Python, e.g. 'table'[0] gives 't'

# P3: We subtract 1 in indexing here, because our table has an extra row
# and column, which our strings don't have

# P4: Again, we use the for ... in range(...) to handily loop

# P5: Note that we can use for ... in ... with a list (any 'iterable', in fact)
# and access the objects directly without referencing their indexes
