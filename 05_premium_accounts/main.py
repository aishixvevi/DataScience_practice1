#Прогноз оплаты премиум-аккаунта по стажу
import matplotlib.pyplot as plt

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
    
#Стаж пользователей
experience = [0.7, 1.9, 2.5, 4.2, 6, 6.5, 7.5, 8.1, 8.7, 10]

# 1 = оплачено, 0 = неоплачено
paid = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1]

plt.figure(figsize=(10, 5))

plt.scatter(experience, paid, color="royalblue", s=100)

#Границы модели
plt.axvline(x=3.0, color="red", linestyle="--")
plt.axvline(x=8.5, color="red", linestyle="--")

plt.yticks([0, 1], ["Not paid", "Paid"])
plt.xlabel("Years of Experience")
plt.ylabel("Premium Account")
plt.title("Premium Account Payment vs Experience")

plt.grid(alpha=0.3)
plt.show()