FROM python:3.9

RUN pip install discord.py
RUN pip install python-dotenv
RUN pip install requests
COPY bot.py ./
CMD ["python3", "bot.py"]
