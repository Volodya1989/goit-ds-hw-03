# GOIT DS HW 3 — MongoDB + Web Scraping Project

## 📘 Description

This project demonstrates:

- Working with MongoDB and PyMongo (CRUD operations)
- Web scraping using `requests` and `BeautifulSoup`
- Data export to `authors.json` and `quotes.json`
- Importing scraped data to MongoDB Atlas

---

## 📂 Project Structure

```
goit-ds-hw-03/
│
├── main.py            # Script for MongoDB CRUD operations
├── scraper.py         # Web scraping script for quotes.toscrape.com
├── authors.json       # Exported author data
├── quotes.json        # Exported quotes data
├── .env               # Environment variables (e.g., MongoDB URI)
├── pyproject.toml     # Poetry project file
├── poetry.lock        # Locked dependencies
└── README.md          # This file
```

---

## ⚙️ Technologies Used

- Python 3.10+
- MongoDB Atlas
- PyMongo
- Requests
- BeautifulSoup (bs4)
- Poetry (for dependency management)
- dotenv (.env config)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Volodya1989/goit-ds-hw-03.git
cd goit-ds-hw-03
```

### 2. Set up a Virtual Environment (with Poetry)

```bash
poetry install
```

### 3. Create a `.env` File

Create a `.env` file in the root directory with the following content:

```env
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>?retryWrites=true&w=majority
```

Replace the placeholder with your actual MongoDB Atlas URI.

---

## 🧐 Functionality Overview

### ✔️ MongoDB CRUD Operations

Located in `main.py`:

- `create_cat` — Add a new cat document
- `get_all_cats` — List all cats
- `get_cat_by_name` — Get cat by name
- `update_cat_age` — Change age by name
- `add_feature_to_cat` — Add a new feature
- `delete_cat_by_name` — Delete a specific cat
- `delete_all_cats` — Delete all cats

### ✔️ Web Scraping: Quotes and Authors

Located in `scraper.py`:

- Scrapes all quotes from all pages of [quotes.toscrape.com](http://quotes.toscrape.com)
- Extracts:

  - Quote text
  - Author name
  - Author biography (born date, location, and description)
  - Tags

- Saves data to:

  - `quotes.json`
  - `authors.json`

---

## 📄 Import Data to MongoDB Atlas

After generating the JSON files:

1. Use MongoDB Compass or `mongoimport` to import `quotes.json` and `authors.json` into your `quotes` and `authors` collections respectively.

---

## 📌 Usage Examples

```bash
poetry run python main.py    # Perform CRUD actions with MongoDB
poetry run python scraper.py # Run the scraper and generate JSON data
```

---

## 🧑‍💻 Author

**Volodymyr Petrytsya**
🔗 [GitHub Profile](https://github.com/Volodya1989)

---

## 📝 License

This project is submitted as part of the GoIT Data Science course.
