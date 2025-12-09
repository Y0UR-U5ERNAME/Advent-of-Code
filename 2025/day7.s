    # MIPS32 assembly solution
    .data
arr:.space 21152 # 141*142+2 + 141*4*2

    .text
add64:
    addu $v0, $a0, $a2
    sltu $v1, $v0, $a0
    addu $v1, $v1, $a1
    addu $v1, $v1, $a3
    jr $ra

main:
    addi $sp, $sp, -4
    sw $ra, 0($sp)

    la $a0, arr
    li $a1, 142 # 141+1
    li $t0, 142
    li $v0, 8
read:
    beq $t0, $0, doneread
    syscall
    addi $a0, $a0, 141
    addi $t0, $t0, -1
    j read
doneread:

    li $t0, 141
    addi $t1, $a0, 2
    la $t2, arr
    li $t3, 'S'
findstart:
    beq $t0, $0, donefind
    sw $0, 0($t1)
    sw $0, 4($t1)
    lb $t4, 0($t2)
    beq $t4, $t3, isstart
    j cont
isstart:
    li $t4, 1
    sw $t4, 0($t1)
cont:
    addi $t1, $t1, 8
    addi $t2, $t2, 1
    addi $t0, $t0, -1
    j findstart
donefind:

    li $t3, 141 # 142-1
    move $t9, $0
loop:
    beq $t3, $0, doneloop
    li $t0, 141
    addi $t1, $t1, -1128 # -141*4*2
    move $t7, $0
    move $t8, $0
loop2:
    beq $t0, $0, doneloop2

    lw $t5, 0($t1)
    lw $t6, 4($t1)
    or $t4, $t5, $t6
    beq $t4, $0, else
    lb $t4, 0($t2)
    addi $t4, -94 # -'^'
    bne $t4, $0, else
    sw $t7, 0($t1)
    sw $t8, 4($t1)
    move $t7, $t5
    move $t8, $t6
    lw $a0, -8($t1)
    lw $a1, -4($t1)
    move $a2, $t5
    move $a3, $t6
    jal add64
    sw $v0, -8($t1)
    sw $v1, -4($t1)
    addi $t9, $t9, 1
    j endif
else:
    move $a0, $t5
    move $a1, $t6
    move $a2, $t7
    move $a3, $t8
    jal add64
    move $t5, $v0
    move $t6, $v1
    sw $t5, 0($t1)
    sw $t6, 4($t1)
    move $t7, $0
    move $t8, $0
endif:

    addi $t1, $t1, 8
    addi $t2, $t2, 1
    addi $t0, $t0, -1
    j loop2
doneloop2:
    addi $t3, $t3, -1
    j loop
doneloop:

    li $v0, 1
    move $a0, $t9
    syscall
    li $v0, 11
    li $a0, '\n'
    syscall
    li $t0, 141
    move $a0, $0
    move $a1, $0
sum:
    beq $t0, $0, donesum
    addi $t1, $t1, -8
    lw $a2, 0($t1)
    lw $a3, 4($t1)
    jal add64
    move $a0, $v0
    move $a1, $v1
    addi $t0, $t0, -1
    j sum
donesum:

    move $t5, $0
dec:
    or $t2, $a0, $a1
    beq $t2, $0, donedec
    addi $sp, $sp, -1
    addi $t5, $t5, 1
    li $t3, 10
    srl $t1, $a1, 16
    divu $t1, $t3
    mflo $t4
    mfhi $t1
    sll $t1, $t1, 16
    andi $t2, $a1, 0xFFFF
    or $t1, $t1, $t2
    divu $t1, $t3
    sll $t4, $t4, 16
    mflo $t2
    or $t4, $t4, $t2
    mfhi $t1
    sll $t1, $t1, 16
    srl $t2, $a0, 16
    or $t1, $t1, $t2
    divu $t1, $t3
    mflo $t0
    mfhi $t1
    sll $t1, $t1, 16
    andi $t2, $a0, 0xFFFF
    or $t1, $t1, $t2
    divu $t1, $t3
    sll $t0, $t0, 16
    mflo $t2
    or $t0, $t0, $t2
    mfhi $t1
    addi $t1, $t1, '0'
    sb $t1, 0($sp)
    move $a0, $t0
    move $a1, $t4
    j dec
donedec:

    li $v0, 11
ans2:
    beq $t5, $0, doneans2
    lb $a0, 0($sp)
    syscall
    addi $t5, $t5, -1
    addi $sp, $sp, 1
    j ans2
doneans2:
    
    lw $ra, 0($sp)
    addi $sp, $sp, 4
    move $v0, $0
    jr $ra