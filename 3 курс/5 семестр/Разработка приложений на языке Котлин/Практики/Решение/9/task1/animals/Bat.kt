import Mammal

class Bat :
    Mammal(),
    Flying {
    override var hunger: Double = 0.0
    override var energy: Double = 100.0
    override var happiness: Double = 50.0
    override val name: String = "Летучая мышь"

    override fun fly() {
        println("Быстро летает")
        energy -= 15
    }
}
