#Stack Trace -> Also known as "Traceback" is the scary-looking error message that the python interpreter prints after encountering some mistakes in the code.
#You should read from the bottom-most to top-most.

'''"""
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    start_battle()
  File "main.py", line 7, in start_battle
    cast_spell("hundred")
  File "main.py", line 3, in cast_spell
    return current_health - damage_amount
TypeError: unsupported operand type(s) for -: 'int' and 'str'
"""'''

#How to break down the problem :-

#The Bottom Lines (the 'what'):- It tells the exact type of error.
#The Middle Lines (the 'where'):- It tells the exact place (like file or line) where the error have occured.
#The Top Lines (the 'how') -> It tells about the historical chain that which part crashed.