FROM python:3.10

# Set working directory
WORKDIR /app

# Copy the entire project (adjust paths if needed)
COPY python ./python
COPY raw ./raw
COPY processed ./processed

# Install dependencies
RUN pip install pandas

# Run the script
CMD ["python", "python/process_nhs_data.py"]

