# frontend/Dockerfile

# Используем базовый образ Node.js
FROM node:14

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json в контейнер
COPY package.json /app/

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы проекта в контейнер
COPY . /app/

# Сборка приложения для production
RUN npm run build

# Открываем порт 8080 для доступа к приложению
EXPOSE 8080

# Команда для запуска приложения
CMD ["npm", "run", "serve"]