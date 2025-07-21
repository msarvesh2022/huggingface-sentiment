# Base image 
FROM python:3.10-slim

# workdir
WORKDIR /app

# Copy command
COPY . /app


# run command
RUN pip install --no-cache-dir -r requirements.txt

# port
EXPOSE 5000



# command
CMD ["python", "./app.py"]