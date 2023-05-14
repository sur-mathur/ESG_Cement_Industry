!pip install openai
import openai
openai.api_key = "<API_KEY>"

def analyze_esg_sentiment(statement):
    retries = 3
    sentiment = None

    while retries > 0:
        messages = [
            {"role": "user", "content": f"As an AI language model specialized in ESG analysis, please analyze the following statement and identify its sentiment as either positive, negative, or neutral. Please return a JSON object that includes the sentiment word, either POSITIVE, NEGATIVE, or NEUTRAL, along with its corresponding confidence score and an explanation for the sentiment prediction. {statement}"}
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=3,
            n=1,
            stop=None,
            temperature=0
        )
        response_text = completion.choices[0].message.content
    return response_text
    
    
#INPUT:
analyze_esg_sentiment("Adbri says that the cost of an upgrade at its Kwinana grinding plant is now estimated to be US$255 – 277m following an engineering design, schedule and budget review. The original estimate for the project in December 2020 was US$130m. The cement producer has blamed the increase in cost on mounting construction costs, a labour shortage and supply chain issues. Commissioning for the upgrade remains scheduled for the second quarter of 2024 with full operation forecast for the third quarter. Adbri's chief executive officer Mark Irwin said, While we are disappointed the project cost is materially higher than initially forecasted, we remain confident the Kwinana Upgrade will support solid returns over the long term. The project continues to have a positive net present value. We have used this review period to also strengthen our project delivery team, adding experience and capability. He added The consolidation of Adbris two existing cement production sites in Western Australia into a single, world class facility at Kwinana positions Adbri to take advantage of continued growth in the local market. We also expect to deliver greater operational savings than originally forecasted.")

#OUTPUT_JSON_FROM_OPEN_API:
'''{
"sentiment": "NEGATIVE",
"confidence": 0.80,
"explanation": "The statement contains negative sentiment as Adbri has announced a cost increase of the project from US$130m to US$255 – 277m. The statement also mentions construction cost, labour shortage, and supply chain issues as reasons for the cost increase which adds to the negative sentiment. However, the CEO of Adbri Mark Irwin has said that the project will support solid returns over the long term and the project continues to have a positive net present value which shows a slightly positive sentiment. Overall, the statement has a negative sentiment with a confidence score of 0.80."
}'''