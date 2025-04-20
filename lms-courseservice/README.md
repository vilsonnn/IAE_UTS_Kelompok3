
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

'GET http://localhost:5002/courses/101'


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
