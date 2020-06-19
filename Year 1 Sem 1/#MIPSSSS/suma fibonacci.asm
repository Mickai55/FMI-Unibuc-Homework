main:
li $a0, 5
j fib
fib:
bgt $a0, 1, body     # continua daca $a0 > 1
addi $v0, $zero, 1   # altfel return 1
addi $v1, $zero, 0
addi $t2, $zero, 0
beqz $ra, end   # if ($ra==0) 
jr $ra              # return body
body:
addi $sp, $sp, -16 # se aloca 4 registrii
sw $a0, 0($sp)     # $a0 = n, in stiva
sw $ra, 4($sp)     # se salveaza return in stiva

addi $a0, $a0, -1  # $a0 =  n - 1
jal fib            # fib(n-1) 
sw $v0, 8($sp)     # $v0 = fib(n-1)

lw $a0, 0($sp)     # se reseteaza $a0
addi $a0, $a0, -2  # $a0 = n - 2  
jal fib            # fib(n-2)
sw $v0, 12($sp)    # $v0 = fib(n-2)

lw $t0, 8($sp)     # $t0 = fib(n-1)
lw $t1, 12($sp)    # $t1 = fib(n-2)
lw $ra, 4($sp)
addi $sp, $sp, 16  
add $v1,$v1,$v0
add $v0, $t0, $t1  # $v0 = fib(n-1) + fib(n-2)
add $t2,$v0,$v1

beqz $ra, end # daca $ra==0 se termina programul
jr $ra             # jump to return address

end:

