# create a program that takes in student ID and name, and 3 grades.
# Average three grades and output it along with last name

# defining some stuff or else it'll get mad
id_name = []
name = ""

# main function to ask for id and name
def main(name):
    name = input("Please enter the student's ID and surname: ")
    s_name = name.split()
    id_name.append(s_name[1])

# average function, calculates the average of 3 grades
def average(a, b, c):
    sum = (a + b + c)/3
    sum = "%.1f" % sum  # thank God for stack overflow
    # round(sum, 1) <-- couldn't get this to for those 33.3333333333 sorta numbers...
    print(str(*id_name) + " " + str(sum))

# call main
main(name)

# prompt for average input
print("Please enter 3 grades.")

a = int(input("Grade 1: "))
b = int(input("Grade 2: "))
c = int(input("Grade 3: "))

# call average
average(a, b, c)

#done!

# personal note for future me:
# oh im making s_name a list and then appending a list into a new list
# so everytime i call [1]], i call s_name, because it's the only thing in the list :skull:
# corrected it now. just append the name ([2]) part of s_name into id_name.
# no need to append all of s_name to id_name








