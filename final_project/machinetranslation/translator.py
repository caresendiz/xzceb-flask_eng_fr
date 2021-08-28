#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

""" import ibm watson credentials"""
authenticator = IAMAuthenticator(apikey)
"""lang translate"""
language_translator = LanguageTranslatorV3(
    version='2021-08-28',
    authenticator=authenticator
)
"""get url"""
language_translator.set_service_url(url)

def english_to_french(english_text):
    """ translate English to French """
    french_text = language_translator.translate(
    text= english_text,
    model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    """translate French to English"""
    english_text = language_translator.translate(
    text= french_text,
    model_id='fr-en').get_result()
    return english_text