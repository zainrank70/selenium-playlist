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

### Topics Covered

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
- **ancestor::** - Navigate from child to parent/grandparent
- **Relative vs Absolute**: 
  - `//` (double slash) = Relative XPath
  - `/` (single slash) = Absolute XPath
- **last()** - Select the last element: `(//input[@value='radio'])[last()]`
- **position()** - Select by position: `[position()<3]` for first 2 elements

#### 4. SendKeys, Click, Get and Clear Input Text (Lines 58-83)
- **send_keys()** - Type text into input fields
- **clear()** - Clear input field content
- **click()** - Click on elements (buttons, links, checkboxes, etc.)
- **element.text** - Get visible text of an element
- **get_attribute()** - Get attribute values (e.g., `value`, `id`, `name`)
- **Element Storage** - Store elements in variables to avoid repeated queries

#### 5. Alert Handling & Wait Time (Lines 58-83)
- **WebDriverWait** - Explicit wait for elements/conditions
- **expected_conditions (EC)** - Wait for specific conditions to be met
- **alert_is_present()** - Wait for alert dialog to appear
- **alert.accept()** - Accept/OK the alert
- **alert.dismiss()** - Cancel/dismiss the alert (not shown in current code)
- **time.sleep()** - Fixed time delay (use sparingly, prefer WebDriverWait)

#### 6. Checkbox Selection with Conditions (Lines 85-108)
- **find_elements()** - Find multiple elements (returns list)
- **Loop through checkboxes** - Select all or specific checkboxes
- **Conditional selection** - Skip certain checkboxes using conditions
- **Dynamic checkbox selection** - Using loops and f-strings: `f"//input[@value='option{i}']"`
- **starts-with() with checkboxes** - `//input[starts-with(@name, 'checkBoxOption')]`
- **Using index** - `checkboxes.index(checkbox)+1` for conditional logic

#### 7. Dropdown Handling (Lines 110-130)
- **Select class** - Import from `selenium.webdriver.support.select`
- **Static Dropdowns** - Standard `<select>` elements
- **select_by_index()** - Select option by index (0-based)
- **select_by_visible_text()** - Select option by visible text
- **select_by_value()** - Select option by value attribute
- **driver.maximize_window()** - Maximize browser window for better visibility

### Important Notes

- **Quotes**: Use double quotes for ID, NAME, CLASS_NAME, LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, and CSS_SELECTOR. Use single quotes for XPath.
- **Attributes**: Use square brackets `[]` for attributes in CSS_SELECTOR, and `@` symbol for attributes in XPath.
- **Detach Option**: The code uses `detach=True` to keep the browser open after script execution for inspection.
- **Unique Elements**: Always aim for unique locators. CLASS_NAME is often not unique, so prefer ID, or use CSS_SELECTOR/XPath with more specific attributes.
- **Element Storage**: Store frequently used elements in variables to avoid repeated DOM queries (better performance).
- **Waits**: Use `WebDriverWait` with `expected_conditions` instead of `time.sleep()` when possible for better reliability.
- **find_elements() vs find_element()**: Use `find_elements()` (plural) to get a list when multiple elements match, `find_element()` (singular) returns only the first match.
- **Select Class**: Always use Selenium's `Select` class for `<select>` dropdowns rather than clicking options directly.

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

Run the main script (currently demonstrates static dropdown handling):
```bash
python main.py
```

To test other strategies, uncomment the relevant sections in `main.py` and comment out the current active code.

### Code Structure

The `main.py` file is organized into commented sections:
1. **Basic Locators** - ID, NAME, CLASS_NAME, LINK_TEXT, PARTIAL_LINK_TEXT
2. **CSS Selector** - Attribute-based element selection
3. **XPath** - Various XPath strategies (basic, text-based, functions, navigation)
4. **SendKeys & Alert Handling** - Input manipulation and alert interactions
5. **Checkbox Selection** - Multiple checkbox handling with conditions
6. **Dropdown Handling** - Static and dynamic dropdown selection (currently active)

Each section contains commented-out example code that can be activated by uncommenting and ensuring the required imports are included.
