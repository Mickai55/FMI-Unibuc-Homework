.data
	suma:.space 4
	n:.word 5
	x:.word 1 2 3 4 5
.text,
main:
	lw $t2,n
	li $t1,0
	li $t0,0
for:
	beq $t1,$t2,iesire
	add $t3,$t1,$t1
	add $t3,$t3,$t3
	lw $t3,x($t3)
	add $t0,$t0,$t3
	add $t1,$t1,1
	j for
iesire:
	sw $t0,suma
	li $v0,1
	add $a0,$zero,$t0 
	syscall # pentru afisare in consola
	li $v0,10
	syscall	 	 	
