# 🧪 Behave BDD + Selenium + Allure Reporting for YouTube Test Automation

This project demonstrates end-to-end UI test automation using **Python**, **Behave BDD**, **Selenium**, and **Allure** to test YouTube functionality (search and play a video).

---

## ✅ Prerequisites

Make sure you have the following installed on your system:

| Tool         | Required |
|--------------|----------|
| Python 3.8+  | ✅       |
| pip          | ✅       |
| Google Chrome| ✅       |
| ChromeDriver | ✅       |
| Git          | ✅       |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/rahmadanityas/bdd_automation.git
cd bdd_automation.git
```

### 2. Create virtual environment
```
python -m venv .venv
```

# Activate it
# On Windows:
```
.venv\Scripts\activate
```

# On macOS/Linux:
```
source .venv/bin/activate
```

### 3. Install Python Dependencies
```
pip install -r requirements.txt
```

# If requirements.txt is missing, create one with:
```
behave
selenium
allure-behave
pyautogui
```

# Then run:
```
pip install behave selenium allure-behave pyautogui
```

## 🚀 Running the Test with Allure Report
### 1. Run Tests and Generate Raw Report Data
This command runs the test and stores Allure JSON results in the reports/ folder.
```
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
```

### 2. Install Allure CLI (One-Time Setup)
# Windows (via Scoop)
```
scoop install allure
```

# Windows (via Chocolatey)
```
choco install allure
```

# macOS (via Homebrew)
```
brew install allure
```

# Or Download Manually and Add to PATH

### 3. Generate the HTML Report
```
allure generate reports/ -o allure-report --clean
```

### 4. Open the Allure Report in Your Browser
This will start a local web server and launch your browser to view the report.
```
allure open allure-report
```

📁 Project Structure
your-repo-name/
│
├── features/
│   ├── example.feature          # Gherkin scenarios
│   └── steps/
│       └── steps.py             # Step definitions
│
├── reports/                     # Allure JSON files (generated after tests)
├── allure-report/               # HTML report (generated)
├── requirements.txt
├── README.md
└── .venv/                       # Virtual environment (excluded in .gitignore)
