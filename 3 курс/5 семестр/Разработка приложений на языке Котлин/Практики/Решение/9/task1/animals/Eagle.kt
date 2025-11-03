import Bird

class Eagle :
    Bird(),
    Flying {
    override var hunger: Double = 0.0
    override var energy: Double = 120.0 // у орла больше энергии
    override var happiness: Double = 40.0
    override val name: String = "Орёл"

    override fun fly() {
        println("$name парит высоко в небе")
        energy -= 20 // полет орла требует больше энергии
        hunger += 15
    }
}
