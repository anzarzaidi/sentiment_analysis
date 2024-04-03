

def analyze_sentiment() -> None:

    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient
    endpoint = "https://sentimentanzar.cognitiveservices.azure.com/"
    key = "c8b97a9d92b44575aa463c2c082ebaac"

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    input_file = open('detailed_analysis.csv', 'r')
    output_file = open('output.csv', 'w')
    for f in input_file.readlines():
        sections = f.split("|")
        url = sections[0]
        title = sections[1]
        text = sections[2]
        image_url = sections[3].replace("\n","")

        print(text)
        documents = [text]
        try:
            result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
            temp = result[0]
            sentiment =temp.sentiment
            score = temp.confidence_scores
            output_file.write(sentiment +"|" + url + "|" + title + "|" + text + "|" + str(score) + "|" + image_url +'\n')
            output_file.flush()
        except Exception as e:
            print(e)



if __name__ == '__main__':
    analyze_sentiment()