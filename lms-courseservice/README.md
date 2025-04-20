
---

## 📁 `lms-courseservice/README.md`

```markdown

# 📗 CourseService

Service ini menyediakan data mata kuliah dalam sistem LMS. Service ini juga mengambil data dosen pengampu dari `UserService` untuk melengkapi informasi course.

---

## 📌 Base URL

`http://localhost:5002`

---

## 🔗 Endpoint

### `GET /courses/<course_id>`

- Mengambil detail course berdasarkan ID.
- Mengambil data dosen (`teacher_id`) dari `UserService`.

**Contoh Request:**

```
GET http://localhost:5002/courses/101
```

**Contoh Response:**

```json
{
  "course": {
    "id": 101,
    "title": "Pemrograman Web",
    "teacher_id": 1
  },
  "teacher": {
    "id": 1,
    "name": "Mahasiswa 1",
    "role": "student"
  }
}
```

---

### `GET /courses/teacher/<teacher_id>`

- Menyediakan daftar semua course yang diajar oleh dosen tertentu.
- Endpoint ini digunakan oleh `UserService`.

**Contoh Request:**

```
GET http://localhost:5002/courses/teacher/1
```

**Contoh Response:**

```json
[
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
```

---

## 🧠 Peran

- ✅ **Provider** data course.
- ✅ **Consumer** data user dari `UserService`.

---

## ⚙️ Teknologi

- Python 3
- Flask
- JSON (REST API)
- Service-to-Service Communication menggunakan `requests` module
