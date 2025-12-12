package banking
class BankAccount(val accountNumber: String, initialBalance: Double, ownerName: String) {
    init {
        require(initialBalance >= 0) { "Начальный баланс не может быть отрицательным" }
    }
    constructor(accountNumber: String, ownerName: String) : this(accountNumber, 0.0, ownerName)
    private var _balance: Double = 0.0
        set(value) {
            field = value
            logTransaction()
        }
    val balance: Double
        get() = kotlin.math.round(_balance * 100) / 100
    private var _ownerName: String = ""
        set(value) {
            require(value.length >= 2) { "Имя должно содержать минимум 2 символа" }
            field = value
        }
    private var transactionCount: Int = 0
    init {
        _balance = initialBalance
        this._ownerName = ownerName
    }
    fun deposit(amount: Double) {
        require(amount > 0) { "Сумма пополнения должна быть положительной" }
        _balance += amount
    }

    fun withdraw(amount: Double): Boolean {
        if (amount > 0 && _balance >= amount) {
            _balance -= amount
            return true
        }
        return false
    }
    private fun logTransaction() {
        transactionCount++
    }
    fun getInfo(): String {
        return "Счет: $accountNumber, Владелец: $_ownerName, Баланс: $balance, Операций: $transactionCount"
    }
}

fun main() {
    val account = BankAccount("123456789", 1000.0, "Иван Иванов")
    account.deposit(500.0)
    account.withdraw(200.0)
    println(account.getInfo())
}
