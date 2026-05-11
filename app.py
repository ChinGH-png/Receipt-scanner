import streamlit as st
import base64
import json
from io import BytesIO
from openai import OpenAI
from PIL import Image

# Initialize OpenAI Client
client = OpenAI(api_key="(YOUR OWN API KEY")

st.set_page_config(page_title="AI Receipt Extractor", layout="centered")
st.title("🧾 OpenAI Receipt Extractor")

# Helper: Convert PIL Image to Base64 for OpenAI API
def encode_image(image):
    buffered = BytesIO()

    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")

    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

uploaded_file = st.file_uploader("Upload a receipt", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt", use_container_width=True)
    
    if st.button("Extract Data with GPT-4o"):
        base64_image = encode_image(image)
        
        with st.spinner("GPT-4o is reading your receipt..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-2024-08-06", # Or "gpt-4o-mini" for faster/cheaper runs
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "Extract the merchant, date, and total amount from this receipt."},
                                {
                                    "type": "image_url",
                                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                                },
                            ],
                        }
                    ],
                    # This is the magic: Structured Outputs
                    response_format={
                            "type": "json_schema",
                            "json_schema": {
                                "name": "receipt_extraction",
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "merchant_name": {"type": "string"},
                                        "date": {"type": "string"},
                                        "total_amount": {"type": "number"},
                                        "currency": {"type": "string"}
                                    },
                                    "required": ["merchant_name", "date", "total_amount", "currency"],
                                    "additionalProperties": False
                                },
                                "strict": True
                            }
                        }
                )
                
                # Parse the response
                st.session_state.extracted_data = json.loads(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")

# Display Editable Form
# Display Editable Form
if "extracted_data" in st.session_state:
    st.divider()
    data = st.session_state.extracted_data
    
    with st.form("edit_form"):
        st.subheader("Review Extracted Information")
        
        # We use .get() to avoid errors if a field is missing
        merchant = st.text_input("Merchant Name", value=data.get("merchant_name", ""))
        date = st.text_input("Date", value=data.get("date", ""))
        
        # Create two columns for Amount and Currency to look professional
        col1, col2 = st.columns(2)
        with col1:
            total = st.number_input("Total Amount", value=float(data.get("total_amount", 0.0)))
        with col2:
            currency = st.text_input("Currency", value=data.get("currency", ""))
        
        if st.form_submit_button("Submit Data"):
            # Display a success message with the final data
            st.success("Information Verified!")
            st.write(f"Record Saved: {merchant} | {currency} {total} on {date}")
