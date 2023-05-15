; Nombre y versión del instalador
OutFile "AppleGameSetup.exe"
VIProductVersion "1.2.4"

; Página de configuración
Page Directory
Page InstFiles

; Archivos a instalar
Section
  SetOutPath "$INSTDIR"
  File "AppleGame.exe"
SectionEnd
