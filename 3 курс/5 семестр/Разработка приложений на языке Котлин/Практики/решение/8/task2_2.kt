open class Animal {
  open fun speak() = "Some sound"
}
class Cat : Animal() {
 override fun speak() = "Meow!"
}

data class User(val name: String,val age: Int) // Нужны val


fun main() {
 val cat = Cat()
 println(cat.speak())
}
