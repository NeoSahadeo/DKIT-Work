#!/bin/bash

# A Few Notes For SysAdmin MCQ

#-----------------------------------------------------------------------------------------------------
# 1. User input
# Syntax:
# 	read variable_name

# example:
echo "Enter username: "
read username
echo $username

# or with a single line:
read -p "Enter username: " username

#-----------------------------------------------------------------------------------------------------
# 2. Functions
# Syntax:
# 	function function_name(){
#			...
# 	}
# 	or
# 	function_name(){
#			...
# 	}

# example:
function hello_world(){
	echo "Hello World"
}

hello_world # This is how to call a function

# 2.1 Parameters
function hello_person(){
	echo "Hello $1"
}

hello_world Neo # This is how to call a function with parameters/arguments

# 2.2 Returning values
function return_me(){
	gamba=777
	echo $gamba # Use the 'echo' command to return a value
}

value=$(return_me)
echo $value

#-----------------------------------------------------------------------------------------------------
# 3. Conditionals
# Keynotes:
# 	-eq: Equal to
#		-gt: Greater than
#		-lt: Less than
#		-ne: Not equal to
#		-ge: Greater than or equal to
#		-le: Less than or equal to
#		-n : Not an empty string
#		-z : Empty string
#		-e : File exists
#		-d : Directory exists
#		-w : File is writable
#		-x : File is executable
#		== : Equal to
#		!= : Not equal to
#		>  : Greater than
#		<  : Less than
#		>= : Greater than or equal to
#		<= : Less than or equal to
#		&& : And
#		|| : Or
#		!  : Not
#
# Syntax:
# 	if [ condition ]; then
# 	fi

x=4
if [ $x -gt 5 ]; then
	echo True!
else
	echo UnTrue!
fi

# 3.1 if-elif

if [ $x -gt 5 ]; then
	echo "Larger than 5"
elif [ $x -eq 4 ]; then
	echo "The number is 4"
fi

# 3.2 number comparisons

if (( $x > 5 )); then
	echo True!
else
	echo Nah!
fi

#-----------------------------------------------------------------------------------------------------
# 4. Binary Operators
# Keynotes:
# 	+ : add
# 	- : minus
# 	* : multiply
# 	/ : divide
# 	% : modulus

#-----------------------------------------------------------------------------------------------------
# 5. Loops
# 2 types of loops:
# For-loops:
# 	for CONDITION; do
# 	done
# While-loops:
# 	while CONDITION; do
# 	done

# 5.1.1 For-loops with a 'condition'
for (( x=0; x < 10; x++ )); do
	echo $x
done

# 5.1.2 For-loops with a range
for x in {0..9}; do
	echo $x
done

# 5.1.3 For-loops with a range + step
for x in {0..9..2}; do # this will step in 2's, eg: 0,2,4,6,8
	echo $x
done

# 5.1.4 For-loop through an array
seasons=("summer" "spring" "winter" "fall")
for x in ${seasons[@]}; do
	echo $x
done

# 5.1.5 For-loop with a file
for x in $(cat ./notes.sh); do
	echo $x
done

# 5.2 While-loop
x=0
while (( x < 4 )); do
	echo $x
	(( x++ ))
done

#-----------------------------------------------------------------------------------------------------
# 6. Variables
#-----------------------------------------------------------------------------------------------------

# 6.1 Arrays, each element is seperated with a space
x=(1 2 3 4 5 6)
y=("Hello" "World")

# 6.2 Strings and numbers
x=0
y="String"

# 6.3 Boolean
x=true # 0
y=false # 1

#-----------------------------------------------------------------------------------------------------
# 7. Arguments
#-----------------------------------------------------------------------------------------------------

# 7.1 Passed-in
# eg: ./notes.sh argument1 argument2
echo $1 $2

# 7.2 Argument Count
echo $#

# 7.3 Arguments as strings; use "$@"
for x in ${@}; do
	echo $x
done

#-----------------------------------------------------------------------------------------------------
# 8. Good to know (or not; 😈)
#-----------------------------------------------------------------------------------------------------

# 8.1 How to generate a random number
# shuf -i start-end -n amount_of_numbers
shuf -i 1-20 -n 1

# 8.2 Password change in 1 line
user="Nemo"
"$user:1Password" | sudo chpasswd $user

# 8.3 Append and overwriting to a file
"Hello" > text.txt # overwrite
"Hello" >> text.txt # append
