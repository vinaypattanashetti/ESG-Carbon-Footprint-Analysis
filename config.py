"""
Configuration settings for Enterprise CarbonScope application
lays the foundation for adaptive environmental data management 
and precision-driven sustainability tracking.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Application settings
APP_NAME = "Enterprise CarbonScope"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "A lightweight, multilingual carbon accounting and reporting tool for SMEs in Asia"
APP_AUTHOR = "Vinay Pattanashetti"
APP_CONTACT = "vinaypattanashetti22@gmail.com"

# API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Data settings
DATA_DIR = "data"
EMISSIONS_FILE = os.path.join(DATA_DIR, "emissions.json")
COMPANY_INFO_FILE = os.path.join(DATA_DIR, "company_info.json")

# Supported languages
SUPPORTED_LANGUAGES = ["English", "Hindi", "French", "German"]

# Emission scopes
EMISSION_SCOPES = ["Scope 1", "Scope 2", "Scope 3"]

# Scope descriptions
SCOPE_DESCRIPTIONS = {
    "Scope 1": "Direct emissions from owned or controlled sources",
    "Scope 2": "Indirect emissions from the generation of purchased energy",
    "Scope 3": "All other indirect emissions that occur in a company's value chain"
}

# Default units
DEFAULT_UNITS = [
    "kWh",
    "MWh",
    "liter",
    "kg",
    "tonne",
    "km",
    "passenger-km",
    "cubic meter",
    "square meter",
    "hour",
    "day",
    "piece",
    "USD"
]

# Regulatory frameworks
REGULATORY_FRAMEWORKS = {
    "India PAT Scheme": "India Perform Achieve and Trade Scheme",
    "USA IRA 2022": "USA Inflation Reduction Act 2022",
    "EU CBAM": "EU Carbon Border Adjustment Mechanism",
    "France SNBC": "France National Low-Carbon Strategy (Stratégie Nationale Bas-Carbone)",
    "Germany BEHG": "Germany Fuel Emissions Trading Act (Brennstoffemissionshandelsgesetz)"
}


# Create data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)
