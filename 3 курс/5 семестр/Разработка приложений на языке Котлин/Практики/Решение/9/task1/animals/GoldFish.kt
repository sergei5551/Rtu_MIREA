import Fish

class GoldFish :
    Fish(),
    Flying {
    override var hunger: Double = 0.0
    override var energy: Double = 80.0 // у рыбки меньше энергии
    override var happiness: Double = 60.0
    override val name: String = "Золотая рыбка"

    override fun fly() {
        println("$name пытается летать... но это же рыбка!")
        happiness -= 10 // рыбка расстраивается
        energy -= 5
    }
}
