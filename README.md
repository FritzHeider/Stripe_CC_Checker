# Stripe Payment Method Checker

## Overview

This Python application uses the Stripe API to validate the status of tokenized payment methods from a user-selected file. It features a Tkinter GUI for easy file selection and writes the results to a dynamically named output file, complete with date and time. Designed for security professionals or developers, this tool ensures secure and controlled validation of stored payment methods.

## Features

- **Tkinter GUI**: Simplifies the process of file selection.
- **Dynamic Output Filenames**: Includes timestamps in filenames to ensure uniqueness.
- **Detailed Console Outputs**: Provides comprehensive logs for tracking processing steps.

## Installation

### Prerequisites

- Python 3.6 or later
- `pip` for installing Python packages

### Dependencies

Install the required Python packages using `pip`:

```bash
pip install stripe
pip install python-dotenv

```
### Configuration
Create a .env file in the project root directory to securely store your Stripe API key:

Creating .env file:
```bash
plaintext
Copy code
# Add this content to your .env file
STRIPE_API_KEY=your_secret_key_here
Updating .gitignore:
```
```bash
gitignore
Copy code
# Ensure this entry is in your .gitignore to keep your secret key safe
.env
Usage
Run the script from the terminal:
```

```bash
Copy code
python stripe_payment_checker.py
Follow the GUI prompts to select your input file containing tokenized payment methods. The results will be output to a file with the format payment_status_YYYY-MM-DD_HH-MM-SS.txt.
```


### Security Practices
No Commit of Sensitive Information: Ensure sensitive keys or personal data are not pushed to version control.
Update Dependencies Regularly: Maintain updated libraries to avoid vulnerabilities.
Secure Payment Information Handling: Adhere to PCI DSS standards for payment data.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.






