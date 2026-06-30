FROM python:3.12-slim


WORKDIR /app/Freelance_Marketplace


COPY . . 


RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /app/Freelance_Marketplace/Freelance_Marketplace

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

