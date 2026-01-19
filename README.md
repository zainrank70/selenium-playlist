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

#### 8. Dynamic Dropdowns / Autocomplete (Lines 132-165)
- **Dynamic Dropdowns** - Dropdowns that populate based on user input (e.g., search suggestions)
- **Wait for suggestions** - Use `wait.until(EC.presence_of_element_located(...))` before finding dropdown options
- **find_elements() with loops** - Find all suggestions and iterate through them
- **Conditional selection** - Use `if "keyword" in option.text.lower()` to find matching options
- **enumerate()** - Get index and element when looping: `for index, option in enumerate(options)`
- **Break on match** - Use `break` to stop iteration after clicking desired option
- **Real-world example** - Flipkart search autocomplete with dynamic suggestions

#### 9. Login Automation (Lines 167-204)
- **Element Click Interception** - Handle overlays/modals that block clicks
- **element_to_be_clickable()** - Wait for element to be both present and clickable
- **scrollIntoView()** - Scroll element into view before clicking: `driver.execute_script("arguments[0].scrollIntoView(true);", element)`
- **JavaScript click fallback** - Use `driver.execute_script("arguments[0].click();", element)` if regular click fails
- **Form filling** - Enter username and password in login forms
- **Wait for form elements** - Use explicit waits for form fields to load after navigation
- **Submit forms** - Click submit buttons with proper waits

#### 10. ActionChains & Mouse Hover (Lines 375-399)
- **ActionChains** - Import from `selenium.webdriver.common.action_chains` for advanced mouse and keyboard actions
- **duration parameter** - Set action speed in milliseconds: `ActionChains(driver, duration=2000)`
- **move_to_element()** - Move mouse to hover over an element
- **click()** - Click action (can be chained with move_to_element)
- **perform()** - Execute all queued actions (required at the end of action chain)
- **Action chaining** - Actions can be chained together and must end with `.perform()`
- **Order matters** - Sequence is important: hover first to reveal dropdown, then click the option
- **Other methods**: `double_click()`, `drag_and_drop()`, `drag_and_drop_by_offset()`, `key_down()`, `key_up()`
- **Simple click**: For regular clicks, `move_to_element()` is not needed - click automatically moves to element

### Important Notes

- **Quotes**: Use double quotes for ID, NAME, CLASS_NAME, LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, and CSS_SELECTOR. Use single quotes for XPath.
- **Attributes**: Use square brackets `[]` for attributes in CSS_SELECTOR, and `@` symbol for attributes in XPath.
- **Detach Option**: The code uses `detach=True` to keep the browser open after script execution for inspection.
- **Unique Elements**: Always aim for unique locators. CLASS_NAME is often not unique, so prefer ID, or use CSS_SELECTOR/XPath with more specific attributes.
- **Element Storage**: Store frequently used elements in variables to avoid repeated DOM queries (better performance).
- **Waits**: Use `WebDriverWait` with `expected_conditions` instead of `time.sleep()` when possible for better reliability.
- **find_elements() vs find_element()**: Use `find_elements()` (plural) to get a list when multiple elements match, `find_element()` (singular) returns only the first match.
- **Select Class**: Always use Selenium's `Select` class for `<select>` dropdowns rather than clicking options directly.
- **Dynamic Dropdowns**: Always wait for suggestions to appear before finding elements. Use `wait.until(EC.presence_of_element_located(...))` before calling `find_elements()`.
- **Element Click Interception**: If clicks are intercepted by overlays, use `element_to_be_clickable()`, `scrollIntoView()`, or JavaScript click as fallback.
- **String Matching in Loops**: Remember to use quotes for strings when checking: `if "keyword" in text.lower()` not `if keyword in text.lower()`.
- **ActionChains**: Always call `.perform()` at the end of action chains to execute actions. Order matters - hover first to reveal dropdowns before clicking options.
- **Implicit vs Explicit Waits**: Use `implicitly_wait()` for global waits, but prefer explicit waits (`WebDriverWait`) for specific elements as they're more reliable.

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

All code examples are currently commented out. To run a specific example:

1. Uncomment the desired section in `main.py`
2. Ensure all required imports are included
3. Run the script:
```bash
python main.py
```

**Example**: To test dynamic dropdown handling, uncomment the "Handle dynamic dropdowns flipkart" section (lines 132-165) and run the script.

### Code Structure

The `main.py` file is organized into commented sections:
1. **Basic Locators** - ID, NAME, CLASS_NAME, LINK_TEXT, PARTIAL_LINK_TEXT
2. **CSS Selector** - Attribute-based element selection
3. **XPath** - Various XPath strategies (basic, text-based, functions, navigation)
4. **SendKeys & Alert Handling** - Input manipulation and alert interactions
5. **Checkbox Selection** - Multiple checkbox handling with conditions
6. **Static Dropdown Handling** - Select class for standard dropdowns
7. **Dynamic Dropdowns** - Autocomplete/suggestion dropdowns with wait strategies
8. **Login Automation** - Form filling, handling click interceptions, and form submission
9. **Implicit Wait** - Global wait strategy with poll frequency
10. **Explicit Wait** - Condition-based waits with custom poll frequency
11. **Common Exceptions** - StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException
12. **ActionChains & Mouse Hover** - Advanced mouse actions and hover automation (currently active)

Each section contains commented-out example code that can be activated by uncommenting and ensuring the required imports are included.
