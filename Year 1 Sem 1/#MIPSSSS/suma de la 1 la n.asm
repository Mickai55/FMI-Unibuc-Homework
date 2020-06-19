.data
	n:.word 5
	s:.space 4
.text
main:
	lw $t2,n
	li $t1,1
	li $t0,0
for:
	add $t0,$t0,$t1
	add $t1,$t1,1
	bgt $t1,$t2,iesire
	j for
iesire:
	sw $t0,s
	li $v0,1
	add $a0, $0, $t0
	syscall
	li $v0,10
	syscall

		
	
