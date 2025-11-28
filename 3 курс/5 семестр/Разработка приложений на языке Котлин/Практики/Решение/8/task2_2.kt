open class Animal {
  open fun speak() = "Some sound" // Нужно указать что метод будет наследуемым(open// Нужны val)
}
class Cat : Animal() {
 override fun speak() = "Meow!"
}
// Нужны val
data class User(val name: String,val age: Int) 


fun main() {
 val cat = Cat()
 println(cat.speak())
}
