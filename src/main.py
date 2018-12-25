import sys
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

def sameple_analyze_sentiment(content):
    client = language_v1.LanguageServiceClient()


    #content = "Your text to analyze"

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')
    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content':content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))


def main():
    sameple_analyze_sentiment("Love")


if __name__ == "__main__":
    main()