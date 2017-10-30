#! /usr/bin/python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(theTable):
    # For simplicity we don't check boundaries of lists.
    outputColumnCounter = len(theTable)
    outputRowCounter = len(theTable[0])
    columnWidths = [0]*outputColumnCounter
    
    # Calculate widths of output columns.
    for i in range(outputColumnCounter):
        for j in range(len(theTable[i])):
            if (columnWidths[i] < len(theTable[i][j])):
                columnWidths[i] = len(theTable[i][j])

    # Start printing.
    for j in range(outputRowCounter):
        for i in range(outputColumnCounter):
            print(theTable[i][j].rjust(columnWidths[i]+1), end='')
        print()

printTable(tableData)