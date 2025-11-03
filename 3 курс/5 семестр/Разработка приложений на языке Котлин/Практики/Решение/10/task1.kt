import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.time.format.DateTimeParseException

enum class Gender {
    MALE,
    FEMALE,
}

class FormValidator {
    fun checkName(name: String) {
        if (name.length < 2 || name.length > 20) {
            throw IllegalArgumentException("Длина имени должна быть от 2 до 20 символов.")
        }
        if (!name[0].isUpperCase()) {
            throw IllegalArgumentException("Имя должно начинаться с заглавной буквы.")
        }
    }

    fun checkBirthDate(birthDate: String) {
        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
        val date: LocalDate
        try {
            date = LocalDate.parse(birthDate, formatter)
        } catch (e: DateTimeParseException) {
            throw IllegalArgumentException("Дата должна быть в формате YYYY-MM-DD.")
        }

        val minDate = LocalDate.of(1900, 1, 1)
        val maxDate = LocalDate.now()
        if (date.isBefore(minDate) || date.isAfter(maxDate)) {
            throw IllegalArgumentException("Дата рождения должна быть между 01.01.1900 и сегодняшним днём.")
        }
    }

    fun checkGender(gender: Gender) {
        if (gender != Gender.MALE && gender != Gender.FEMALE) {
            throw IllegalArgumentException("Пол должен быть MALE или FEMALE.")
        }
    }

    fun checkWeight(weight: Double) {
        if (weight <= 0) {
            throw IllegalArgumentException("Вес должен быть положительным числом.")
        }
    }

    fun validateAll(
        name: String,
        birthDate: String,
        gender: Gender,
        weight: Double,
    ) {
        checkName(name)
        checkBirthDate(birthDate)
        checkGender(gender)
        checkWeight(weight)
        println("Все данные корректны! Можно отправлять анкету на сервер.")
    }
}

fun main() {
    try {
        val form = FormValidator()
        form.validateAll(
            name = "Василийasdasdasdasdasdasdadawdad",
            birthDate = "1999-05-12",
            gender = Gender.MALE,
            weight = 75.5,
        )
    } catch (e: IllegalArgumentException) {
        println("Ошибка проверки: ${e.message}")
    }
}
