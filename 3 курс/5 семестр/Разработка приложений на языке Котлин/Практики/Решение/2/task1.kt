fun aritmetic_mean(array: Array<Int>): Float {
    var sum: Int = 0
    for (i in 0 until array.size) {
        sum += array[i]
    }
    return (sum.toFloat() / array.size)
}

fun main() {
    print("Колличество элементов n: ")
    val n: Int = readln().toInt()
    val a = Array<Int>(n) { 0 }

    for (i in 0 until a.size) {
        print("Ввод a[${i + 1}]: ")
        var a_elem = readln().toInt()
        a[i] = a_elem
    }

    println("Среднее арифметическое: " + aritmetic_mean(a))
}
