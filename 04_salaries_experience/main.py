import matplotlib.pyplot as plt
from collections import defaultdict

salaries_and_tenures = [
    (83000, 8.7),
    (88000, 8.1),
    (48000, 0.7),
    (76000, 6),
    (69000, 6.5),             #годовая зарплата и стаж
    (76000, 7.5),
    (60000, 2.5),
    (83000, 10),
    (48000, 1.9),
    (63000, 4.2)
]

salaries = [
    salary
    for salary, tenure in salaries_and_tenures
]

tenures = [
    tenure
    for salary, tenure in salaries_and_tenures
]

plt.scatter(tenures, salaries)

plt.xlabel("Experience (years)")
plt.ylabel("Annual salary ($)")
plt.title("Salary vs Experience")

plt.grid(True)
plt.show()

#группировка зарплаты по стажу
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

print("Зарплаты по стажу:")
print(dict(salary_by_tenure))

#Средняя зарплата для каждого значения стажа
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
print("Средняя зарплата по стажу:")

for tenure, average in average_salary_by_tenure.items():
    print(f"Стаж: {tenure} лет - Средняя зарплата: ${average:.2f}")
    
#Определяем категориюсотрудника по стажу
def tenure_bucket(tenure):
    if tenure < 2:
        return "Less than 2 years"
    elif tenure < 5:
        return "Between 2 and 5 years"
    else:
        return "More than 5 years"
    
#Создаем словарь для категорий 
salary_by_tenure_bucket = defaultdict(list)

#Распределяем зарплаты по категориям 
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
#Средняя зарплата по категориям
average_salary_by_bucket = {
    bucket: sum(salaries) / len(salaries)
    for bucket, salaries in salary_by_tenure_bucket.items()
}

print("\nAverage salary by experience group:")

for bucket, average in average_salary_by_bucket.items():
    print(f"{bucket}: ${average:.2f}")
    
    
#ДИАГРАММА
#располагаем категории по возрастанию стажа
categories = [
    "Less than 2 years",
    "Between 2 and 5 years",
    "More than 5 years"
]

#Получаем среднюю зп из словаря
average_salaries = [
    average_salary_by_bucket[category]
    for category in categories
]

plt.figure(figsize=(10, 6))

bars = plt.bar(
    categories,
    average_salaries,
    color=["skyblue", "cornflowerblue", "royalblue"]
)

#Подписываем значения над столбцами 
for bar in bars:
    height = bar.get_height()
    
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1000,
        f"${height:,.0f}",
        ha="center"
    )
    
#Настраиваем график
plt.title("Average salary by experience")
plt.xlabel("Years of experience")
plt.ylabel("Average annualsalary ($)")

plt.ylim(0, max(average_salaries) * 1.2)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()