import pandas as pd
import matplotlib.pyplot as plt
import json

# Этап 1: Загрузка данных из JSON
print("1. Загружаем данные из events.json...")
with open('events.json', 'r') as f:
    data = json.load(f)

# Этап 2: Анализ данных с помощью Pandas
print("2. Создаем DataFrame и анализируем...")
df = pd.DataFrame(data['events'])

# Извлекаем тип события (первое слово)
df['event_type'] = df['signature'].str.split().str[0]

# Считаем распределение
event_counts = df['event_type'].value_counts()

print("\nРаспределение событий по типам:")
print("-" * 40)
for event_type, count in event_counts.items():
    print(f"{event_type}: {count} событий")

# Этап 3: Визуализация с помощью Matplotlib
print("\n3. Строим график...")
plt.figure(figsize=(10, 6))

# Простой столбчатый график
bars = plt.bar(event_counts.index, event_counts.values, color='skyblue')

# Настройки
plt.title('Распределение событий информационной безопасности по типам')
plt.xlabel('Тип события')
plt.ylabel('Количество событий')
plt.xticks(rotation=45)

# Добавляем числа на столбцы
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom')

plt.tight_layout()

# Сохраняем график
plt.savefig('security_events_distribution.png', dpi=100)
print("\n✓ График сохранен как 'security_events_distribution.png'")

# Показываем график
plt.show()

print("\n✓ Задание выполнено!")
