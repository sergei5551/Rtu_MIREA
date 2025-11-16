package order
class Product (
    val id: Int,
    val name: String,
    val price: Int,
    val categeory: String
)

class Order{
    var items: MutableList<Pair<Product, Int>> = mutableListOf() 
    var totalPrice: Double = 0.0
    var status: String = "PENDING"

    fun addProduct(product: Product, quantity: Int = 1) {
        items.add(product to quantity)
        totalPrice += product.price * quantity
    }
}

fun main() {
    // Создаем несколько продуктов
    val laptop = Product(1, "Laptop", 1000, "Electronics")
    val mouse = Product(2, "Mouse", 50, "Electronics")
    val book = Product(3, "Kotlin Programming", 35, "Books")
    val chair = Product(4, "Office Chair", 200, "Furniture")

    val order = Order().apply {
        addProduct(laptop)
        addProduct(mouse, 2)
        addProduct(book)
        status = "PROCESSING"
        println("Заказ создан и проинициализирован")
    }
    order.also {
        println("\n--- Информация о заказе ---")
        println("Статус: ${it.status}")
        println("Количество товаров: ${it.items.size}")
        println("Общая стоимость: $${it.totalPrice}")
    }

}
