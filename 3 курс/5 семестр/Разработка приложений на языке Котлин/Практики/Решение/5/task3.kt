import task.Student

class StudentService {
    fun findBestStudent(students: Array<Student>): Student? {
        return students.maxByOrNull { it.getAverageScore() }
    }

    fun sortStudentsByLastName(students: Array<Student>): Array<Student> {
        return students.sortedBy { it.lastName }.toTypedArray()
    }
}

fun main() {
    val students =
            arrayOf(
                    Student().apply {
                        lastName = "Иванов"
                        firstName = "Алексей"
                    },
                    Student().apply {
                        lastName = "Петров"
                        firstName = "Дмитрий"
                    },
                    Student().apply {
                        lastName = "Сидоров"
                        firstName = "Сергей"
                    }
            )

    val service = StudentService()
    val sorted = service.sortStudentsByLastName(students)

    println("Отсортировано по фамилии:")
    sorted.forEach { println("${it.lastName} ${it.firstName}") }
}
