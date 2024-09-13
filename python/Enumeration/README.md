 
# Enum

In this project, we explore Python's built-in enumeration functionality using `import enum`.

## Description

Let's say we want a consistent set of application exceptions. Each exception should have:

- **`code`:** An integer value.
- **`message`:** A descriptive message (e.g., "Something caused an xxx error").
- **`type`:** The exception type (e.g., `ValueError`) to be used when raising the error.

We'll create an enumeration called `AppException` with these members and the ability to `throw` errors with custom messages.

## My Approach

1. **Customizing Enumeration Members:** 
   Since we want members with multiple properties, we override the `__new__` method:

   ```python
   import enum

   @enum.unique
   class AppException(enum.Enum):
       def __new__(cls, code, type_, message):
           member = object.__new__(cls)
           member.code = code
           member._value_ = code 
           member.message = message
           member.type = type_
           return member
   ```

2. **Adding the `throw` Method:**
   We extend the functionality with a `throw` method to mimic exception raising:

   ```python
       def throw(self, message=None):
           if message is None:
               raise self.type(self.message)
           raise self.type(message) 
   ```

3. **Creating Enumeration Examples:**

   ```python
   CONNECTION_TIMEOUT = (100, TimeoutError, 'Default connection timeout error')
   ARITHMETIC_ERROR = (200, ArithmeticError, 'Default arithmetic error')
   ```

4. **Testing:**

   ```python
   if __name__ == '__main__':
       # Accessing by code
       timeout_exc = AppException(100) # <AppException.CONNECTION_TIMEOUT: 100>

       print(list(AppException))  # List all available exceptions

       try:
           AppException.CONNECTION_TIMEOUT.throw()  # Throw with the default message
       except TimeoutError as error:
           print('Caught timeout error:', error)

       try:
           AppException.ARITHMETIC_ERROR.throw('Custom error message') 
       except ArithmeticError as error:
           print('Caught arithmetic error:', error) 
   ```
 
