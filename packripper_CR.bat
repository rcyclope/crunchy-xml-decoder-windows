@Echo off

:Enter-URL
		"./autocatch.py" %video_url%
		Echo .
		Echo recuperation des liens termin�s
		GOTO auto
:auto
		"crunchy-xml-decoder.bat"