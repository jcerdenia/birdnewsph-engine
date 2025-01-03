import os

from .brevo import BrevoAPI
from .ebird import EBirdAPI
from .groq import GroqAPI
from .sanity import SanityAPI
from .sheets import SheetsAPI

brevo_api = BrevoAPI()

ebird_api = EBirdAPI()

groq_api = GroqAPI()

sanity_api = SanityAPI()

sheets_api = SheetsAPI(os.getenv("SPREADSHEET_ID"))
