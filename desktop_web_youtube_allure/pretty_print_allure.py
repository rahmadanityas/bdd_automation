import os
import json

report_dir = "reports"
for filename in os.listdir(report_dir):
    if filename.endswith(".json"):
        file_path = os.path.join(report_dir, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
print("✅ Allure JSON files have been pretty-printed.")
