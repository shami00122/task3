import eel
import pandas as pd

eel.init("web")
eel.start("main.html")


@ eel.expose
def wanpi_search(word, csv_name):
    
    df = pd.read_csv(f"{csv_name}")
    source = list(df["name"])
    
    if word in source:
        print(f'『{word}』はあります')
        eel.view_log_js(f'『{word}』はあります')
        res = True
    else:
        print(f'『{word}』はありません')
        eel.view_log_js(f'『{word}』はHITしませんでした') 
        eel.view_log_js(f'『{word}』を追加します') 
        source.append(word)
        res = False    
    
    
    df = pd.DataFrame(data=source, columns=["name"]) 
    df.to_csv("source.csv", encoding="utf_8-sig")
    print(source)
    
    return res
    
    