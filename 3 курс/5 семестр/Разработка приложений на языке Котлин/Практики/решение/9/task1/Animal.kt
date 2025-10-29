abstract class Animal {
    var hanger: Double = 0
    var energy: Double = 0
    var happiness: Double = 0

    fun eat() {
        hanger += 20
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
    get() = field
    set(value){
      field = value
    }
    abstract fun wayOfBirth()
}
