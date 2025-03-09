# Justia Lawyer Scraper

This project is a **web scraper** that extracts **lawyer information** from Justia's directory of family law attorneys in **Chicago, Illinois**. The scraper uses **Selenium** to navigate through multiple pages and collect details such as names, profile links, phone numbers, images, descriptions, and consultation availability.

## 📌 Features
- **Automated Pagination**: Scrapes all available pages.
- **Data Extraction**: Collects lawyer details (name, profile link, phone, website, etc.).
- **CSV Export**: Saves the scraped data into `justia_lawyers_selenium.csv`.
- **Error Handling**: Handles missing elements to avoid crashes.
- **Headless Mode**: Runs without opening a browser window.

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/justia-scraper.git
cd justia-scraper
```

### **2️⃣ Install Dependencies**
Ensure you have **Python 3.x** installed. Then, install the required packages:
```bash
pip install selenium webdriver-manager pandas
```

### **3️⃣ Run the Scraper**
```bash
python justia_scraper.py
```

## 📂 Project Structure
```
justia-scraper/
│── justia_scraper.py      # Main scraping script
│── justia_lawyers_selenium.csv  # Output file (generated after running the script)
│── README.md              # Documentation
│── requirements.txt       # List of dependencies
```

## 📝 Dependencies
- `selenium` → For browser automation
- `webdriver-manager` → Auto-downloads the correct ChromeDriver
- `pandas` → For saving scraped data in CSV format

To install dependencies manually, run:
```bash
pip install -r requirements.txt
```

## 🛑 Notes
- This scraper **runs in headless mode** to improve efficiency.
- Ensure that **Google Chrome is installed** on your system.
- **IP Blocking Warning**: Running the scraper too frequently may lead to blocking. Consider using **proxies** if needed.

## 🚀 Future Enhancements
- Add **proxy rotation** to avoid detection.
- Improve **error handling and logging**.
- Support **other lawyer categories or cities**.

## 📜 License
This project is licensed under the MIT License.

---
Developed by [Yuri P.](https://github.com/yp-data) 🚀

