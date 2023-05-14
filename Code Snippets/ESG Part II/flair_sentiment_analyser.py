!pip install flair 

from flair.models import TextClassifier
from flair.data import Sentence
classifier = TextClassifier.load('en-sentiment')

sentence=Sentence("Adbri says that the cost of an upgrade at its Kwinana grinding plant is now estimated to be US$255 – 277m following an engineering design, schedule and budget review. The original estimate for the project in December 2020 was US$130m. The cement producer has blamed the increase in cost on mounting construction costs, a labour shortage and supply chain issues. Commissioning for the upgrade remains scheduled for the second quarter of 2024 with full operation forecast for the third quarter. Adbri's chief executive officer Mark Irwin said, While we are disappointed the project cost is materially higher than initially forecasted, we remain confident the Kwinana Upgrade will support solid returns over the long term. The project continues to have a positive net present value. We have used this review period to also strengthen our project delivery team, adding experience and capability. He added The consolidation of Adbri's two existing cement production sites in Western Australia into a single, world class facility at Kwinana positions Adbri to take advantage of continued growth in the local market. We also expect to deliver greater operational savings than originally forecasted.")
classifier.predict(sentence)
sentence.labels

#'POSITIVE' (0.9985)
