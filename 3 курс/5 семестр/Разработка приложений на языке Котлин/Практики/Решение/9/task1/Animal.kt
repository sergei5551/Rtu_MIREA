abstract class Animal {
    abstract var hunger: Double
    abstract var energy: Double
    abstract var happiness: Double
    abstract val name: String

    fun eat() {
        hunger += 20
        println("Хрум-хрум")
    }

    fun sleep() {
        energy += 100
        println("zzzzz")
    }

    fun play() {
        happiness += 50
        println(" \" Звуки игры \" ")
    }

    fun status() {
        println(
            """
      Сытость: $hunger
      Энергия: $energy
      Счастье: $happiness
      """,
        )
    }

    abstract fun wayOfBirth()
}
