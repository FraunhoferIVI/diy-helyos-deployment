FROM python:3.8

WORKDIR /app
COPY ./build_python_image/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY src/ src/
EXPOSE 9002:9002

# Run the application using Gunicorn
WORKDIR /app/src
CMD ["gunicorn","-w","4","-b","0.0.0.0:9002", "service:app"]
