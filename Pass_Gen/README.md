# Pass_Gen


In this project, I have created a Random Password Generator in both Python and C, to demonstrate the differences in how randomization is implemented in the two languages.

In Python, I used NumPy’s rand function to generate random characters. While this method works for demonstration purposes, it is not suitable for real-world security applications, as it is not cryptographically secure.

In C, I used the standard library’s rand() function along with the time library to seed and generate random outputs.

The key difference between the two implementations is in clipboard functionality — in Python, I implemented a simple function to copy the generated password directly to the clipboard. In contrast, in C, this would require learning and using an additional external library.

Overall, this project highlights the contrast between high-level simplicity in Python and low-level control in C, especially in handling randomization and external features like clipboard access.
