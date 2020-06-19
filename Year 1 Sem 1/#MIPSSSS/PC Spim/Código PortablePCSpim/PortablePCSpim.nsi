;Copyleft (C) 2006 Luis González Almenara

!define NAME "PortablePCSpim"
!define FRIENDLYNAME "Portable PCSpim"
!define APP "PCSpim"
!define VER "0.0.0.1b"
!define DEFAULTEXE "pcspim.exe"
!define DEFAULTAPPDIR "PCSpim"


Name "${NAME}"
OutFile "${NAME}.exe"
Caption "${FRIENDLYNAME} - A MIPS32 Simulator Made Portable"
VIProductVersion "${VER}"
VIAddVersionKey FileDescription "${FRIENDLYNAME}"
VIAddVersionKey LegalCopyright "GPL"
VIAddVersionKey Comments "Allows ${APP} to be run from a removable drive."
VIAddVersionKey CompanyName "by Luis González Almenara"
VIAddVersionKey OriginalFilename "${NAME}.exe"
VIAddVersionKey FileVersion "${VER}"


CRCCheck On
WindowIcon Off
SilentInstall Silent
AutoCloseWindow True



Var PathExcept
Var Reg


Function ConvertBStoDBS
 Exch $R0 ;input string
 Push $R1
 Push $R2
 StrCpy $R1 0
loop:
  IntOp $R1 $R1 - 1
  StrCpy $R2 $R0 1 $R1
  StrCmp $R2 "" done
 StrCmp $R2 "\" 0 loop
  StrCpy $R2 $R0 $R1 ;part before
   Push $R1
  IntOp $R1 $R1 + 1
  StrCpy $R1 $R0 "" $R1 ;part after
 StrCpy $R0 "$R2\\$R1"
   Pop $R1
  IntOp $R1 $R1 - 1
Goto loop
done:
   Pop $R2
   Pop $R1
   Exch $R0 ;output string
FunctionEnd





Section "Main"

GetFullPathName $PathExcept "PCSpim\exceptions.s" 
Push $PathExcept
Call ConvertBStoDBS 
Pop $R0
StrCpy $PathExcept $R0


ReadRegStr $Reg HKCU "Software\LarusStone\PCSpim\Settings" "Exception File"
IfErrors WriteReg Launch
  

WriteReg:

	WriteRegStr HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Window Font Face" "Courier"
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Window Font Height" 0x10
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Window Font Weight" 0x190
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Window Font Italic" 0x0
	WriteRegStr HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Main Window Position" "169, 61, 937, 591"
	WriteRegStr HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Console Window Position" "0, 0, 500, 326"
	WriteRegStr HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Data Segment Window Position" "0, 212, 756, 318"
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Data Segment Window State" 0x1
	WriteRegStr HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Message Window Position" "0, 318, 756, 424"
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Message Window State" 0x1
	WriteRegStr HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Register Window Position" "0, 0, 756, 106"
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Register Window State" 0x1
	WriteRegStr HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Text Segment Window Position" "0, 106, 756, 212"
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Text Segment Window State" 0x1
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Uncheck Undefined Symbols" 0x1
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Bare Machine" 0x0
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Accept Pseudo Instructions" 0x1
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Simulate Delayed Branches" 0x0
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Simulate Delayed Loads" 0x0
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Load Exception Handler" 0x1
	WriteRegStr HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Exception File" $PathExcept
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Mapped IO" 0x1
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Quiet" 0x0
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "General Regs in Hex" 0x1
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "FP Regs in Hex" 0x0
	WriteRegDWORD HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings" "Save Window Positions" 0x1
	Goto LaunchWait
LaunchWait:
	ExecWait "PCSpim\pcspim.exe"
	Call DelReg
	Goto End
Launch:
	Exec "PCSpim\pcspim.exe"
End:
SectionEnd
	Function "DelReg"
	DeleteRegKey HKEY_CURRENT_USER "Software\LarusStone\PCSpim\Settings"
	DeleteRegKey HKEY_CURRENT_USER "Software\LarusStone"
	FunctionEnd
	