'''Takes a file, empties it and replaces it with text
   Simple text edior, created in python. 
   Warning: DO NOT try this on an important file
'''

from sys import argv #Imports from system libary the argv module

script, filename = argv #input filename, filename assigned to argv

print "File %r will be erased and replaced." % filename #Notifys user what file will be deleted

print "Do not erase, hit CTRL-C (^C)." # Allows user to exit

print "Erase and replace, ENTER" #Prompts user to proceed 

raw_input(">>> ")  #Question mark for input from user

print "Opening the file....%r" % filename #Notifys user what will be opened and replace
target = open(filename, 'w') #Opens file and allows content to be written

print "File %r will be erased and replaced by your text." % filename #Deletes/replaces file content

#target.truncate #Removes content from the file

print "Enter replacement text to input" 

line1 = raw_input("Replacement text >>> ") # First line of replacement text

#line2 = raw_input("line 2: ") # Second line of replacement text

#line3 = raw_input("line 3: ") # Third line of replacement text

print "The following",line1,'''line2,line3,''' "will be written to the file"

target.write(line1) # Replaces content of the file
target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")


print "Command completed successfully, File is now closing" #Prompts user
target.close() #Closes file 
