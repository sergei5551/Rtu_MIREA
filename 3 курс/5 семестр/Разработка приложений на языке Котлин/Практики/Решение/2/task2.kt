fun task2(array: Array<Int>) {
    var count = 1
    for (i in 0 until array.size - 1) {
        if (array[i + 1] == array[i]) {
            count++
        } else {
            println("$count - ${array[i]}")
            count = 1
        }
    }
    println("$count - ${array[array.size - 1]}")
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
    task2(a)
}
