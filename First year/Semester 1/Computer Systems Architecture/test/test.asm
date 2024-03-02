bits 32

global start

extern exit, fopen, fread, fclose, fprintf
import exit msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll

segment data use32 class=data
    file_name db 'words.txt', 0
    access_mode db 'r', 0
    file_descriptor dd -1
    file_name2 db 'wordscount.txt', 0
    access_mode2 db 'w', 0
    file_descriptor2 dd -1
    buffer_size equ 100
    word_flag db 1
    space equ ' '
    point equ '.'
    buffer resb buffer_size
    counter dd 0
    format db '%d', 0
    
   
    
segment code use32 class=code
    start:
    
        ;printf(print_format)
        ;push dword print_format
        ;call [printf]
        ;add ESP, 4*1
        
        ;gets(file_name)
        ;push dword file_name
        ;call [gets]
        ;add ESP, 4*1
        
        
        PUSH dword access_mode
        PUSH dword file_name
        CALL [fopen]
        ADD ESP, 4*2
        CMP EAX, 0
        JE finish
        MOV [file_descriptor], EAX
        
        PUSH dword access_mode2
        PUSH dword file_name2
        CALL [fopen]
        ADD ESP, 4*2
        CMP EAX, 0
        JE finish
        MOV [file_descriptor2], EAX
        
        file_loop:
            PUSH dword [file_descriptor]
            PUSH dword buffer_size
            PUSH dword 1
            PUSH dword buffer
            CALL [fread]
            ADD ESP, 4*4
            CMP EAX, 0
            JE after
            
            MOV ECX, EAX
            CLD
            MOV ESI, buffer
            
            ;push dword buffer
            ;push dword [file_descriptor2]
            ;call [fprintf]
            ;add ESP, 4*2
            
            buffer_loop:
                LODSB
                CMP AL, space
                JE punctuation
                CMP AL, point
                JE punctuation
                
                CMP byte [word_flag], 1
                JNE skip
                INC dword [counter]
                MOV byte [word_flag], 0
                JMP skip
                
                punctuation:
                MOV byte [word_flag], 1
                
                skip:
            LOOP buffer_loop
        JMP file_loop
        after:
        
        PUSH dword [counter]
        push dword format
        push dword [file_descriptor2]
        call [fprintf] 
        add esp, 4*3
        
        PUSH dword [file_descriptor]
        CALL [fclose]
        ADD ESP, 4
        
        
        PUSH dword [file_descriptor2]
        CALL [fclose]
        ADD ESP, 4
        
        finish:
        PUSH dword 0
        CALL [exit]