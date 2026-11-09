import networkx as nx
import matplotlib.pyplot as plt

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3),
    (2, 3), (3, 4), (4, 5), (5, 6),
    (5, 7), (6, 8), (7, 8), (8, 9)
]

# Создаём списки друзей
for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

# Количество друзей каждого пользователя
for user in users:
    print(user["name"], len(user["friends"]))

# Среднее количество друзей
num_friends = [
    len(user["friends"])
    for user in users
]

total_connections = sum(num_friends)
avg_connections = total_connections / len(users)

print("Total connections:", total_connections)
print("Average connections:", avg_connections)

# Визуализация
G = nx.Graph()

for user in users:
    G.add_node(user["name"])

for i, j in friendships:
    G.add_edge(users[i]["name"], users[j]["name"])

nx.draw(
    G,
    with_labels=True,
    node_color="skyblue",
    node_size=1500,
    font_size=10
)

plt.show()
