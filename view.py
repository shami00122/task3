import eel
import desktop
import search

app_name="html"
end_point="main.html"
size=(700,600)

@ eel.expose
def wanpi_search(word, csv_name):
    search.wanpi_search(word, csv_name)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)