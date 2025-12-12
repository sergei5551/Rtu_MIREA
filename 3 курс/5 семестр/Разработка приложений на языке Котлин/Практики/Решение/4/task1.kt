data class Question(val text: String, val options: List<String>, val correctAnswer: Int)

fun main() {
    val questions =
            listOf(
                    Question(
                            "Столица Франции?",
                            listOf("1. Лондон", "2. Берлин", "3. Париж", "4. Мадрид"),
                            3
                    ),
                    Question(
                            "Сколько планет в Солнечной системе?",
                            listOf("1. 7", "2. 8", "3. 9", "4. 10"),
                            2
                    ),
                    Question(
                            "Автор 'Войны и мира'?",
                            listOf("1. Достоевский", "2. Толстой", "3. Пушкин", "4. Чехов"),
                            2
                    )
            )

    var score = 0

    questions.shuffled().forEach { question ->
        println("\n${question.text}")
        question.options.forEach { println(it) }

        print("Ваш ответ (1-4): ")
        val answer = readLine()?.toIntOrNull()

        if (answer == question.correctAnswer) {
            println("Правильно!")
            score++
        } else {
            println("Неправильно. Правильный ответ: ${question.correctAnswer}")
        }
    }

    println("\nИтоговый счет: $score из ${questions.size}")
}
