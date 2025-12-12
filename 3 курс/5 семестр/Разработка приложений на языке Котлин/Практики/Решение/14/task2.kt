// Создадим data class для типа записи
data class MemeEntry(
        val text: String,
        val author: String,
        val type: String, // "quote", "poem", "meme"
        val tags: List<String>
)

fun main() {
    val entries =
            listOf(
                    MemeEntry(
                            text = "Быть или не быть, вот в чём вопрос.",
                            author = "Шекспир",
                            type = "quote",
                            tags = listOf("философия", "жизнь", "решение")
                    ),
                    MemeEntry(
                            text = "Я помню чудное мгновенье: Передо мной явилась ты...",
                            author = "А.С. Пушкин",
                            type = "poem",
                            tags = listOf("любовь", "воспоминания", "красота")
                    ),
                    MemeEntry(
                            text = "Это фиаско, братан.",
                            author = "Internet Meme",
                            type = "meme",
                            tags = listOf("юмор", "неудача", "интернет")
                    ),
                    MemeEntry(
                            text = "Зимнее утро. Мороз и солнце; день чудесный!",
                            author = "А.С. Пушкин",
                            type = "poem",
                            tags = listOf("природа", "утро", "зима", "радость")
                    ),
                    MemeEntry(
                            text =
                                    "Когда жизнь дает тебе лимоны, не делай лимонад. Заставь жизнь забрать их обратно!",
                            author = "Internet Meme",
                            type = "meme",
                            tags = listOf("юмор", "мотивация", "протест")
                    )
            )

    // 1. Вывести все цитаты (quotes)
    println("1. Все цитаты (type='quote'):")
    entries.filter { it.type == "quote" }.forEach {
        println("   - \"${it.text}\" (${it.author})")
        println("     Теги: ${it.tags.joinToString()}")
    }

    // 2. Найти все записи от определенного автора
    val authorToFind = "А.С. Пушкин"
    println("\n2. Все записи автора '$authorToFind':")
    entries.filter { it.author == authorToFind }.forEach {
        println("   - \"${it.text}\" [${it.type}]")
        println("     Теги: ${it.tags.joinToString()}")
    }

    // 3. Дополнительные операции:

    // Поиск по тегу
    val tagToFind = "юмор"
    println("\n3. Записи с тегом '$tagToFind':")
    entries.filter { tagToFind in it.tags }.forEach {
        println("   - \"${it.text}\" (${it.author})")
    }

    // Группировка по типу
    println("\n4. Группировка по типу:")
    entries.groupBy { it.type }.forEach { (type, items) ->
        println("   $type (${items.size}):")
        items.forEach { println("     - ${it.text.take(30)}...") }
    }

    // Поиск всех уникальных тегов
    val allTags = entries.flatMap { it.tags }.toSet().sorted()
    println("\n5. Все уникальные теги: ${allTags.joinToString()}")

    // Статистика по авторам
    println("\n6. Количество записей по авторам:")
    entries.groupingBy { it.author }.eachCount().forEach { (author, count) ->
        println("   $author: $count записей")
    }
}
