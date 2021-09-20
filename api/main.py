#falcon
import falcon
import falcon.asgi

#classes for this app
from getmax import GetMax
from home import index
from populate import DbLoader

app = application = falcon.App()
maxValue= GetMax()
startPage= index()
#db_load_page= DbLoader()
app.add_route('/', startPage)
app.add_route('/max', maxValue)
#app.add_route('/populate', db_load_page)

