# Base image 
FROM python:3.10-slim

# workdir
WORKDIR /app

# Copy command
COPY . /app


# run command
RUN pip install --no-cache-dir -r requirements.txt

# port
EXPOSE 8080



# command
CMD ["python", "./app.py"]