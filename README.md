# QA Automation Project

Automated testing project for web application using Python, Playwright and pytest.

## 📌 Overview

This project demonstrates automated UI and API testing with a focus on:
- test structure
- maintainability
- real-world testing scenarios

## 🧪 Test Coverage

### UI Testing
- Login functionality
- Positive and negative test cases
- Edge cases (empty fields, invalid input)
- Logout functionality

### API Testing
- GET and POST requests
- Status code validation
- Response data validation

## 🏗️ Project Structure
qa-automation-project/
│
├─ pages/ # Page Object Model classes
│ ├─ base_page.py
│ └─ login_page.py
│
├─ tests/ # Test files
│ ├─ test_login_positive.py
│ ├─ test_login_negative.py
│ └─ test_empty_fields.py
│
├─ data/ # Test data
│ └─ test_data.py
│
├─ requirements.txt
└─ README.md

## ⚙️ Technologies Used

- Python
- Playwright
- pytest
- requests (API testing)
- Postman (manual API testing)

## 🚀 How to Run Tests

1. Install dependencies:
  pip install -r requirements.txt
2. Run tests:


## 💡 Features

- Page Object Model (POM)
- Test parametrization (pytest)
- Separation of test data
- Handling waits and dynamic elements
- Basic API test coverage
- Clean and maintainable structure

## 🎯 Purpose

This project was created to practice QA automation skills and demonstrate understanding of:
- UI and API testing
- test design
- automation best practices
