fun main() {

    val listA = listOf(101, 205, 303, 404, 505, 303, 101) // ID купленных товаров
    val listB = listOf(303, 404, 505, 606, 707, 808) // ID товаров на складе

    val setA = listA.toSet()
    val setB = listB.toSet()
    println("Список A: ${listA}\n" + "Список B: ${listB}\n")
    // 1. пересечение
    val boughtAndInStock = setA.intersect(setB).sorted()
    println("1. Пересечение: ${boughtAndInStock}")

    // 2. разность
    val boughtButNotInStock = setA.subtract(setB).sorted()
    println("2. Разность: ${boughtButNotInStock}")

    // 3. объединение
    val allUniqueIds = setA.union(setB).sorted()
    println("3. Объединение: $allUniqueIds")
}
