'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab 5 : Playing with a Text File

This is the program for Lab 5. It must be run through the command line. 
It takes input from one text file and writes the changed input in a different file.
'''

import sys

'''
This is a simple usage message function.
If the user enters incorrect values, it will print and remind the user how to run the program.
It has no parameters.
It returns several printed strings. 
'''
def usage_msg():
    print("This program needs four arguments to run. It is run in the command line.")
    print("The first argument should be the name of the program file (textFileManip.py).")
    print("The second argument should be the name of the file you want to use as your input file.")
    print("The third argument should be the name of the file you want to use as your output file.")
    print("The fourth argument should be the function number you want to run. Here are your options:")
    print("...'1' for the all_upper_case function, which will convert everything in input file to upper case and saves it in output file.")
    print("...'2' for the remove_a_word function, which gets as input a word or letter, removes it from the input file, and creates an output file without that word.")
    print("...'3' for the reverse_file function, which reverses (by word) the input file and writes it in the output file.")
    print("...'4' for the pattern_count function, which gets as input a word or letter, checks the input file, and then prints how many times it occurs in the output file.")
    print("...'5' for the encode_file function, which writes all the data out to the new file but shifts each letter forward by one.")
    print("...'6' for the decode_file function, which reverses the output from the encode_file function.")
    print("To run the program, make sure you use this format: input file name, output file name, function number")

'''
This function will change text to all uppercase. 
It takes an input file (in_file) as the first parameter, which contains the text that will be changed.
It takes an output file (out_file) as the second parameter, which is where the new text is written.
It returns the new text as a sequence of strings in the output file.
'''
def all_upper_case(in_file, out_file):
    file_in = open(in_file,"r") 
    input_contents = file_in.read() 
    file_in.close()
    changed_input = input_contents.upper() 
    file_out = open(out_file,"w") 
    file_out.writelines(changed_input)
    file_out.close()

'''
This function will remove all instances of a string from a text file. 
It takes an input file (in_file) as the first parameter, which contains the text that will be changed.
It takes an output file (out_file) as the second parameter, which is where the new text is written.
The third parameter is the input string from the user which will be removed from the text file. 
It returns the new text as a list of strings in the output file, with the string from the third parameter removed.
'''
def remove_a_word(in_file, out_file, input_to_remove):
    file_in = open(in_file,"r") # look here 
    input_contents = file_in.read() 
    file_in.close()
    changed_input = input_contents.split(input_to_remove) 
    file_out = open(out_file,"w") 
    file_out.writelines(changed_input) 
    file_out.close()

'''
This function will reverse the text (by word) in a file. 
It takes an input file (in_file) as the first parameter, which contains the text that will be changed.
It takes an output file (out_file) as the second parameter, which is where the new text is written.
It returns the new text as a sequence of strings in the output file.
'''
def reverse_file(in_file, out_file):
    file_in = open(in_file,"r")
    input_contents = file_in.read()
    file_in.close()
    input_list = input_contents.split(' ')
    input_reversed = ' '.join(reversed(input_list)) 
    file_out = open(out_file,"w") 
    file_out.writelines(input_reversed)
    file_out.close() 

'''
This function will count the instances of a string in the text file. 
It takes an input file (in_file) as the first parameter, which contains the text that will be changed.
It second parameter is an input string from the user which will be counted in the text file. 
It returns an integer value for the number of times the string appeared in the text file.
'''
def pattern_count(in_file,input_to_count):
    file_in = open(in_file,"r")
    input_contents = file_in.read()
    print(input_contents.count(input_to_count))
    file_in.close()

'''
This function will shift each letter forward by one (example: a --> b). 
It takes an input file (in_file) as the first parameter, which contains the text that will be changed.
It takes an output file (out_file) as the second parameter, which is where the new text is written.
It returns the new text as a list of strings in the output file.
'''
def encode_file(in_file,out_file):
    file_in = open(in_file,"r")
    input_contents = file_in.read() 
    file_in.close()
    input_list = []
    input_list[:0] = input_contents
    count = 0
    while count < len(input_list):
        if (65 <= (ord(input_list[count])) < 90): # character conversion, move forward and then loop back around
            input_list[count] = chr(ord(input_list[count])+1)
            count += 1
        elif (97 <= (ord(input_list[count])) < 122):
            input_list[count] = chr(ord(input_list[count])+1)
            count += 1
        elif (ord(input_list[count]) == 90):
            input_list[count] = chr(65)
            count += 1
        elif (ord(input_list[count]) == 122):
            input_list[count] = chr(97)
            count += 1
        else:
            count += 1
    file_out = open(out_file,"w") 
    file_out.writelines(input_list)
    file_out.close()

'''
This function will shift each letter backward by one (example: b --> a). 
It only takes the output file (out_file) as a parameter, since the purpose of this function is to undo the encode function.
It takes the text from output file, changes it, and then writes over the previous text in the same output file.
It returns the new text as a list of strings in the output file.
'''
def decode_file(out_file):
    file_in = open(out_file,"r")
    input_contents = file_in.read() 
    file_in.close()
    input_list = []
    input_list[:0] = input_contents
    count = 0
    while count < len(input_list):
        if (65 < (ord(input_list[count])) <= 90):
            input_list[count] = chr(ord(input_list[count])-1)
            count += 1
        elif (97 < (ord(input_list[count])) <= 122):
            input_list[count] = chr(ord(input_list[count])-1)
            count += 1
        elif (ord(input_list[count]) == 65):
            input_list[count] = chr(90)
            count += 1
        elif (ord(input_list[count]) == 97):
            input_list[count] = chr(122)
            count += 1
        else:
            count += 1
    file_out = open(out_file,"w") 
    file_out.writelines(input_list)
    file_out.close()

'''
This is the driver function. It is meant to be run through the command line.
It can only be run if the command line lists four arguments, otherwise it will return the usage message.
The fourth argument must be a number between 1 and 6. 
'''
def main():
    if len(sys.argv) == 4:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
        fun_call = sys.argv[3]
        if fun_call == "1":
            all_upper_case(in_file, out_file)
            print("you entered 1, the all_upper_case function")
        elif fun_call == "2":
            input_to_remove = input("What would you like to remove?\n: ")
            remove_a_word(in_file,out_file,input_to_remove)
            print("you entered 2, the remove_a_word function")
        elif fun_call == "3":
            reverse_file(in_file, out_file)
            print("you entered 3, the reverse_file function")
        elif fun_call == "4":
            pattern_count(in_file,input("What word or letter would you like to count?\n: "))
            print("you entered 4, the pattern_count function")
        elif fun_call == "5":
            encode_file(in_file, out_file)
            print("you entered 5, the encode_file function")
        elif fun_call == "6":
            decode_file(out_file)
            print("you entered 6, the decode_file function")
        else:
            print("The function options are 1, 2, 3, 4, 5, or 6.")
    else:
        usage_msg()
main()