import json
import streamlit as st
import pandas as pd

from agents.booking_agent import SupportDependencies, support_agent
from services.chat_service import ChatService

prompt = st.chat_input('Say something!')

chat_service = ChatService()

if prompt:

  deps = SupportDependencies(api_url='random url')
  result = support_agent.run_sync(prompt, deps=deps)  
  print(result.data)
  st.write(result.data)  
  # st.write('The user has sent: ', prompt)

  # response = chat_service.chat(prompt)

  # st.write('The AI has responded: ', response)
  # bookings = [
  #   {
  #     "id": "OTBH3821",
  #     "arrival_date": "2024-11-15"
  #   },
  #   {
  #     "id": "OTBH9472",
  #     "arrival_date": "2024-11-16"
  #   },
  #   {
  #     "id": "OTBH94723",
  #     "arrival_date": "2024-11-16"
  #   },
  #   {
  #     "id": "OTBH94723",
  #     "arrival_date": "2024-12-01"
  #   },
  #   {
  #     "id": "OTBH6549",
  #     "arrival_date": "2024-12-27"
  #   }
  # ]

  # extended_prompts = f"""
  #   Using this booking data:
  #   {json.dumps(bookings)}
  #   Generate a timeseries chart that shows the trend of bookings over time. 
  #   The chart should:
  #   1. Display the number of bookings per day on the y-axis
  #   2. Show dates on the x-axis
  #   3. Include a clear title "Booking Trends Over Time"
  #   4. Have properly labeled axes
  #   5. Use a blue line for the trendPlease create and display this chart directly, not just provide code for it. I want to see the actual visualization based on my data.
  #   6. Plot point for each day, if the aggregated value is zero then plot zero for that date.

  #   Just the code, don't respond like a human
  #   Don't wrap the response in anything like ```python ... ```
  #   Don't use matplotlib, just use st.line_chart or otherwise (some other st.)
  # """

  # # extended_prompts = f"""
  # #   Given a list of bookings like [
  # #       {{"id": "OTBH3821", "arrival_date": "2024-11-15"}},
  # #       {{"id": "OTBH9472", "arrival_date": "2025-01-03"}}
  # #   ]
  # #   {prompt}
  # #   Generate a time series chart, could use st or pd (pandas).
  # #   Just the code, don't respond like a human
  # #   Don't wrap the response in anything like ```python ... ```
  # #   Just use some st. command for charts
  # #   """

  # response = chat_service.chat(extended_prompts)
  # print('response: ', response)
  # exec(response)
  