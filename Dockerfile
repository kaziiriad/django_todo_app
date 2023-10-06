# Python runtime
FROM python:3.8

# Set environment variables for Djangodoc
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=todo_list.settings

# Create and set the working directory
RUN mkdir /home/app
WORKDIR /home/app

#copying the dependency list
COPY ./requirements.txt /home/app/

# Install any needed packages. 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the current directory contents into the container at /home/app/ 
COPY . /home/app/


#Make port 8000 available to the world outside the container
EXPOSE 8000

# Define the default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

