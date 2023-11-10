glossary = {'Infinite loops':'An infinite loop is a loop that never ends.',
            'Variables':'Containers for storing data values.',
            'Constants':'These are variable whose values do not change.',
            'Operators':'Special symbols in python that perform arithmetic or logical computation.',
            'Comments':'These describe what is going on inside a program.',
            'Module':'A new file containing values or functions that are imported to the main file.',
            'Keywords':'These are the reserved words in Python.',
            'If statement':'It starts with the keyword if. The condition uses comparison or logical operators and ends the line with a colon(:).',
            'Strings':' These are sequences of characters surrounded by quotes.',
            'Loops':'Used when we want to execute code statements multiple times.'} #Contents inside the glossary

for key, value in glossary.items(): #This code will print all the keys inside the dictionary, followed by the value
    print(key+":", value,"\n")