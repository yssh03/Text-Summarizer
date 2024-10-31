# Text Summarizer with Pegasus and FastAPI

This repository contains a text summarization application built with a fine-tuned Hugging Face model (`google/pegasus-cnn_dailymail`) on the SAMSum dataset. The application is modularized for easy maintenance and extensibility. The backend is powered by FastAPI.

## Features

- **Text Summarization**: Summarizes input text using the `google/pegasus-cnn_dailymail` model fine-tuned on the SAMSum dataset.
- **FastAPI Integration**: Provides a RESTful API to interact with the summarization model.
- **Modular Code Structure**: Organized and easy-to-read code for better maintainability.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/text-summarizer.git
    cd text-summarizer
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Start the Application

Run the application with the following command:

```bash
uvicorn app:app --reload
