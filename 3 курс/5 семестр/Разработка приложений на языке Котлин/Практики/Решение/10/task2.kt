data class User(
    val name: String,
    val age: Int,
    val friends: List<String>,
)

fun main() {
    val usersData =
        object {
            val users =
                listOf(
                    User("Сергей", 20, listOf("Мария", "Дмитрий")),
                    User("Мария", 18, listOf("Сергей", "Екатерина")),
                    User("Дмитрий", 25, listOf("Сергей")),
                    User("Екатерина", 28, listOf("Мария")),
                )

            fun findOldestUser(): User? = users.maxByOrNull { it.age }

            fun printAllUsers() {
                println("Список пользователей:")
                for (u in users) {
                    println("- ${u.name}, ${u.age} лет, друзья: ${u.friends.joinToString(", ")}")
                }
            }
        }

    usersData.printAllUsers()

    val oldest = usersData.findOldestUser()
    if (oldest != null) {
        println("\nСамый старший пользователь: ${oldest.name}, возраст: ${oldest.age}")
    } else {
        println("\nСписок пользователей пуст!")
    }
}
