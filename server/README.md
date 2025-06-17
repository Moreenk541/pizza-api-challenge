
#  Pizza API Challenge

A RESTful API for managing restaurants, pizzas, and their associations.

---

##  Setup Instructions

1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd pizza-api-challenge
```

2. **Set up a virtual environment**

```bash
pipenv install
pipenv shell
```

3. **Set environment variables (optional)**

```bash
export FLASK_APP=server.app
export FLASK_ENV=development
```

4. **Run the application**

```bash
flask run --port=5003
```

---

##  DB Migration & Seeding

1. **Initialize the DB (only once)**

```bash
flask db init
```

2. **Generate migration files**

```bash
flask db migrate -m "Initial migration"
```

3. **Apply migrations**

```bash
flask db upgrade
```

4. **Seed the database**

```bash
python -m server.seed
```

---

##  Route Summary

| Method | Endpoint                       | Description                                 |
|--------|--------------------------------|---------------------------------------------|
| GET    | /restaurants                   | Get all restaurants                         |
| GET    | /restaurants/<id>              | Get a restaurant and its pizzas             |
| DELETE | /restaurants/<id>              | Delete a restaurant                         |
| GET    | /pizzas                        | Get all pizzas                              |
| POST   | /restaurant_pizzas             | Create a restaurant-pizza association       |

---

## 🔁 Example Requests & Responses

### GET /restaurants

**Response:**

```json
[
  {
    "id": 1,
    "name": "Dominos",
    "address": "123 Street"
  }
]
```

### GET /restaurants/1

```json
{
  "id": 1,
  "name": "Dominos",
  "address": "123 Street",
  "pizzas": [
    {
      "id": 1,
      "name": "Pepperoni",
      "ingredients": "Cheese, Tomato, Pepperoni"
    }
  ]
}
```

### DELETE /restaurants/1

- **Success:** Status Code `204 No Content`
- **If Not Found:**

```json
{ "error": "Restaurant not found" }
```

### GET /pizzas

```json
[
  {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Cheese, Tomato, Pepperoni"
  }
]
```

### POST /restaurant_pizzas

**Request:**

```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

**Success Response:**

```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Emma",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "address3"
  }
}
```

**Error Response (Invalid Price):**

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---

## Validation Rules

- `price` in `/restaurant_pizzas` must be between **1 and 30**
- `pizza_id` and `restaurant_id` must be valid and exist in the database

---

## 📬 Postman Usage

1. Open Postman.
2. Click **"Import"** → **Upload Files**.
3. Upload `challenge-1-pizzas.postman_collection.json`.
4. Test all routes directly from the collection.

---
