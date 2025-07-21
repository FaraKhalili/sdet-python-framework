# 🧪 SDET Python Automation Framework

This is a real-world **SDET-style test automation framework** built with Python.  
It uses **Selenium WebDriver** for browser automation, **Pytest** for test execution and fixtures, and **JSON files** for data-driven testing.  
The goal is to demonstrate a modular, scalable test framework suitable for UI and API testing in professional environments.

---

## 🚀 Features

- ✅ Selenium WebDriver for browser automation
- ✅ Pytest for test discovery and execution
- ✅ Fixtures for setup and teardown (with `@pytest.fixture`)
- ✅ JSON-based data-driven testing
- ✅ Parametrized test functions
- ✅ Organized folder structure for scalability
- ✅ Easy integration with HTML reports and CI pipelines

---

## 📂 Project Structure

```
sdet-python-framework/
├── tests/                # UI and API test cases
│   ├── test_ui_google.py
│   └── test_api_addition.py
├── fixtures/             # Reusable test fixtures
│   └── browser_fixture.py
├── data/                 # JSON test data
│   └── test_data.json
├── src/                  # (Optional) business logic or page objects
├── conftest.py           # Global fixtures (if used)
├── requirements.txt      # Project dependencies
├── pytest.ini            # Pytest configuration
└── README.md             # Project overview and instructions
```

---

## 🛠️ Installation

Make sure you have **Python 3.8+** installed, then:

```bash
git clone https://github.com/FaraKhalili/sdet-python-framework.git
cd sdet-python-framework
pip install -r requirements.txt
```

---

## ✅ Running Tests

```bash
pytest
```

To generate an HTML report:
```bash
pytest --html=report.html
```

---

## 🧪 Example Test: `test_api_addition.py`

Reads data from `test_data.json` and validates addition function:

```python
import json

def add(a, b):
    return a + b

with open("data/test_data.json", "r") as f:
    data = json.load(f)

for case in data["test_cases"]:
    a, b = case["input"]
    expected = case["expected"]
    result = add(a, b)
    assert result == expected
```

---

## 👩‍💻 Author

**Fara Khalili**  
📍 Vancouver, BC  
🔗 [LinkedIn](https://www.linkedin.com/in/farakhalili/)  
🔗 [GitHub](https://github.com/FaraKhalili)

---

## 📌 License

This project is for educational and professional portfolio use.
