.data
	n: .word 32
	rez: .space 4
.text
main:
	lw $t0, n
	sub $sp, $sp, 4
	sw $t0, 0($sp) #push(n)
	jal suma

	lw $t0, 0($sp)
	sw $t0, rez

	addi $sp, $sp, 4 # pop(suma(n))

	li $v0, 1
	lw $a0, rez
	syscall # printf("%d", rez);
	li $v0, 10
	syscall

suma:
	sub $sp, $sp, 4
	sw $fp, 0($sp) #push($fp)
	move $fp, $sp

	sub $sp, $sp, 4
	sw $ra, 0($sp) #push($ra)

	lw $t0, 4($fp)
	beq $t0, $0, return0
	li $t1, 10
	rem $t2,$t0,$t1 # t2 = n%10

	sub $sp, $sp, 4
	sw $t2, 0($sp) #push($t2)

	div $t0, $t0, $t1 # t0 = t0/10 = n/10

	sub $sp, $sp, 4
	sw $t0, 0($sp) #push($t0)

	jal suma

	lw $t1,-12($fp) # suma(n/10)
	lw $t0,-8($fp) # n%10
	
	addi $sp, $sp, 4 # pop( suma(n/10) )
	addi $sp, $sp, 4 # pop( n%10 )

	add $t0, $t0, $t1

	lw $ra, -4($fp) # restauram $ra
	lw $fp, 0($fp) # restauram $fp

	addi $sp, $sp, 4 # pop( $ra )
	addi $sp, $sp, 4 # pop( $fp )

	sw $t0, 0($sp)
	jr $ra
return0:
	lw $ra, -4($fp) # restauram $ra
	lw $fp, 0($fp) # restauram $fp

	addi $sp, $sp, 4 # pop( $ra )
	addi $sp, $sp, 4 # pop( $fp )

	jr $ra
