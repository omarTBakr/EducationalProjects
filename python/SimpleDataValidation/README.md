## Simple Data Validation 

This project demonstrates a basic data validation system using Python. It includes:

**Components:**

- **`template`:** A dictionary defining the expected structure and data types for user data.
- **Sample Data:**  (`john`, `eric`, `michael`) - Example dictionaries representing user information.
- **Custom Exceptions:**
    - `SchmaError`: Base exception class for schema-related errors.
    - `SchemaKeyError`:  Raised for mismatched keys between the template and data.
    - `SchemaValueError`: Raised for incorrect data types in the data.
- **Validation Functions:**
    - `validate_keys`: Checks if the keys in the data match the template.
    - `validate_types`: Verifies data types against the template.
    - `recursive_validate`: Recursively validates nested dictionaries.
    - `validate`: A wrapper function for `recursive_validate`.

**How it Works:**

1. **Template Definition:** The `template` dictionary outlines the expected structure.
2. **Data Validation:** The `validate` function is called with the `template` and the data to be validated.
3. **Recursive Validation:** The `recursive_validate` function iterates through the data, comparing keys and data types against the template. It handles nested dictionaries recursively.
4. **Error Handling:** If discrepancies are found, custom exceptions (`SchemaKeyError` or `SchemaValueError`) are raised with informative messages.

**Example Usage:**

```python
if __name__ == '__main__':
    validate(template, michael) 
```

This code snippet attempts to validate the `michael` data dictionary against the defined `template`. If the validation fails, an exception will be raised, indicating the specific error.

**Purpose:**

This project serves as an educational example of how to implement basic data validation in Python. It highlights the importance of data integrity and provides a foundation for building more complex validation systems. 
