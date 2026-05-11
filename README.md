# Receipt-scanner
A simple web application that uses Vision AI to extract structured data from receipt images and auto-fill a digital form.


How It Works
The application functions as a bridge between unstructured image data and structured digital forms. It follows a four-stage pipeline:


1. Image Pre-processing
When a user uploads a receipt (JPG, PNG, or RGBA), the system uses the Pillow (PIL) library to handle the file. Because the OpenAI API requires a specific format, the app automatically checks for transparency layers (Alpha channels) and converts the image to a standard RGB JPEG. It then encodes the image into a Base64 string for secure transmission over the API.


2. Multimodal AI Analysis (Vision)
Instead of using traditional Optical Character Recognition (OCR)—which often struggles with tilted text, varying fonts, or crumpled paper—this app utilizes GPT-4o, a multimodal LLM. The model "looks" at the raw pixels and understands the spatial context of the receipt (e.g., knowing that a number at the bottom-right next to the word "Total" is the final price).


3. Constraint-Based Extraction (JSON Schema)
To ensure the app doesn't crash from unexpected text, we use OpenAI's Structured Outputs. We provide a strict JSON Schema that forces the AI to return only four specific data points:


Merchant Name: (String)

Date: (String)

Total Amount: (Number)

Currency: (String)


By setting strict: True, the AI is mathematically guaranteed to follow this format, making the data "machine-readable" immediately.

4. Interactive UI & Validation
The extracted JSON is parsed and used to auto-fill a Streamlit form. This allows the user to act as a "Human-in-the-loop" (HITL) to verify or correct any details before the data is final. The app uses Session State to ensure the data persists on the screen even as the user interacts with the form.



Tech Stack:

Language: Python 3.11+

Framework: Streamlit (Frontend & UI)

AI Engine: OpenAI API (GPT-4o / GPT-4o-mini)

Image Processing: Pillow (PIL)

  urllib3==2.6.3
  uvicorn==0.46.0
  watchdog==6.0.0
  wcwidth==0.6.0
  websockets==16.0
  yarl==1.22.0
