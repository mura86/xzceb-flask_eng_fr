"""Translator EN/FR/EN"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(text1):
    """this function translates EN to FR"""
    #write the code here
    french_text = language_translator.translate(text=text1, model_id='en-fr').get_result()
    
    return french_text.get("translations")[0].get("translation")

def french_to_english(text1):
    """this function translates FR to EN"""
    #write the code here
    english_text = language_translator.translate(text=text1, model_id='fr-en').get_result()

    return english_text.get("translations")[0].get("translation")
