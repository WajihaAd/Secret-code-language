# Secret Code Language

This is a Python program that converts input text into a secret code language and provides the functionality to decode it back to the original text.

## Description

The "Secret Code Language" program takes input text from the user and encodes it into a secret code language. It uses a simple algorithm to encode the text by shuffling characters and appending random characters to them. The encoded text is then displayed to the user.

Additionally, the program provides the option to decode the encoded text back to the original text.

## Features

- Encode input text into a secret code language.
- Decode encoded text back to the original text.
- Handles input validation for empty strings and invalid options.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Run the program:

    ```bash
    python secret_code_language.py
    ```

2. Enter the secret code language options:

    - Enter `1` for coding (encoding) the text.
    - Enter `2` for decoding the encoded text.
    - Enter `3` to quit the program.

3. Follow the prompts to enter the secret code or encoded text.

### Output Examples

- **Example 1: Coding (Encoding) Text**

    ```
    Enter the secret code:
    Hello
    Enter 1 for coding and 2 for decoding and 3 for quit: 1
    Encoded Text: kloelloh*&j
    ```

- **Example 2: Decoding Encoded Text**

    ```
    Enter the secret code:
    kloelloh*&j
    Enter 1 for coding and 2 for decoding and 3 for quit: 2
    Decoded Text: Hello
    ```

## Acknowledgments

- This program is inspired by the idea of creating a secret code language for fun and learning purposes.

