;--------------------------------------------------------
; External References for shared variables
;--------------------------------------------------------
        EXTERN  BusAddress          ; External reference for the bus address variable
        EXTERN  BusData             ; External reference for the bus data variable

;--------------------------------------------------------
; Lookup table for 7-segment SSGs 0-F
;--------------------------------------------------------
        RSEG CODE                   ; Place the table in the CODE segment (read-only memory)
        PUBLIC SSG0              ; Make the start address of the table ('SSG0') externally visible

SSG0:     DW 0x0040               ; 7-segment pattern for the SSG "0"
SSG1:     DW 0x0079               ; 7-segment pattern for the SSG "1"
SSG2:     DW 0x0024               ; 7-segment pattern for the SSG "2"
SSG3:     DW 0x0030               ; 7-segment pattern for the SSG "3"
SSG4:     DW 0x0019               ; 7-segment pattern for the SSG "4"
SSG5:     DW 0x0012               ; 7-segment pattern for the SSG "5"
SSG6:     DW 0x0002               ; 7-segment pattern for the SSG "6"
SSG7:     DW 0x0078               ; 7-segment pattern for the SSG "7"
SSG8:     DW 0x0000               ; 7-segment pattern for the SSG "8"
SSG9:     DW 0x0018               ; 7-segment pattern for the SSG "9"
SSGA:     DW 0x0008               ; 7-segment pattern for the SSG "A"
SSGB:     DW 0x0003               ; 7-segment pattern for the SSG "b" (lowercase)
SSGC:     DW 0x0046               ; 7-segment pattern for the SSG "C" (uppercase C)
SSGD:     DW 0x0021               ; 7-segment pattern for the SSG "d" (lowercase d)
SSGE:     DW 0x0006               ; 7-segment pattern for the SSG "E"
SSGF:     DW 0x000E               ; 7-segment pattern for the SSG "F"

END
