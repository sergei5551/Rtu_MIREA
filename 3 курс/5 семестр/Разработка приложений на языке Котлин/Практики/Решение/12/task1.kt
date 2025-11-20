class UserProfile (
    val name: String?,
    val age: Int?,
    val robbits: String?,
    val favoriteColor: String?,
    val favoriteMovie: String?
){
    fun printProfileInfo(){
        println(
        """
        Информация о пользователе:
        Имя: ${name ?: "не указано"},
        Возраст: ${age ?: "не указано"},
        Хобби: ${robbits ?: "не указано"},
        Любимый цвет: ${favoriteColor ?: "не указано"},
        Фильм: ${favoriteMovie ?: "не указано"}
        """.trimIndent())
    }
}
fun main(args: Array<String>) {
    val user = UserProfile(
        name = "Sergei",
        age = null,
        robbits = null,
        favoriteColor = null,
        favoriteMovie = null
    )
    user.printProfileInfo()
}