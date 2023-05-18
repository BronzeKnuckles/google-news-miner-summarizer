FROM python:3.9

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY ["gnews.py","setup.py","docker-main.py","gnews/*","/app/"]
COPY gnews/ /app/gnews
RUN ls -la /app/gnews/*
RUN pip install gnews
EXPOSE 8000:8000
CMD [ "python", "docker-main.py" ]




