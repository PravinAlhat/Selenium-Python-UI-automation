FROM python:3.13-slim

WORKDIR /app

COPY . .

CMD ["pytest", "-s", "-v", "--browser", "chrome", "--url", "https://www.letskodeit.com/practice", "--headless", "Y", "tests/"]
