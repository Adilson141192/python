import pyautogui
import time

pyautogui.PAUSE = 1.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=540, y=565)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=580, y=391)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, categoria]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, preco-unitario]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, custo]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")  
    pyautogui.scroll(2000)