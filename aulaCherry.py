import cherrypy
from datetime import datetime

class Root(object):
    
    @cherrypy.expose
    def index(self):
        return """<html>
        <head></head>
        <body> 
          <form method="get" action=" resultado">
            <input type="text" name ="numero" />
            <button type="submit">Enviar</button>
          </form>
        </body>
        </html>"""

    @cherrypy.expose
    def hora(self):
        return str(datetime.now())

    @cherrypy.expose
    def resultado(self, numero):
        return """Você digitou {}""".format(numero)



cherrypy.quickstart(Root())