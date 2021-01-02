def pattern(input_char = "*", line_count = 5, display_mode = "RIGHT"):
    #BEGIN your code
    
    a = display_mode
    if a == "RIGHT":
        for x in range(line_count):
            print('  '*(line_count-x-1)+ input_char* (2*x+1))
    if a == "LEFT":
        for x in range(line_count):
            print(''*(line_count-x-1)+ input_char* (2*x+1))
    if a == "CENTER":
        for x in range(line_count):
            print(' '*(line_count-x-1)+ input_char* (2*x+1))
    


    #END your code
    
    

# Assignment 10  test cases

#Test Case 1
print('Test Case 1:  pattern("*",5,"RIGHT")')
pattern("*",5,"RIGHT")

#Test Case 2
print('Test Case 2:  pattern("@",6,"LEFT")')
pattern("@",6,"LEFT")

#Test Case 3
print('Test Case 3:  pattern("#",10,"CENTER")')
pattern("#",10,"CENTER")

#Test Case 4 with all defaults
print('Test Case 4: pattern()')
pattern( )

#Test Case 5 pass in only two params and third is a default
print('Test Case 4: pattern("X", 5)')
pattern("X",5)

#Test Case 6: Take the inputs from the user on all three 
# and use those to test your method
a = input("Enter your character? ")
b = input("How many lines do you need? ")
c = input("How do you want to justify the display (LEFT, RIGHT, CENTER)? ")
b = int(b)
pattern(a,b,c)
