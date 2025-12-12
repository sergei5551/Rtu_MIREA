class UniqueString(private var chars: CharArray) {
    constructor(str: String) : this(str.toCharArray())
    fun getChar(index: Int): Char {
        require(index in chars.indices) { "Индекс вне диапазона" }
        return chars[index]
    }
    fun length() = chars.size
    fun print() {
        println(String(chars))
    }
    fun contains(substring: CharArray): Boolean {
        return String(chars).contains(String(substring))
    }
    fun contains(substring: String): Boolean {
        return String(chars).contains(substring)
    }
    fun trimStart() {
        var startIndex = 0
        while (startIndex < chars.size && chars[startIndex].isWhitespace()) {
            startIndex++
        }
        chars = chars.copyOfRange(startIndex, chars.size)
    }
    fun reverse() {
        var left = 0
        var right = chars.size - 1
        while (left < right) {
            val temp = chars[left]
            chars[left] = chars[right]
            chars[right] = temp
            left++
            right--
        }
    }
}

fun main() {
    val str = UniqueString("  Hello World")
    println("Длина: ${str.length()}")
    str.trimStart()
    str.print()
    println("Содержит 'World': ${str.contains("World")}")
    str.reverse()
    println("Развернутая строка:")
    str.print()
}
