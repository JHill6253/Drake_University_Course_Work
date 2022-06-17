# sorting.asm
#   A MIPS program that sorts an array of integers
#
# Author:
#   John Hill

######################################################################

.data
arr: .word 7, 2, 1, 3, 4, 5, 8, 6, 9, 0

######################################################################

.text
main:
    la $s0, arr             # $s0 holds address of arr
    addi $s1, $zero, 10     # $s1 holds value of size
    
    addi $a0, $s0, 0        # calls isort(arr, size)
    addi $a1, $s1, 0
    jal isort

    addi $a0, $s0, 0        # calls the print function
    addi $a1, $s1, 0        # to print off all the
    jal print               # elements of arr

    addi $v0, $zero, 17     # Ends the program via a
    syscall                 # system call

######################################################################

print:
    addi $t0, $a0, 0
    addi $t1, $a1, 0
    addi $v0, $zero, 1

    print_while:
        beq $t1, $zero, print_done
        
        lw $a0, 0($t0)      # since $v0 = 1, this
        syscall             # prints $a0 as an int

        addi $t0, $t0, 4    # arr = arr + 1
        addi $t1, $t1, -1   # size = size - 1

        j print_while

    print_done:
        jr $ra

######################################################################
# All of your solutions should go below
#
# NOTE: Any code that you modify above this line should be restored
#       before you submit your assignment
######################################################################

isort:
	addi $t5, $zero, 1 #sets reg $t5 to 1 which serve as the counter
	
	loop: slt $t6, $t5, $a1 #set less than $t6 
	      beq $t6, $zero, exit #branch if equal $t6 $zero
		
	      addi $sp , $sp, -8 #Setting point stacker 
	      sw $ra, 0($sp) # storing return address stack pointer
	      sw $a1, 4($sp) #store word for  4 positions form the stack pointer 
	      addi $a1, $t5, 0 #Add immediate  $a1 $t5 and 0
	      jal insert_left
		
	      lw $ra, 0($sp) 
	      lw $a1, 4($sp)
	      addi $sp, $sp, 8
	
	      addi $t5, $t5, 1
	      j loop
		
	exit: jr $ra  # Put your solution to isort here

######################################################################

insert_left:
    	sll $t1, $a1,2 # setting reg $t1 = i * 
	add $t1, $a0, $t1 # adding reg $t1 + i *4
	
	lw $t0, 0($t1) # loading reg $t0 (temp) = arr[i]
	lw $t2, -4($t1)# loading reg $t2 = arr[i-1]
	
	slt $t3,$zero, $a1 #set $t3 to 0 if $t2 is less than 
	slt $t4, $t0, $t2 #set $t4 to 0 if  $t0 is less than 
	beq $t3, $zero, Exit #if equal exit 
	beq $t4, $zero, Exit #if equal exit 
	
	addi $sp, $sp, -4 #change stack pointer 
	sw $ra, 0($sp) # store stack pointer 
	jal swap # call jal swap
	
	lw $ra, 0($sp)# load word $a2
	addi $sp, $sp, 4 #resseting stack pointer
	addi $a1, $a1, -1 #Setting parameter for insert_left 
	j insert_left # call j insert left 
	
	Exit: jr $ra  # Put your solution to insert_left here

######################################################################

swap:
	sll $t1, $a1,2 # setting reg $t1 = i * 4
	add $t1, $a0, $t1 # adding reg $t1 + i *4
	
	lw $t0, 0($t1) # loading reg $t0 (temp) = arr[i]
	lw $t2, -4($t1)# loading reg $t2 = arr[i-1]
	
	sw $t2, 0($t1) # store word arr[i] = reg $t2
	sw $t0, -4($t1) # store word arr[i-1] = reg $t0 (temp)
	
    	jr $ra  # Put your solution to swap here
