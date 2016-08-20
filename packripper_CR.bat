@Echo off

:Enter-URL
		"./autocatch.py" %video_url%
		Echo .
		Echo recuperation des liens terminés
		GOTO auto
:auto
		"crunchy-xml-decoder.bat"