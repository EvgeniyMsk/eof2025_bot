FROM python:3.12


WORKDIR /eof2025_bot


COPY ./requirements.txt /eof2025_bot/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /eof2025_bot/requirements.txt


COPY . /eof2025_bot/


CMD ["python", "main.py"]