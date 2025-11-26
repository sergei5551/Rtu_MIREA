fun count_nycl(nycl: String) {
    val map = mutableMapOf<Char, Int>()
    for (i in 0 until nycl.length) {
        var nycl_1 = nycl[i]
        map[nycl_1] = map.getOrDefault(nycl_1, 0) + 1
    }

    println(
            "A: ${map.getOrDefault('A', 0)}, " +
                    "T: ${map.getOrDefault('T', 0)}, " +
                    "G: ${map.getOrDefault('G', 0)}, " +
                    "C: ${map.getOrDefault('C', 0)}"
    )
}

fun main() {
    val nycl_str = "ATGCCTCTCTC"
    println("Строка: $nycl_str")
    count_nycl(nycl_str)
}
