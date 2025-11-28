fun generate_passowrd(n: Int): String {
    if (n < 8) return "Пароль с $n количеством символов небезопасен"

    var password: String = ""
    var char_p =
            arrayOf("zxcvbnmasdfghjklqwertyuiop", "ZXCVBNMASDFGHJKLQWERTYUIOP", "0123456789", "_*-")

    for (i in 0 until n) {
        var category = char_p[i % 4]
        var randomIndex = (0 until category.length).random()
        password += category[randomIndex]
    }
    return password
}

fun main() {
    var n = 0
    while (n < 8) {
        print("Введите длину пароля: ")
        n = readln().toInt()
        println(generate_passowrd(n))
    }
}
