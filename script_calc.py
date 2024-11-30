#=============================================================================================================
# Скрипт создан и проверен в OS => Windows 10 Pro для рабочих станций(22H2)
#============================================================================================================

import os
import threading as th
import time



command = 'calc' #Команда вызова калькулятора в OS Windows

try:
    #=====================Вызов_калькулятора==================================================
    thread_start_calc = th.Thread(target=lambda: os.system(command))
    thread_start_calc.daemon = True
    thread_start_calc.start()
    time.sleep(1)
    # =====================Поиск_и_нажатие_кнопок==================================================
    import pyautogui as  pya
    
    pya.click(pya.locateOnScreen('./find_imgs/_1_.png', confidence=0.95, grayscale=True))
    time.sleep(1)
    pya.click(pya.locateOnScreen('./find_imgs/_2_.png', confidence=0.95, grayscale=True))
    time.sleep(1)
    pya.click(pya.locateOnScreen('./find_imgs/_+_.png', confidence=0.95, grayscale=True))
    time.sleep(1)
    pya.click(pya.locateOnScreen('./find_imgs/_7_.png', confidence=0.95, grayscale=True))
    time.sleep(1)
    pya.click(pya.locateOnScreen('./find_imgs/_=_.png', confidence=0.95, grayscale=True))
except Exception as ex:
    print('==========================================================================================================================================')
    print('Возможные причины неисправности:\n')
    print('Операционная система отличается от Windows 10 Pro для рабочих станций(22H2)\n')
    print('Не установленны библиотеки pyautogui, Pillow(для работы метода locateOnScreen) или OpenCV(для атрибута confidence метода locateOnScreen)\n')
    print('Калькулятор в текущей ОС отличается от калькулятора использованного при создании скрипта')
    print('Скрипт запущен не из текущей дирректории')
    print('Машаб и разметка  дисплея в ситеме отличается от 100%')
    print('==========================================================================================================================================')
    print('Лог ошибки\n')
    print(ex)
    print('==========================================================================================================================================')
    input()
