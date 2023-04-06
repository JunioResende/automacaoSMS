import pyautogui
from time import sleep

# Coordenadas
coordinate_select_atribute_X = 1239
coordinate_select_atribute_Y = 225
coordinate_click_right_button_X = 805
coordinate_click_right_button_Y = 330
coordinate_export_button_X = 870
coordinate_export_button_Y = 411
coordinate_init_export_X = 613
coordinate_init_export_Y = 601
coordinate_format_export_X = 517
coordinate_format_export_Y = 603


# Tempo de execuçao do atributo
execution_time_atribute = 60

# Aluminio
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(execution_time_atribute)
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
pyautogui.write('14_Aluminio')
pyautogui.press('enter')
