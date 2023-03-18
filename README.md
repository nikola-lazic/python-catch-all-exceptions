# **Python snippet for catching all Exceptions**

This is one useful Python snippet for catching all exceptions and exporting them into TXT file.
</br>Libraries used for this are:
- traceback
- logging

</br>Example of generated crashlog: crash_log_2023-03-18_23-04-36.txt

```
ERROR:root:Traceback (most recent call last):
  File "d:/Programming/python-catch-all-exceptions/python-catch-all-exceptions.py", line 15, in <module>
    main_function()
  File "d:/Programming/python-catch-all-exceptions/python-catch-all-exceptions.py", line 8, in main_function
    print(something_undefined_or_any_error)  # Function with error (d is not defined)
NameError: name 'something_undefined_or_any_error' is not defined
```