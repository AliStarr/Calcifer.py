FROM python:3.9
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
CMD ["src/Calcifer.py"]
ENTRYPOINT ["python3"]