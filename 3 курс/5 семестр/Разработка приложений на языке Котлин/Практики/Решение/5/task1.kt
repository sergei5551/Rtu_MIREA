import kotlin.random.Random

class Cat {
    private fun rest() = println("Sleep")
    private fun voice() = println("Meow")
    private fun feed() = println("Eat")

    fun randomAction() {
        when (Random.nextInt(1, 4)) {
            1 -> rest()
            2 -> voice()
            3 -> feed()
        }
    }
}

fun main() {
    val cat = Cat()
    repeat(5) { cat.randomAction() }
}
