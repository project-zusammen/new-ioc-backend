# Use an official Python runtime as the base image
FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install additional tools (e.g., black, pylint, etc.)
RUN pip install black pylint

# # Set up a non-root user (optional but recommended)
# RUN useradd -m vscode
# USER vscode

# Set the working directory
WORKDIR /workspace

# Expose ports if needed
EXPOSE 5000