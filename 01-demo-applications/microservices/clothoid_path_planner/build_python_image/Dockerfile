FROM python:3.8
WORKDIR /app
COPY ./build_python_image/requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 9002:9002
CMD ["python", "./src/service.py"]
