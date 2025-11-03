import Animal

abstract class Mammal : Animal() {
    override fun wayOfBirth() {
        println("Живородящие")
    }
}
