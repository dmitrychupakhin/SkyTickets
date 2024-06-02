# backend/Dockerfile

# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY r.txt /app/

# Устанавливаем зависимости
RUN pip install -r r.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]