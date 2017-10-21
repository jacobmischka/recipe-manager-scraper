FROM python

WORKDIR /app

COPY ./src /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 4000

ENTRYPOINT ["python"]
CMD ["/app/app.py"]
