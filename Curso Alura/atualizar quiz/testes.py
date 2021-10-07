import pyautogui
pyautogui.PAUSE = 1 #tempo de pausa entre uma execucao e outra
print(pyautogui.position())#mostra posicao atual do mouse
print(pyautogui.size())#tmanho da tela
print(pyautogui.onScreen(1365,768))#diz se esta posicao esta localizada na tela
print('Oh')
#pyautogui.moveTo(x, y, duration=num_seconds)
pyautogui.moveTo(500,500)
print('Coou')
#pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
pyautogui.moveRel(20,50,duration=2)
#pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
pyautogui.dragTo(20,0)
#pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
#O buttonargumento de palavra-chave pode ser 'left', 'middle'ou 'right'.
pyautogui.click(x=5,y=10,clicks=3,interval=1,button='left')
# >>> pyautogui.rightClick(x=moveToX, y=moveToY)
# >>> pyautogui.middleClick(x=moveToX, y=moveToY)
# >>> pyautogui.doubleClick(x=moveToX, y=moveToY)
# >>> pyautogui.tripleClick(x=moveToX, y=moveToY)

print(pyautogui.confirm('Apertai rapa'))

