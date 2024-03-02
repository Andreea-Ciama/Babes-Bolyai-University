bits 32                                                                                         
global start        
extern exit               
import exit msvcrt.dll  
                           

;our data is declared here                           
segment data use32 class=data
    a db 3
    e dw 2
    f dw 3

    ;our code starts here
segment code use32 class=code
    start:
        
        ;a*a-(e+f) a,b,c,d-byte, e,f,g,h-word

        mov AL, [a]
        mov BL, [a]
        mul BL          ; AX= a*a
        
        
        mov BX, [e]
        add BX, [f]     ;BL= a+d
        
        sub AX, BX  ;AL= a*a-(e+f)
        
        
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

