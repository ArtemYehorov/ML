import pandas as pd
import numpy as np
#1
arr = np.random.randint(1, 101, size = 10)

mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)

print("Масив:", arr)
print("Середнє:", mean)
print("Медіана:", median)
print("Стандартне відхилення:", std_dev)

arr[arr % 2 == 0] = 0
print("Масив після заміни парних чисел на 0:", arr)

print('-' * 100)
#2
matrix = np.random.randint(1, 101, size = (3,3))

print("Матриця:\n", matrix)
print("Перший рядок:", matrix[0])
print("Останній стовпець:", matrix[:, -1])
print("Діагональні елементи:", np.diagonal(matrix))


print('-' * 100)
#3
matrix_2d = np.random.randint(1, 101, size =(3, 3))
array_1d = np.random.randint(1,11, size=3)

result = matrix_2d + array_1d

print("2D Масив:\n", matrix_2d)
print("1D Масив:", array_1d)
print("Результат broadcasting:\n", result)


print('-' * 100)
#4
matrix_5x5 = np.random.randint(1,101, size=(5,5))
unique_elements = np.unique(matrix_5x5)

threshold = 200
threshold_rows = matrix_5x5[np.sum(matrix_5x5, axis=1) > threshold]

print("Матриця 5x5:\n", matrix_5x5)
print("Унікальні елементи:", unique_elements)
print(f"Рядки із сумою більше {threshold}:\n", threshold_rows)

print('-' * 100)
#5
arr_1d = np.arange(1,21)
arr_2d = arr_1d.reshape(4,5)

print("1D Масив:", arr_1d)
print("2D Масив:\n", arr_2d)

print('-' * 100)
print('-' * 100)
print('-' * 100)

#1
data = {
    'Ім\'я': ['Аня', 'Петро', 'Оля', 'Іван', 'Микола'],
    'Вік': [23, 34, 28, 45, 50],
    'Місто': ['Київ', 'Львів', 'Одеса', 'Харків', 'Запоріжжя']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

#2
df['Зарплата'] = [1500, 2000, 1800, 2200, 2500]
print("\nDataFrame з новим стовпцем:\n", df)
#3
filtered_df = df[df['Зарплата'] > 2000]
print("\nВідфільтрований DataFrame (Зарплата > 2000):\n", filtered_df)
#4
df_wine = pd.read_csv('wine.csv')
print("Перші 5 рядків набору даних:\n", df_wine.head().to_string(header = False))
#5
numeric_stats = df_wine.describe()
print("\nЗагальна статистика для числових стовпців:\n", numeric_stats.to_string(header = False))
#6
unique_classes = df_wine['1'].unique()
print("\nУнікальні значення у стовпці '1':\n", unique_classes)