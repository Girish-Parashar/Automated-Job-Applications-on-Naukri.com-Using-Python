# Naukri Auto Apply Automation

This project is an **automated job application bot** designed for **Naukri.com**, focused on **Data Analyst** job listings. Using **Selenium** ![Selenium](https://img.shields.io/badge/selenium-25B5A3?style=flat-square&logo=selenium) and **Python** ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python), it simulates user actions like logging in, applying for jobs, and answering application questions, saving time and effort.

## Features

- **Automated Login & Job Search**: Automatically logs in to Naukri.com and navigates to the Data Analyst job listings page.
- **Job Application Automation**: Automatically applies to jobs directly listed on Naukri.com, avoiding redirects to external websites.
- **Handles Application Questions**: If job application questions appear, the bot answers them with predefined responses.
- **Tab Management**: Opens and closes browser tabs efficiently to prevent unnecessary tabs from remaining open.
- **Predefined Answer Logic**: The script interacts with text input fields, radio buttons, and dropdown menus with default answers.

## Technologies Used

- **Python** ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python): Core programming language used for automation.
- **Selenium** ![Selenium](https://img.shields.io/badge/selenium-25B5A3?style=flat-square&logo=selenium): Web automation tool for interacting with Naukri.com and handling dynamic content.
- **WebDriver**: Used to simulate user actions such as clicking, typing, and navigating between pages.

## How It Works

1. **Login to Naukri**: The bot logs in to Naukri using your credentials (email & password).
2. **Job Search**: The bot navigates to the **Data Analyst** job search results page.
3. **Job Application**: It identifies job listings and applies to them directly through Naukri.com.
4. **Handling Application Questions**: If application questions appear, the bot answers them with predefined responses.

## Prerequisites

To run the project, make sure you have:

- **Python 3.x** ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python)
- **Selenium** installed: `pip install selenium`
- **ChromeDriver** installed (ensure compatibility with your version of Chrome)

## Getting Started

1. Clone the repository to your local machine.
2. Install required libraries with `pip install -r requirements.txt`.
3. Run the script using `python apply_jobs.py`.

## Contributing

Feel free to fork and submit pull requests to improve the functionality. Contributions are welcome for bug fixes, feature enhancements, or optimizations.

## License

Distributed under the MIT License. See `LICENSE` for more information.
