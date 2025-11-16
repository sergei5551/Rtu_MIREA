class ValueValidator<T : Any> {
    
    fun validate(value: T): Boolean {
        return when (value) {
            is Int -> value > 0
            is Double -> value > 0
            is String -> value.length > 5
            else -> false
        }.also { isValid ->
            val message = when (value) {
                is Int, is Double -> 
                    if (isValid) "Число $value валидно (больше 0)"
                    else "Число $value невалидно (должно быть больше 0)"
                is String -> 
                    if (isValid) "Строка '$value' валидна (длина ${value.length} > 5)"
                    else "Строка '$value' невалидна (длина ${value.length} <= 5)"
                else -> "Неподдерживаемый тип: ${value::class.simpleName}"
            }
            println(message)
        }
    }
}


fun main() {
    val validator = ValueValidator<Any>()
    
    validator.validate(10)
    validator.validate(-5)
    validator.validate(3.14)
    validator.validate(0.0)
    
    validator.validate("Hello World")
    validator.validate("Hi")
    validator.validate("Kotlin")
    
    validator.validate(true)
    validator.validate(listOf(1, 2, 3))
}