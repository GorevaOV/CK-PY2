list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
m_ind = 0 # индекс макс. значения
m_val = list_numbers[m_ind] # само макс. значение
l_val = list_numbers[-1] # последнее значение в списке

for i, c_val in enumerate(list_numbers): # для i-го индекса и соответствующего ему значение запускаем цикл
    if c_val >= m_val: # условие перебора
        m_val = c_val # приравнивание текущего значения максимальному
        m_ind = i # приравнивание текущего индекса

list_numbers[m_ind], list_numbers[i] = list_numbers[i], list_numbers[m_ind] # меняем нужное местами
print(list_numbers) # финал
