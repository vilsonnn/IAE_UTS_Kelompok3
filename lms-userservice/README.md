# 📘 UserService

Service untuk menyediakan data user (mahasiswa, dosen) dan mengambil informasi course yang diajar user.

## 📌 Base URL
http://localhost:5001


## 🔗 Endpoint

### `GET /users/<user_id>`

- Mengambil data user berdasarkan ID.

**Contoh Response:**

```json
{
  "id": 1,
  "name": "Mahasiswa 1",
  "role": "student"
}

GET /users/<user_id>/courses
Mengambil semua course yang diajar oleh user dengan role "teacher". Mengambil data dari CourseService.

Contoh Responses:
{
  "user_id": 1,
  "courses": [
    {
      "id": 101,
      "title": "Pemrograman Web",
      "teacher_id": 1
    }
  ]
}

⚙️ Teknologi
Python 3

Flask

HTTP communication with requests


🧠 Peran
✅ Provider data user.

✅ Consumer data course dari CourseService.


