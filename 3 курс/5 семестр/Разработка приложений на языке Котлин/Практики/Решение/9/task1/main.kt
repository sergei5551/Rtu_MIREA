import Animal
import Bat
import Dolphin
import Eagle
import GoldFish

fun animalMenu() {
    val animals: List<Animal> =
        listOf(
            Bat(),
            Dolphin(),
            GoldFish(),
            Eagle(),
        )

    while (true) {
        println("\n=== Меню управления животными ===")
        println("1. Показать всех животных")
        println("2. Взаимодействовать с животным")
        println("3. Выход")
        print("Выберите опцию: ")
        when (readLine()) {
            "1" -> {
                println("\nСписок животных:")
                animals.forEachIndexed { index, animal ->
                    println("${index + 1}. ${animal.name}")
                }
            }
            "2" -> {
                print("Введите номер животного: ")
                val input = readLine()?.toIntOrNull()
                if (input != null && input - 1 in animals.indices) {
                    animalActions(animals[input - 1])
                } else {
                    println("Неверный номер!")
                }
            }
            "3" -> return
            else -> println("Неверная опция!")
        }
    }
}

fun animalActions(animal: Animal) {
    while (true) {
        println("\n=== Взаимодействие с ${animal.name} ===")
        println("1. Покормить")
        println("2. Уложить спать")
        println("3. Играть")
        println("4. Состояние")
        println("5. Назад")
        print("Выберите действие: ")

        when (readLine()) {
            "1" -> animal.eat()
            "2" -> animal.sleep()
            "3" -> animal.play()
            "4" -> animal.status()
            "5" -> return
            else -> println("Неверное действие!")
        }
    }
}

fun main() {
    animalMenu()
}
