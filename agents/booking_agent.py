

from dataclasses import dataclass

from pydantic_ai import Agent, RunContext

from models.booking import Booking

from dotenv import load_dotenv

load_dotenv()

@dataclass
class SupportDependencies:
  api_url: str

support_agent = Agent(  
  'openai:gpt-4o',  
  deps_type=SupportDependencies,
  result_type=str,  
  system_prompt=(  
    'You are a support agent to retrieve bookings'
  ),
)

@support_agent.tool
async def get_bookings(ctx: RunContext[SupportDependencies]) -> list[Booking]:
  """Returns all bookings"""
  print('calling get all bookings: ', ctx.deps.api_url)
  return [
    Booking(id='OTBH1234', hotel_id=1234, hotel_name='marosol suites 2', arrival_date='2025-01-01'),
    Booking(id='OTBH1233', hotel_id=1234, hotel_name='marosol suites 3', arrival_date='2025-01-02'),
    Booking(id='OTBH1235', hotel_id=1234, hotel_name='marosol suites 4', arrival_date='2025-01-03'),
    Booking(id='OTBH1235', hotel_id=1234, hotel_name='Ibiza Rocks 4', arrival_date='2025-01-03')
  ]

@support_agent.tool
async def get_single_booking(ctx: RunContext[SupportDependencies], booking_id: str) -> Booking:
  """Returns all bookings"""
  print('calling get single booking: ', ctx.deps.api_url)
  return Booking(id='OTBH1234', hotel_id=1234, hotel_name='marosol suites 1', arrival_date='2025-01-01')

@support_agent.tool
async def delete_booking(ctx: RunContext[SupportDependencies], booking_id: str) -> None:
  """Delete booking by booking id"""
  print('calling delete booking: ', booking_id)