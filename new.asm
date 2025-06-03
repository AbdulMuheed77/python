 .model small
 .stack 100h
 .data 
 .code
 main proc
    mov ah,1
    int 21h
    mov bl,al          ;user sa value
  
    
    
    mov dl,0dh       ;new line
    mov ah,2
    int 21h
    mov dl,0ah
    mov ah,2
    int 21h 
     
     
     
    mov ah,1             ;dusri valu
    int 21h
    mov cl,al
   
    
    mov dl,0dh         ;new value
    mov ah,2
    int 21h
    mov dl,0ah
    mov ah,2
    int 21h 
     
    
    
    mov dl,bl         ;print value
    mov ah,2
    int 21h 
    
    mov dl,0dh         ;new value
    mov ah,2
    int 21h
    mov dl,0ah
    mov ah,2
    int 21h 
    
    mov dl,cl         ;print value
    mov ah,2
    int 21
     
    
    mov ah, 4ch
    int 21h     
  
    main endp
 end main