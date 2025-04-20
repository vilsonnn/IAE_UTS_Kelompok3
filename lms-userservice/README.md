
---

## 📁 `lms-userservice/README.md`

```markdown


# 📘 UserService

Service ini menyediakan data pengguna (mahasiswa dan dosen) dalam sistem LMS. Selain sebagai penyedia data user, service ini juga bertindak sebagai **consumer** yang mengambil data course dari `CourseService`.

---

## 📌 Base URL

`http://localhost:5001`

---

## 🔗 Endpoint

### `GET /users/<user_id>`

- Mengambil informasi user berdasarkan ID.

**Contoh Request:**

```
GET http://localhost:5001/users/1
```

**Contoh Response:**

```json
{
  "id": 1,
  "name": "Mahasiswa 1",
  "role": "student"
}
```

---

### `GET /users/<user_id>/courses`

- Mengambil daftar mata kuliah yang diajar oleh user (dosen) berdasarkan ID.
- Endpoint ini melakukan request ke `CourseService`.

**Contoh Request:**

```
GET http://localhost:5001/users/1/courses
```

**Contoh Response:**

```json
{
  "user_id": 1,
  "courses": [
    {
      "id": 101,
      "title": "Pemrograman Web",
      "teacher_id": 1
    },
    {
      "id": 102,
      "title": "Struktur Data",
      "teacher_id": 1
    }
  ]
}
```

---

## 🧠 Peran

- ✅ **Provider** data user.
- ✅ **Consumer** data course dari `CourseService`.

---

## ⚙️ Teknologi

- Python 3
- Flask
- JSON (REST API)
- Service-to-Service Communication menggunakan `requests` module
