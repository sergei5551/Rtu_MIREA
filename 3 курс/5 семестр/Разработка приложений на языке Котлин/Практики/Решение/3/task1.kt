import kotlin.random.Random

fun game() {
    val M: Int = Random.nextInt(0, 1001)
    println("Загаданное число: " + M)
    var choice_num = 0
    while (M != choice_num && choice_num >= 0) {
        print("Ввод: ")
        choice_num = readln().toInt()
        when (choice_num) {
            in 0 until M -> println("Это число меньше загаданного.")
            M -> {
                println("Победа!")
                return
            }
            else -> println("Это число больше загаданного.")
        }
    }
}

fun main() {
    game()
}
