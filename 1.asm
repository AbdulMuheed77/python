.model small
.stack 100h
.data 
var db 'a'
.code
main proc
    mov ax,@data
    mov ds,ax
    mov var ,'a'
    mov ah,4ch ;
    int 21h;
    main endp
    end main
    