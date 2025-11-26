// SalesAnalysis.kt - Полностью независимое приложение для анализа продаж

import java.time.LocalDate

data class Sale(
    val date: LocalDate,
    val product: String,
    val quantity: Int,
    val pricePerUnit: Double
) {
    val totalPrice: Double
        get() = quantity * pricePerUnit
}

class SalesAnalyzer(private val sales: List<Sale>) {
    
    // 1. Подсчет общей выручки за все время
    fun getTotalRevenue(): Double {
        return sales.sumOf { it.totalPrice }
    }
    
    // 2. Группировка продаж по продуктам и подсчет количества проданных единиц
    fun getProductsSalesSummary(): Map<String, Int> {
        return sales.groupBy { it.product }
            .mapValues { (_, productSales) -> productSales.sumOf { it.quantity } }
    }
    
    // 3. Получение списка продаж за конкретный месяц
    fun getSalesByMonth(month: Int, year: Int): List<Sale> {
        return sales.filter { 
            it.date.monthValue == month && it.date.year == year 
        }
    }
    
    // 4. Определение продукта, который принес наибольшую выручку
    fun getTopProductByRevenue(): Pair<String, Double>? {
        return sales.groupBy { it.product }
            .mapValues { (_, productSales) -> productSales.sumOf { it.totalPrice } }
            .maxByOrNull { it.value }
            ?.let { it.key to it.value }
    }
    
    fun displayAllSales() {
        sales.forEach { sale ->
            println("${sale.date}: ${sale.product} x${sale.quantity} " +
                   "по ${sale.pricePerUnit} руб. = ${sale.totalPrice} руб.")
        }
    }
}

fun main() {

    val testSales = listOf(
        Sale(LocalDate.of(2024, 1, 15), "Ноутбук", 2, 50000.0),
        Sale(LocalDate.of(2024, 1, 20), "Смартфон", 3, 30000.0),
        Sale(LocalDate.of(2024, 2, 5), "Ноутбук", 1, 55000.0),
        Sale(LocalDate.of(2024, 2, 10), "Наушники", 5, 8000.0),
        Sale(LocalDate.of(2024, 2, 25), "Смартфон", 2, 32000.0),
        Sale(LocalDate.of(2024, 3, 1), "Планшет", 2, 25000.0),
        Sale(LocalDate.of(2024, 3, 15), "Наушники", 3, 7500.0),
        Sale(LocalDate.of(2024, 3, 20), "Монитор", 1, 35000.0)
    )
    
    val analyzer = SalesAnalyzer(testSales)
    
    // Выводим все продажи
    analyzer.displayAllSales()
    
    // 1. Общая выручка
    println("\n1. Общая выручка за все время:")
    val totalRevenue = analyzer.getTotalRevenue()
    println("${"%.2f".format(totalRevenue)} руб.")
    
    // 2. Группировка по продуктам
    println("\n2. Продажи по продуктам (количество):")
    val productsSummary = analyzer.getProductsSalesSummary()
    productsSummary.forEach { (product, quantity) ->
        println("$product: $quantity шт.")
    }
    
    // 3. Продажи за февраль 2024
    println("\n3. Продажи за февраль 2024:")
    val februarySales = analyzer.getSalesByMonth(2, 2024)
    if (februarySales.isEmpty()) {
        println("Продаж в этом месяце нет")
    } else {
        februarySales.forEach { sale ->
            println("${sale.date}: ${sale.product} x${sale.quantity} - ${sale.totalPrice} руб.")
        }
    }
    
    // 4. Продукт с наибольшей выручкой
    println("\n4. Продукт с наибольшей выручкой:")
    val topProduct = analyzer.getTopProductByRevenue()
    if (topProduct != null) {
        println("${topProduct.first}: ${"%.2f".format(topProduct.second)} руб.")
    } else {
        println("Нет данных о продажах")
    }
    
}