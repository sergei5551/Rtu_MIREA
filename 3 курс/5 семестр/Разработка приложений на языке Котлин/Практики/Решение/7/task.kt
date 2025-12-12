import java.util.UUID

abstract class MenuItem {
    abstract val name: String
    abstract val basePrice: Double

    abstract fun calculateFinalPrice(): Double

    final val id: String = UUID.randomUUID().toString()
}

data class Ingredient(val name: String, val isAllergen: Boolean)

enum class Size {
    SMALL,
    MEDIUM,
    LARGE
}

class Drink(override val name: String, override val basePrice: Double, val size: Size) :
        MenuItem() {

    final override fun calculateFinalPrice(): Double {
        return when (size) {
            Size.SMALL -> basePrice * 1.0
            Size.MEDIUM -> basePrice * 1.5
            Size.LARGE -> basePrice * 2.0
        }
    }
}

class Food(
        override val name: String,
        override val basePrice: Double,
        val ingredients: List<Ingredient>
) : MenuItem() {

    val isVegetarian: Boolean
        get() = ingredients.none { it.isAllergen }

    override fun calculateFinalPrice(): Double {
        return basePrice
    }
}

fun main() {
    val drink = Drink("Кофе", 100.0, Size.LARGE)
    println("${drink.name}: ${drink.calculateFinalPrice()}")

    val food =
            Food("Салат", 200.0, listOf(Ingredient("Помидоры", false), Ingredient("Огурцы", false)))
    println("${food.name}: ${food.calculateFinalPrice()}, Вегетарианский: ${food.isVegetarian}")
}
