# Equipment Rental API (rent_shop) 🚜💨

Сервис автоматизации проката и учета строительной техники и оборудования, разработанный на Django REST Framework. Поддерживает JWT-авторизацию, автоматический учет статусов доступности техники и предоставляет интерактивную документацию API.

## 🛠 Стек технологий
* **Backend:** Python 3.11+, Django 4.x / 5.x
* **API:** Django REST Framework (DRF)
* **Auth:** SimpleJWT (JSON Web Tokens)
* **Docs:** OpenAPI / Swagger (drf-yasg)

---

## 🚀 Архитектура и Структура моделей (Приложение `AllInOne`)

### 1. Доступность техники (`ActiveStatus`)
Поле статуса реализовано через расширяемый класс `models.TextChoices`. Возможные состояния:
* `available` — Доступна
* `repair` — В ремонте
* `rented` — В аренде

### 2. Основные сущности:
* **Customer** — Профиль клиента, связанный со стандартным пользователем Django.
* **Equipment** — Карточка техники (название, категория, серийный номер, посуточная цена, статус).
* **Rental** — Оформленные договора аренды (даты начала/окончания, итоговая стоимость и статус).

---

## 🛣 Эндпоинты API (Маршруты)

### 🔐 Аутентификация и Регистрация
* `POST /api/register/` — Регистрация нового аккаунта пользователей.
* `POST /api/token/` — Логин (получение пары Access и Refresh токенов).
* `POST /api/token/refresh/` — Обновление протухшего Access-токена.

### 💼 Бизнес-логика (CRUD через ViewSets)
* `GET, POST /api/customer/` — Список и создание клиентов.
* `GET, POST, PUT, DELETE /api/equipment/` — Управление каталогом техники.
* `GET, POST, PUT, DELETE /api/rental/` — Управление договорами проката.

### 📋 Документация API
* `http://127.0.0` — Интерактивная веб-панель Swagger UI (Try it out).
* `http://127.0.0` — Чистая техническая документация ReDoc.

---

## 📦 Быстрый запуск проекта локально

### 1. Клонирование репозитория и настройка
```bash
git clone https://github.com
cd rent_shop
```

### 2. Активация виртуального окружения (VENV)
* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **Mac/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Установка необходимых зависимостей
```bash
pip install django djangorestframework djangorestframework-simplejwt drf-yasg
```

### 4. Применение миграций базы данных
```bash
python manage.py migrate
```

### 5. Создание учетной записи Администратора (для /admin/)
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера разработки
```bash
python manage.py runserver
```
После запуска проект будет доступен по адресу: `http://127.0.0`
