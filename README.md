# bdd_automation
Automation Web and Desktop App Testing Using Pyhton, Allure, and Gerkhin 

🧪 Behave BDD Automation with Allure Report (Python + Selenium)
This project runs automated UI tests (e.g., YouTube search) using Behave BDD with Allure reporting.

✅ Prerequisites
Make sure you have the following installed:

Tool	Version/Command
Python	3.8+ (python --version)
pip	latest (python -m pip install --upgrade pip)
Google Chrome	Installed
ChromeDriver	Match your Chrome version
Git	Installed

🔧 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
🛠️ 2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate    # Windows
# Or
source .venv/bin/activate # macOS/Linux
📦 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt, create it with:

txt
Copy
Edit
behave
selenium
allure-behave
pyautogui
Install with:

bash
Copy
Edit
pip install behave selenium allure-behave pyautogui
🧪 4. Run the Behave Test with Allure Formatter
bash
Copy
Edit
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
This will run all feature files in the features/ directory and generate raw Allure JSON results into the reports/ folder.

📈 5. Install Allure CLI (to Generate Web Reports)
🅰️ Option A – Using Scoop (Windows)
bash
Copy
Edit
scoop install allure
🅱️ Option B – Using Chocolatey (Windows)
bash
Copy
Edit
choco install allure
🅾️ Option C – Manually via ZIP
Download from https://github.com/allure-framework/allure2/releases
Then add the bin/ folder to your PATH.

🌐 6. Generate the HTML Report
bash
Copy
Edit
allure generate reports/ -o allure-report --clean
🚀 7. Open the Allure Report in Your Browser
bash
Copy
Edit
allure open allure-report
This will:

Launch a local server

Open the interactive report in your browser (http://localhost:port/)

🗂️ Project Structure
bash
Copy
Edit
your-repo-name/
│
├── features/
│   ├── example.feature
│   └── steps/
│       └── steps.py
│
├── reports/                # Allure raw JSON results
├── allure-report/          # HTML web report (after generating)
├── requirements.txt
├── README.md
└── .venv/                  # Python virtual environment (ignored in .gitignore)
