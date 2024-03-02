bits 32                                                                                         
global start        
extern exit               
import exit msvcrt.dll    
                          
segment data use32 class=data
    a dw 128
    b dw 128
    c dw 240
    d dw 15


segment code use32 class=code
    start:
        ; (a+b+b)+(c-d) from additions, substractions, all variables as words
        
        mov AX, [a]   ; AX= a
        add AX, [b]   ; AX= a+b
        add AX, [b]   ; AX= a+b+b
        
        mov BX, [c]   ;BX= c
	    sub BX,[d]    ;BX= c-d
        
        add AX, BX   ;AX= (a+b+b)+(c-d)
     
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
