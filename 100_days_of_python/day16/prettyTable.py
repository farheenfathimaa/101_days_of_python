from prettytable import *
table=PrettyTable()
table.add_column("name",['bob','john','patrick'])
table.align = "l"
table.add_column("marks",[89,43,67])
print(table)