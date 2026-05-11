# Receipt-scanner
It is lightweight web application built with Streamlit and OpenAI's GPT-4o that automates data entry by extracting key information from receipt images using Vision AI.



Features:
Vision AI Extraction: Uses GPT-4o to "read" images without traditional OCR.

Structured Outputs: Ensures the AI returns valid JSON every time.

Interactive UI: Pre-fills a web form that allows for manual review and editing.

Cross-Format Support: Handles JPG, PNG, and transparent RGBA images.



Tech Stack:
Language: Python 3.11+

Framework: Streamlit (Frontend & UI)

AI Engine: OpenAI API (GPT-4o / GPT-4o-mini)

Image Processing: Pillow (PIL)

