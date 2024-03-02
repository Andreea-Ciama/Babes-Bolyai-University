bits 32                                                                                         
global start        
extern exit               
import exit msvcrt.dll    
     

;our data is declared here       
segment data use32 class=data
    a db 10
    b db 2
    c db 98
    d dw 300

;our code starts here

segment code use32 class=code
    start:
        ;    (a+b)/2 + (10-a/c)+b/4  multiplications and divisions, a,b,c as bytes, d as word
        ;
        mov AX, [a]   ;AX= a
	    add AX, [b]   ;AX= a+b
        mov BL, 2     ;BL= 2
        div BX        ;AL=(a+b)/2
        
        mov CL, AL    ;CL=(a+b)/2
        
        mov AX, [a]
        mov BL, [c]
        div BL           ; AL=a/c
        
        mov BL, 10
        sub BL,AL   ;(10-a/c)
     
        
        add CL, BL
        
        mov AX, [b]
        mov BL, 4
        div BL           ; AL=b/4
        
        add CL, BL   ;CL= (a+b)/2 + (10-a/c)+b/4
        
        
       
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program        
