# JLPT Learning App

![License](https://img.shields.io/github/license/BigDataRPG/jlpt_learning_app)
![Issues](https://img.shields.io/github/issues/BigDataRPG/jlpt_learning_app)
![Stars](https://img.shields.io/github/stars/BigDataRPG/jlpt_learning_app)

JLPT Learning App is a web application designed to help users learn Japanese words and prepare for the JLPT exam. The app provides features to memorize words with sentence examples, pronunciation with sound, and pictures for each sentence example and word.

## Features

- **Word Memorization**: Select and learn Japanese words with contextual sentence examples.
- **Pronunciation**: Hear the pronunciation of words and sentences using text-to-speech.
- **Images**: Visualize words and sentences with relevant images.

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
