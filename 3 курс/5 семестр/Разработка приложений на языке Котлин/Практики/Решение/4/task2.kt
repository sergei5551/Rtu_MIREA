fun topKFrequent(words: Array<String>, k: Int): List<String> {
    val frequency = mutableMapOf<String, Int>()

    for (word in words) {
        frequency[word] = frequency.getOrDefault(word, 0) + 1
    }

    return frequency
            .entries
            .sortedWith(compareByDescending<Map.Entry<String, Int>> { it.value }.thenBy { it.key })
            .take(k)
            .map { it.key }
}

fun main() {
    val words =
            arrayOf("the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "day")
    val k = 4

    val result = topKFrequent(words, k)
    println(result)
}
