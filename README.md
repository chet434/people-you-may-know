# 👥 People You May Know - Friend Recommendation System

This is a Python project that simulates the "People You May Know" feature seen on social media platforms like Facebook and LinkedIn. It uses mutual friend logic to suggest new connections for a user based on a given social network dataset.

---

## 📌 Features

- Suggests potential friends based on mutual connections.
- Works on structured JSON data representing users and their friendships.
- Ranks recommendations by number of shared mutual friends.
- Easy to extend with features like name-based display, friend-of-friend chains, or visualization.

---

## 🗂️ Project Structure

people-you-may-know/
├── people_you_may_know.py         # Main Python script
├── large_social_network.json      # Sample dataset
└── README.md                      # Project documentation

---

## 🧠 How It Works

1. Loads data from a JSON file containing users and their friends.
2. For a given user ID:
   - Finds their direct friends.
   - Finds friends of friends (mutuals).
   - Filters out direct friends and self.
   - Counts how many times each mutual appears (mutual friend count).
   - Sorts suggestions based on highest mutual friends first.
3. Returns a list of suggested user IDs.

---

## 📄 Sample JSON Structure

```json
{
  "users": [
    {
      "id": 1,
      "name": "Amit",
      "friends": [2, 3],
      "liked_pages": [101]
    },
    ...
  ],
  "pages": [
    {
      "id": 101,
      "name": "Python Developers"
    },
    ...
  ]
}
```

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.x

### ▶️ Run the Script

```
python people_you_may_know.py

It will print suggestions like:

People You May Know for User 1: [32, 6, 8, 15, 5, 10, 13, ...]
```

---

## 📈 Sample Output Explained

If user 1 is directly friends with users 2 and 3, and:
- User 2 is friends with [4, 5]
- User 3 is friends with [5, 6]

Then 5 appears twice → gets a higher rank in recommendations than 4 or 6.

---

## 🔧 Customization Ideas
- Return names instead of just user IDs.
- Visualize the network using `networkx` and `matplotlib`.
- Combine with other data like shared interests or liked pages.
- Add a CLI or web interface (Flask or FastAPI).

---

## 📂 Data

A sample dataset is included as large_social_network.json. You can expand it or generate your own.

---

## 📜 License

This project is open-source and free to use for learning or extension.

---

## 🙋‍♂️ Author

Created by Chetan Prasad Sahoo — a passionate developer learning data science, AI, and social graph algorithms.

Feel free to connect or contribute!
