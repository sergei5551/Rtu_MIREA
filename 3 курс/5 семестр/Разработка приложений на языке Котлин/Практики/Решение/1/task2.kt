fun foo(n: Int): Unit {
    var nom8 = n / 8
    var nom4 = n % 8 / 4
    var nom2 = n % 4 / 2
    var nom1 = n % 2 / 1

    println("$n рублей| 8: $nom8, 4: $nom4, 2: $nom2, 1: $nom1")
}

fun main() {
    foo(5)
}
