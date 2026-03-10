# Invoice Extractor

An AI-powered invoice analysis web application built with **Google Gemini 2.5 Flash** and **Streamlit**. Upload any invoice image and ask questions about it in plain English — the app will intelligently extract and interpret the information for you.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Screenshot](#screenshot)
- [Author](#author)

---

## Overview

The **Invoice Extractor** leverages Google's multimodal Gemini AI model to understand invoice images. Instead of manually reading through invoices, users can upload an image and ask questions like:

- *"What is the total amount due?"*
- *"Who is the vendor?"*
- *"List all the line items."*
- *"What is the invoice date and due date?"*

The model processes both the image and the user's question together to return a precise, context-aware answer.

---

## Features

- Upload invoice images in **JPG, JPEG, or PNG** format
- Ask free-form natural language questions about the invoice
- Powered by **Gemini 2.5 Flash** — fast, accurate, and free-tier compatible
- Clean and minimal **Streamlit** UI
- Real-time AI response rendering

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.9+ | Core programming language |
| Streamlit | Web application framework |
| Google Generative AI SDK | Interface with Gemini 2.5 Flash model |
| Pillow (PIL) | Image loading and display |
| python-dotenv | Environment variable management |

---

## Project Structure

```
Invoice-Recognition/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # API key configuration (not committed to version control)
└── README.md            # Project documentation
```

---

## Prerequisites

- Python 3.9 or higher
- A valid **Google Gemini API key**
  - Get one for free at [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/Invoice-Recognition.git
   cd Invoice-Recognition
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

Create a `.env` file in the project root directory and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> **Important:** Never commit your `.env` file to version control. Add it to `.gitignore` to keep your API key secure.

---

## Usage

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

3. In the web interface:
   - Enter your question or prompt in the **Input Prompt** field *(e.g., "What is the total amount?")*
   - Click **Browse files** to upload an invoice image (JPG, JPEG, or PNG)
   - Click **Tell me the invoice details**
   - The AI response will appear below

---

## How It Works

1. **Image Ingestion** — The uploaded image is read as raw bytes and packaged with its MIME type into a format accepted by the Gemini API.
2. **Prompt Construction** — A system prompt establishes that the model is an invoice expert. The user's custom query is appended alongside the image data.
3. **Gemini API Call** — The `gemini-2.5-flash` model receives the combined input (system prompt + image + user query) and generates a response.
4. **Response Display** — The AI's answer is rendered directly in the Streamlit UI.

```
User Input (text) ─┐
                   ├──► Gemini 2.5 Flash ──► AI Response
Invoice Image ─────┘
```

---

## Screenshot

> *(Add a screenshot of the running app here)*

---

## Author

**Shah Devang Deepakkumar**

---

## License

This project is intended for educational and personal use as part of a Generative AI course/project.
