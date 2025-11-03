import Mammal

class Dolphin :
    Mammal(),
    Swimming {
    override var hunger: Double = 0.0
    override var energy: Double = 100.0
    override var happiness: Double = 70.0 // дельфины обычно счастливые
    override val name: String = "Дельфин"

    override fun swim() {
        println("$name грациозно плавает")
        energy -= 10
        happiness += 5 // плавание радует дельфина
    }
}
