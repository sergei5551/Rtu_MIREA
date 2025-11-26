data class Order(
    val orderId: Int,
    val customerId: Int,
    val products: List<String>,
    val totalPrice: Double
)

class OrderAnalyzer {
    private val orders = mutableListOf<Order>()
    
    // 1. Добавление нового заказа в коллекцию
    fun addOrder(order: Order) {
        orders.add(order)
        println("Заказ ${order.orderId} добавлен успешно")
    }
    
    // 2. Удаление заказов, сумма которых меньше заданного значения
    fun removeOrdersBelowPrice(minPrice: Double): List<Order> {
        val removedOrders = orders.filter { it.totalPrice < minPrice }
        orders.removeAll { it.totalPrice < minPrice }
        println("Удалено заказов: ${removedOrders.size}")
        return removedOrders
    }
    
    // 3. Получение списка всех уникальных клиентов
    fun getUniqueCustomers(): Set<Int> {
        return orders.map { it.customerId }.toSet()
    }
    
    // 4. Подсчет общего дохода магазина
    fun getTotalRevenue(): Double {
        return orders.sumOf { it.totalPrice }
    }
    
    // 5. Получение топ-3 самых дорогих заказов
    fun getTop3MostExpensiveOrders(): List<Order> {
        return orders.sortedByDescending { it.totalPrice }.take(3)
    }
    
    fun displayAllOrders() {
        if (orders.isEmpty()) {
            println("Заказов нет")
        } else {
            orders.forEach { order ->
                println("Заказ #${order.orderId}, Клиент: ${order.customerId}, " +
                       "Товары: ${order.products}, Сумма: ${order.totalPrice} руб.")
            }
        }
    }
}

fun main() {
    val analyzer = OrderAnalyzer()
    
    val testOrders = listOf(
        Order(1, 101, listOf("Ноутбук", "Мышь"), 85000.0),
        Order(2, 102, listOf("Смартфон"), 45000.0),
        Order(3, 101, listOf("Наушники", "Чехол"), 15000.0),
        Order(4, 103, listOf("Планшет", "Клавиатура"), 65000.0),
        Order(5, 104, listOf("Монитор"), 30000.0)
    )
    
    testOrders.forEach { analyzer.addOrder(it) }
    
    analyzer.displayAllOrders()
    
    // 1. Добавляем новый заказ
    println("\n1. Добавляем новый заказ:")
    analyzer.addOrder(Order(6, 105, listOf("Принтер", "Бумага"), 25000.0))
    
    // 2. Удаляем заказы с суммой меньше 40000
    println("\n2. Удаляем заказы дешевле 40000:")
    val removedOrders = analyzer.removeOrdersBelowPrice(40000.0)
    println("Удаленные заказы: ${removedOrders.map { it.orderId }}")
    

    
}