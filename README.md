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



Requirements (can be Install):
aiohappyeyeballs==2.6.1
aiohttp==3.13.3
aiosignal==1.4.0
altair==6.1.0
annotated-types==0.7.0
anyio==4.12.1
asttokens==3.0.1
attrs==25.4.0
blinker==1.9.0
cachetools==7.1.1
certifi==2026.1.4
cffi==2.0.0
charset-normalizer==3.4.4
click==8.3.3
colorama==0.4.6
comm==0.2.3
comtypes==1.4.15
cryptography==46.0.5
debugpy==1.8.20
decorator==5.2.1
distro==1.9.0
dotenv==0.9.9
executing==2.2.1
frozenlist==1.8.0
genai==2.1.0
gitdb==4.0.12
GitPython==3.1.50
google-ai-generativelanguage==0.6.15
google-api-core==2.30.0
google-api-python-client==2.190.0
google-auth==2.49.0.dev0
google-auth-httplib2==0.3.0
google-generativeai==0.8.6
googleapis-common-protos==1.72.0
grpcio==1.78.1
grpcio-status==1.71.2
h11==0.16.0
httpcore==1.0.9
httplib2==0.31.2
httptools==0.7.1
httpx==0.28.1
idna==3.11
ipykernel==7.2.0
ipython==8.38.0
itsdangerous==2.2.0
jedi==0.19.2
Jinja2==3.1.6
jiter==0.13.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
jupyter_client==8.8.0
jupyter_core==5.9.1
MarkupSafe==3.0.3
matplotlib-inline==0.2.1
multidict==6.7.1
narwhals==2.21.0
nest-asyncio==1.6.0
numpy==2.4.4
openai==2.21.0
packaging==26.0
pandas==3.0.2
parso==0.8.6
pillow==12.2.0
platformdirs==4.9.2
prompt_toolkit==3.0.52
propcache==0.4.1
proto-plus==1.27.1
protobuf==5.29.6
psutil==7.2.2
pure_eval==0.2.3
pyarrow==24.0.0
pyasn1==0.6.2
pyasn1_modules==0.4.2
PyAudio==0.2.14
pycparser==3.0
pydantic==2.12.5
pydantic_core==2.41.5
pydeck==0.9.2
Pygments==2.19.2
pyparsing==3.3.2
pypiwin32==223
python-dateutil==2.9.0.post0
python-dotenv==1.2.1
python-multipart==0.0.28
pyttsx3==2.99
pywin32==311
pyzmq==27.1.0
referencing==0.37.0
regex==2026.2.19
requests==2.32.5
rpds-py==0.30.0
six==1.17.0
smmap==5.0.3
sniffio==1.3.1
SpeechRecognition==3.14.5
stack-data==0.6.3
starlette==1.0.0
streamlit==1.57.0
tabulate==0.9.0
tenacity==9.1.4
tiktoken==0.3.3
toml==0.10.2
tornado==6.5.4
tqdm==4.67.3
traitlets==5.14.3
typing-inspection==0.4.2
typing_extensions==4.15.0
tzdata==2026.2
uritemplate==4.2.0
urllib3==2.6.3
uvicorn==0.46.0
watchdog==6.0.0
wcwidth==0.6.0
websockets==16.0
yarl==1.22.0
