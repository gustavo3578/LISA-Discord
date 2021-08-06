"""
Connects with data sources.
"""
import requests
from requests.api import get
from lisa.settings import BACKEND_URL


class GraphQLQuery:
    """
    GraphQL Queries
    """
    @staticmethod
    def lisa_service_version():
        payload = '{ lisa }'
        request = requests.post(BACKEND_URL, json={'query': payload})

        err_msg = 'Unable to communicate with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('lisa', [err_msg])

        return response_message[-1]

    @staticmethod
    def lisa_sentiment_extraction(text):
        payload = f'''
        query{{
        sentimentExtraction(text: "{text}")
        }}
        '''
        request = requests.post(BACKEND_URL, json={'query': payload})
        
        err_msg = 'Unable to communicate with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('sentimentExtraction', err_msg)
        
        return response_message

    @staticmethod
    def lisa_sentence_segmentation(text):
        payload = f'''
        query{{
        sentenceSegmentation(text: "{text}"){{
            inputedData
            numSentences
            output
        }}
        }}
        '''
        request = requests.post(BACKEND_URL, json={'query': payload})

        err_msg = 'Unable to connect with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('sentenceSegmentation')
        response_message1 = response_message.get('numSentences', err_msg)
        return response_message1

    @staticmethod
    def lisa_text_offensive_level(text):
        payload = f'''
        query{{
        textOffenseLevel(text: "{text}"){{
            text
            average
            isOffensive
        }}
        }}
        '''
        request = requests.post(BACKEND_URL, json={'query': payload})

        err_msg = 'Unable to connect with the service!'
        response_data = request.json().get('data')
        response_message = response_data.get('textOffenseLevel')
        response_message1 = response_message.get('average', err_msg)
        return response_message1