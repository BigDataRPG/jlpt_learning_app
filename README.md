# JLPT Learning App

![License](https://img.shields.io/github/license/BigDataRPG/jlpt_learning_app)
![Issues](https://img.shields.io/github/issues/BigDataRPG/jlpt_learning_app)
![Stars](https://img.shields.io/github/stars/BigDataRPG/jlpt_learning_app)

JLPT Learning App is a web application designed to help users learn Japanese words and prepare for the JLPT exam. The app provides features to memorize words with sentence examples, pronunciation with sound, and pictures for each sentence example and word.

## Features

- **Word Memorization**: Select and learn Japanese words with contextual sentence examples.
- **Pronunciation**: Hear the pronunciation of words and sentences using text-to-speech.
- **Images**: Visualize words and sentences with relevant images.
- **Random Word Selection**: Randomly select a word from a CSV file.
- **Example Sentences**: Generate example sentences using LLMs.

## Installation

To get started with the JLPT Learning App, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/BigDataRPG/jlpt_learning_app.git
    cd jlpt_learning_app
    ```

2. **Install Poetry** (if not already installed):
    ```sh
    pip install poetry
    ```

3. **Install the dependencies:**
    ```sh
    poetry install
    ```

## Usage

To run the JLPT Learning App, use the following command:

```sh
poetry run streamlit run jlpt_learning_app/app.py
```

This will start the Streamlit app, and you can access it in your web browser at `http://localhost:8501`.

## Project Structure

```
jlpt_learning_app/
│
├── jlpt_learning_app/
│   ├── __init__.py
│   └── app.py
│
├── tests/
│   └── __init__.py
│
├── .gitignore
├── pyproject.toml
├── README.md
└── poetry.lock
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please open an issue on the [GitHub repository](https://github.com/BigDataRPG/jlpt_learning_app).

---

© 2024 BigDataRPG. All rights reserved.
