fun task3(array: Array<String>): String {
    for (i in 0 until array.size) {
        for (j in i + 1 until array.size) if (array[i].equals(array[j])) return array[i]
    }
    return ""
}

fun main() {
    print("Колличество элементов n: ")
    val n: Int = readln().toInt()
    val a = Array<String>(n) { "" }

    for (i in 0 until a.size) {
        print("Ввод a[${i + 1}]: ")
        var a_elem = readln()
        a[i] = a_elem
    }
    println(task3(a))
}
