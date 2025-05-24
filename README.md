# Сравнение REST и gRPC: Конвертер температуры на Python

Этот проект демонстрирует различия между REST API (на FastAPI) и gRPC-сервисом (на Protocol Buffers и grpcio) на примере простого микросервиса — конвертера температуры.

## 📦 Структура проекта

```
grpc_vs_rest/
├── rest_api/         # Реализация REST API на FastAPI
├── grpc_api/         # Реализация gRPC API
└── README.md         # Инструкции по запуску и описанию проекта
```

---

## 🔹 REST API (FastAPI)

### 📂 Путь: `rest_api/`

### 🖥 Установка зависимостей

```bash
cd rest_api
pip install -r requirements.txt
```

### ▶ Запуск сервера

```bash
uvicorn main:app --reload
```

### 🌐 Документация (Swagger UI)

Открой в браузере: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔸 gRPC API (grpcio + protobuf)

### 📂 Путь: `grpc_api/`

### 🖥 Установка зависимостей

```bash
cd grpc_api
pip install -r requirements.txt
```

### 🛠 Генерация gRPC-кода из `.proto`

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. temperature.proto
```

### ▶ Запуск gRPC-сервера

```bash
python server.py
```

### 💬 Запуск gRPC-клиента

В другом терминале:

```bash
python client.py
```

---

## ⚖️ Сравнение подходов

| Характеристика        | REST (FastAPI)                     | gRPC                                 |
|-----------------------|------------------------------------|--------------------------------------|
| Протокол              | HTTP/1.1                           | HTTP/2                               |
| Формат данных         | JSON                               | Protocol Buffers (бинарный)          |
| Читаемость            | Высокая                            | Низкая (нужна десериализация)       |
| Скорость              | Умеренная                          | Очень высокая                        |
| Стриминг              | Ограничен (WebSockets)             | Поддерживается из коробки            |
| Поддержка браузеров   | Отличная                           | Ограничена (нужен gRPC-Web)         |
| Простота использования| Очень прост                        | Требует подготовки `.proto` и сборки |

---

