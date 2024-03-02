bits 32                                                                                         
global start        
extern exit               
import exit msvcrt.dll    
                          
segment data use32 class=data
    a resw 1

segment code use32 class=code
    start:
    
    
       mov ax, -1
       mov bh, 1
       div bh
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program