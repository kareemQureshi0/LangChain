from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Annotated,TypedDict,Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")

class Review(TypedDict):
    summary:Annotated[str,"A brief overview of the product"]
    sentiment:Annotated[str,"Give me Sentiment Analysis of the product either positive,negative or neutral"]
    keyThemes:Annotated[list[str],"Give me key themes of the product in a list"]
    pros:Annotated[Optional[list[str]], "Give me the pros of the product in a list"]
    cons:Annotated[Optional[list[str]],"Give me the cons of the product in a list"]
    
structuredOutput = model.with_structured_output(Review)

result = structuredOutput.invoke(""" I recently upgraded to the Apple MacBook Air M3, and I have to say, it has been an absolute joy for daily productivity! The M3 chip makes everything feel completely effortless—whether I’m compiling code, editing 4K video clips, or jumping between dozens of browser tabs. The battery life is phenomenal, easily carrying me through an entire 14-hour workday without having to reach for the MagSafe charger.

The Liquid Retina display is sharp, vibrant, and bright enough for outdoor work, and the silent, fanless design means it runs whisper-quiet even under sustained load. The keyboard and trackpad continue to be best-in-class, offering responsive typing and fluid gesture navigation. Dual external monitor support with the lid closed is also a massive workflow upgrade over previous models.

However, the base configuration still starts at just 8GB of unified memory and 256GB of storage, which fills up quickly and creates memory pressure under heavy workloads. Apple’s upgrade pricing for extra RAM and SSD capacity remains absurdly expensive. Additionally, the lack of an active cooling fan means the chassis can get noticeably warm during prolonged heavy tasks, causing thermal throttling.

Pros:
Blazing fast M3 chip with exceptional daily performance
Outstanding battery life lasting over 14 hours
Whisper-quiet fanless design and premium build quality
BrillianI recently upgraded to the Apple MacBook Air M3, and I have to say, it has been an absolute joy for daily productivity! The M3 chip makes everything feel completely effortless—whether I’m compiling code, editing 4K video clips, or jumping between dozens of browser tabs. The battery life is phenomenal, easily carrying me through an entire 14-hour workday without having to reach for the MagSafe charger.

The Liquid Retina display is sharp, vibrant, and bright enough for outdoor work, and the silent, fanless design means it runs whisper-quiet even under sustained load. The keyboard and trackpad continue to be best-in-class, offering responsive typing and fluid gesture navigation. Dual external monitor support with the lid closed is also a massive workflow upgrade over previous models.

However, the base configuration still starts at just 8GB of unified memory and 256GB of storage, which fills up quickly and creates memory pressure under heavy workloads. Apple’s upgrade pricing for extra RAM and SSD capacity remains absurdly expensive. Additionally, the lack of an active cooling fan means the chassis can get noticeably warm during prolonged heavy tasks, causing thermal throttling.

Pros:
Blazing fast M3 chip with exceptional daily performance
Outstanding battery life lasting over 14 hours
Whisper-quiet fanless design and premium build quality
Brilliant Liquid Retina display and top-tier trackpad

Cons:
Base model comes with only 8GB RAM and 256GB SSD
Extremely expensive memory and storage upgrade costs
Thermal throttling occurs during sustained, intensive workloads
Limited port selection requires dongles for legacy USB-A accessoriest Liquid Retina display and top-tier trackpad

""")

print(result)


# literal can also be provided
# The problem is runtime data validation