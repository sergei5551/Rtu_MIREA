
class ErrorLogger<T> {
    private val errorLog = mutableListOf<String>()
    

    fun logError(error: T) {
        val errorMessage = when (error) {
            is String -> "String error: $error"
            is Number -> "Numeric error: $error"
            else -> "Unknown error type"
        }
        errorLog.add(errorMessage)
        println(errorMessage)
    }

}

fun <T> ErrorLogger<T>.logAndSend(error: T) {
    logError(error) 
    println("Попытка отправки ошибки на сервер: $error") 
}


fun main() {

    val stringLogger = ErrorLogger<String>()
    val numberLogger = ErrorLogger<Number>()
    val anyLogger = ErrorLogger<Object>()

    println("\nЛогирование строк")
    stringLogger.logError("Файл не найден")
    stringLogger.logError("Ошибка подключения к базе данных")
    

    println("\nЛогирование чисел")
    numberLogger.logError(404)
    numberLogger.logError(3.14)
    numberLogger.logError(-1)   
    
}