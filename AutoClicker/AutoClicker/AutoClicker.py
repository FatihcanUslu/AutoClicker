import keyboard, time , pyautogui

print("f5 tuşu çalıştırmak f6 tuşu durdurmak ve f7 tuşu programı sonlandırmak için kullanılır")
while True :
    if keyboard.is_pressed('f5'):
        while True :           
            pyautogui.leftClick()            
            if keyboard.is_pressed('f6'):
                break            
    if keyboard.is_pressed('f7'):
        break
            

    time.sleep(0.1)