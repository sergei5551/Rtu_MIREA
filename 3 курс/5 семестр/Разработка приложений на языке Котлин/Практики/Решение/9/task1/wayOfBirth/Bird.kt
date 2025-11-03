import Animal

abstract class Bird : Animal() {
    override fun wayOfBirth() {
        println("Откладывает яйца")
    }
}
