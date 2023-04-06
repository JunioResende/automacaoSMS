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
execution_time_atribute = 30

# Aluminio
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('14_Aluminio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Areia
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('4_Areia', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Argila
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('3_Argila', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Boro
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('21_Boro', interval=0.2)
pyautogui.press('enter')
sleep(5)

# CaCTC
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('22_Calcio_CTC', interval=0.2)
pyautogui.press('enter')
sleep(5)

# CaK
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('27_Relacao_Calcio_Potassio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# CaMg
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('26_Relacao_Calcio_Magnesio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Ca+Mg
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('13_Calcio_Mais_Magnesio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Calcio
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('11_Calcio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Carbono Organico
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('7_Carbono_Organico', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Cobre
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('29_Cobre', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(20)

# CTC Total
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('8_CTC_Total', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Enxofre
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('20_Enxofre', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Ferro
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('30_Ferro', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Fosforo Mehlich
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('18_Fosforo_Mehlich', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Hidrogenio + Alumino
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('15_Hidrogenio_Mais_Aluminio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Hidrogenio + Alumino CTC
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('25_Hidrogenio_Mais_Aluminio_CTC', interval=0.2)
pyautogui.press('enter')
sleep(20)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(20)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(20)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(20)

# Potassio CTC
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('24_Potassio_CTC', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Magnesio
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('12_Magnesio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Manganes
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('31_Manganes', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Materia Organica
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('6_Materia_Organica', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Magnesio CTC
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('23_Magnesio_CTC', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Magnesio Potassio
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('28_Relacao_Magnesio_Potassio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(5)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(5)

# pHCaCl
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('9_pH_Cloreto_de_Calcio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(5)

# Potassio
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('19_Potassio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Potassio ppm
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('17_Potassio_ppm', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(5)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(5)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(5)

# Saturação de Bases
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('10_Saturacao_de_Bases', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Saturação por Aluminio
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('10_Saturacao_de_Bases', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Silte
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('5_Silte', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Sodio
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('33_Sodio', interval=0.2)
pyautogui.press('enter')
sleep(5)

# Pular atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
sleep(5)

# Zinco
# Selecionar atributo
pyautogui.click(coordinate_select_atribute_X,
                coordinate_select_atribute_Y, duration=2)
pyautogui.press('down')
# Tempo para a execução do atributo
sleep(execution_time_atribute)
# Clique no botão direito do mouse para iniciar o processo de exportação
pyautogui.click(button='right', x=coordinate_click_right_button_X,
                y=coordinate_click_right_button_Y, duration=2)
# Clique em exportar
pyautogui.click(coordinate_export_button_X,
                coordinate_export_button_Y, duration=2)
# Clique no botão Iniciar Processo de exportação de Aquivo Genérico
pyautogui.click(coordinate_init_export_X, coordinate_init_export_Y, duration=2)
# Clique em Exportar para o formato de arquivo selecionado
pyautogui.click(coordinate_format_export_X,
                coordinate_format_export_Y, duration=2)
sleep(2)
pyautogui.write('32_Zinco', interval=0.2)
pyautogui.press('enter')
sleep(5)
