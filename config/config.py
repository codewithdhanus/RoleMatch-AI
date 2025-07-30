import os
from dotenv import load_dotenv

load_dotenv()

# Google Gemini API Key - now tries both possible environment variable names
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("No Google API key found. Please set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file")
print("GOOGLE_API_KEY found:", GOOGLE_API_KEY)

# Pinecone API Key and Index Name
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east1-gcp")  # Default if not set
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "role-comparison-index")

# Other configurations
PDF_CHUNK_SIZE = int(os.getenv("PDF_CHUNK_SIZE", 1000))
PDF_CHUNK_OVERLAP = int(os.getenv("PDF_CHUNK_OVERLAP", 100))
ROLE_EXTRACTION_PROMPT = os.getenv(
    "ROLE_EXTRACTION_PROMPT",
    "List all the job roles or titles mentioned in the following document. "
    "Provide a comma-separated list of unique roles. If no roles are found, respond with 'None'."
)
FUZZY_MATCH_THRESHOLD = int(os.getenv("FUZZY_MATCH_THRESHOLD", 80))