import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please set it in your .env file."
    )

# Model configuration
GROQ_MODEL = "llama3-8b-8192"   # Fast & cheap (recommended)
# GROQ_MODEL = "llama3-70b-8192"  # Higher quality

# App settings
APP_NAME = "AutoStream Social-to-Lead Agent"
TEMPERATURE = 0.3
