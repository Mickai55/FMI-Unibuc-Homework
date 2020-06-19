.data
	n: .word 938
	s: .word 0
.text
main:
	lw $t0,n
	li $t1,10
	li $t4, 0

imparte:
	div $t0,$t1             #mflo = n/10 and mfhi = n%10
	mflo $t0		#t0 = n/10
	mfhi $t3                #t3 = n%10
	add $t4,$t4,$t3         #s=s+digit
	bne $t0, 0, imparte     #if n!=0

sfarsit:
	sw $t4,s
	li $v0,10
	syscall
