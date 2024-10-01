# Password Complexity Checker

## Overview

The **Password Complexity Checker** is a Python tool designed to assess the strength of passwords based on specific criteria. It checks for the presence of uppercase letters, lowercase letters, numbers, special characters, and the overall length of the password. The tool also securely accepts password input and saves the plaintext password to a file.

## Features

- **Password Strength Assessment**: Evaluates the strength of the entered password based on defined criteria.
- **Masked Input**: Utilizes secure input to hide the password as it is typed.
- **Plaintext Password Storage**: Saves the entered plaintext password to a text file for later reference.

## Requirements

- Python 3.x
- Built-in libraries: `re`, `getpass`, `os`

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the script file.

```bash
git clone <repository-url>
```

3. Navigate to the project directory.

```bash
cd Password_complexity_checker
```

## Usage

1. Run the script using Python:

```bash
python password_checker.py
```

2. When prompted, enter a password. The password input will be masked (displayed as asterisks).
3. After entering the password, the tool will provide feedback on its strength and save the plaintext password to `passwords.txt`.

### Example

```bash
Enter a passwd to check its strength: ********
Strong passwd!
Password saved to 'passwords.txt'.
```

## Password Strength Criteria

The password is assessed based on the following conditions:

- Minimum length of 8 characters.
- At least one uppercase letter (A-Z).
- At least one lowercase letter (a-z).
- At least one digit (0-9).
- At least one special character (e.g., @, #, $, etc.).

## Security Considerations

- **Plaintext Storage**: This tool saves passwords in plaintext format, which may pose security risks. For production use, consider implementing hashed storage instead.
- Use this tool responsibly and ensure that sensitive data is managed securely.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for enhancements and bug fixes.

---

Feel free to modify any sections to better fit your project or personal preferences! If you need further assistance or adjustments, just let me know.
