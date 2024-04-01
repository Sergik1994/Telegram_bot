FROM python:3.10-slim
ENV TOKEN='6890809775:AAG9LzHoZE2UjCNQZIRMEkfcQ8eNhGMtf_I'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]