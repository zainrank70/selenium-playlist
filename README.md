# selenium-playlist

## Selenium Practice Tasks - Locator Strategies

This repository contains Selenium WebDriver automation practice scripts covering all major locator strategies and techniques.

### Practice Website

**Testing Link:** [Rahul Shetty Academy - Automation Practice](https://rahulshettyacademy.com/AutomationPractice/)

This practice page includes various automation scenarios:
- Radio Button Examples
- Dropdown Examples
- Checkbox Examples
- Switch Window/Tab Examples
- Alert Handling
- Web Tables
- Mouse Hover
- iFrame Examples
- And more...

### Locator Strategies Covered

#### 1. Basic Locators (Lines 8-21)
- **By.ID** - Find elements by unique ID attribute
- **By.NAME** - Find elements by name attribute
- **By.CLASS_NAME** - Find elements by class name (note: may not be unique)
- **By.LINK_TEXT** - Find links by exact visible text
- **By.PARTIAL_LINK_TEXT** - Find links by partial visible text

#### 2. CSS Selector (Lines 24-36)
- Use when ID, NAME, or CLASS_NAME are not unique
- Syntax: `[attribute='value']` with double quotes
- Example: `[value='radio2']`

#### 3. XPath (Lines 38-58)
- **Basic XPath**: `//input[@value='radio2']`
- **Text-based**: `//legend[text()='Suggestion Class Example']`
- **starts-with()**: `//input[starts-with(@value, 'rad')]` - For dynamic values
- **contains()**: `//input[contains(@value, 'adio')]` or `//legend[contains(text(), 'Class Example')]` - For partial matching
- **Parent-Child Navigation**: `//div[@id='radio-btn-example']/fieldset/label[@for='radio3']/input`
- **Relative vs Absolute**: 
  - `//` (double slash) = Relative XPath
  - `/` (single slash) = Absolute XPath

### Important Notes

- **Quotes**: Use double quotes for ID, NAME, CLASS_NAME, LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, and CSS_SELECTOR. Use single quotes for XPath.
- **Attributes**: Use square brackets `[]` for attributes in CSS_SELECTOR, and `@` symbol for attributes in XPath.
- **Detach Option**: The code uses `detach=True` to keep the browser open after script execution for inspection.
- **Unique Elements**: Always aim for unique locators. CLASS_NAME is often not unique, so prefer ID, or use CSS_SELECTOR/XPath with more specific attributes.

### Setup

1. Create a virtual environment:
```bash
python -m venv env
```

2. Activate the virtual environment:
```bash
# Windows
env\Scripts\activate

# Linux/Mac
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install selenium directly:
```bash
pip install selenium
```

### Usage

Run the main script (currently demonstrates XPath parent-child navigation):
```bash
python main.py
```

To test other locator strategies, uncomment the relevant sections in `main.py` and comment out the current active code.
