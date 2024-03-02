bits 32                                                                                         
global start        
extern exit               
import exit msvcrt.dll    
                          
segment data use32 class=data
    a db 4
    b db 4


segment code use32 class=code
    start:
        ; 4*4-excersise 16 from Simple Excersises
        mov AL, [a] ;AL=a
        mov BL, [b]  ;BL= b
        mul BL ; AX= AL* BL
        
        
        
        
        
    
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
