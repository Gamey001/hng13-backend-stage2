# 🌍 Country Currency & Exchange API

A RESTful FastAPI service that fetches country and currency data from external APIs, computes estimated GDP, caches results in a PostgreSQL database, and exposes CRUD and analytical endpoints.

---

## 🚀 Features

- Fetch all countries and their currencies from **REST Countries API**
- Fetch real-time exchange rates from **Open Exchange API**
- Compute and cache `estimated_gdp` using:
  ```
  estimated_gdp = population × random(1000–2000) ÷ exchange_rate
  ```
- Filter and sort countries by region, currency, and GDP
- View total stats and auto-refresh timestamp
- Generate and serve summary image (`cache/summary.png`)
- Full CRUD operations with validation and error handling

---

## 🧠 Tech Stack

| Component        | Technology            |
| ---------------- | --------------------- |
| Language         | Python 3.11+          |
| Framework        | FastAPI               |
| Database         | PostgreSQL            |
| ORM              | SQLAlchemy            |
| HTTP Client      | httpx                 |
| Image Generation | Pillow                |
| Deployment       | Railway (recommended) |

---

## 📦 Folder Structure

```
hng13-backend-stage2/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── utils.py
│
├── tests/
│   └── test_endpoints.py
│
├── cache/
│   └── summary.png  # auto-generated
│
├── .env
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/hng13-backend-stage2.git
cd hng13-backend-stage2
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate     # (Windows)
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should include:

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
httpx
python-dotenv
pillow
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file in the project root with:

```
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/countrydb
PORT=8000
```

> 🧩 Tip: For Railway, replace with the PostgreSQL URL from your Railway dashboard after deployment.

---

### 5️⃣ Initialize Database

Ensure PostgreSQL is running and create your DB:

```bash
psql -U postgres
CREATE DATABASE countrydb;
\q
```

Then run the app once to auto-create tables:

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Testing Endpoints

After running the app, test endpoints using **curl** or **Postman**.

| Method   | Endpoint             | Description                                |
| -------- | -------------------- | ------------------------------------------ |
| `POST`   | `/countries/refresh` | Fetch & cache data                         |
| `GET`    | `/countries`         | List all countries (filter/sort supported) |
| `GET`    | `/countries/{name}`  | Fetch one country                          |
| `DELETE` | `/countries/{name}`  | Delete country                             |
| `GET`    | `/status`            | Get system stats                           |
| `GET`    | `/countries/image`   | View summary image                         |

**Example:**

```bash
curl -X POST http://127.0.0.1:8000/countries/refresh
```

---

## 🧾 Example Response

```json
{
  "id": 1,
  "name": "Nigeria",
  "capital": "Abuja",
  "region": "Africa",
  "population": 206139589,
  "currency_code": "NGN",
  "exchange_rate": 1600.23,
  "estimated_gdp": 25767448125.2,
  "flag_url": "https://flagcdn.com/ng.svg",
  "last_refreshed_at": "2025-10-25T18:00:00Z"
}
```

---

## 🧰 Running Tests

You can run tests (if provided) using pytest:

```bash
pytest
```

---

## 🖼️ Summary Image

After running `/countries/refresh`, a summary image will be generated at:

```
cache/summary.png
```

You can view it via:

```
GET /countries/image
```

---

## ☁️ Deployment

### Railway (Recommended)

1. Push your code to GitHub.
2. Create a new **Railway Project**.
3. Connect your GitHub repo.
4. Add PostgreSQL plugin.
5. Set `DATABASE_URL` environment variable.
6. Deploy.

Your app will be live at:

```
https://yourapp.up.railway.app
```

---

## 🧩 Submission Guide

To submit for HNG Stage 2:

1. Verify your app works from multiple networks.
2. Go to **#stage-2-backend** on Slack.
3. Run the command:
   ```
   /stage-two-backend
   ```
4. Submit:
   - API Base URL (e.g., `https://yourapp.up.railway.app`)
   - GitHub Repo URL
   - Full Name
   - Email
   - Stack (`Python / FastAPI / PostgreSQL`)

---

## 🛠️ Error Handling

| Code | Response Example                                |
| ---- | ----------------------------------------------- |
| 400  | `{"error": "Validation failed"}`                |
| 404  | `{"error": "Country not found"}`                |
| 500  | `{"error": "Internal server error"}`            |
| 503  | `{"error": "External data source unavailable"}` |

---

## 👨🏽‍💻 Author

**Gamaliel Dashua**  
Backend Developer | HNG 13 Cohort  
📧 your-email@example.com  
🔗 [LinkedIn / GitHub / Portfolio]

---

## 🏁 License

This project is licensed under the MIT License.

---

✅ _Built with FastAPI for HNGx Stage 2 Backend Challenge._
