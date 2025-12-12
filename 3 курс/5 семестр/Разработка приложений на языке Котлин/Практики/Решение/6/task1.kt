class TimeMeasure
public constructor(private var hours: Int, private var minutes: Int, private var seconds: Int) {
    init {
        require(hours in 0..23) { "Часы должны быть от 0 до 23" }
        require(minutes in 0..59) { "Минуты должны быть от 0 до 59" }
        require(seconds in 0..59) { "Секунды должны быть от 0 до 59" }
    }
    constructor(hours: Int, minutes: Int) : this(hours, minutes, 0)
    constructor(hours: Int) : this(hours, 0, 0)
    fun print24Format() {
        println(String.format("%02d:%02d:%02d", hours, minutes, seconds))
    }
    fun print12Format() {
        val period = if (hours < 12) "AM" else "PM"
        val displayHours = if (hours == 0) 12 else if (hours > 12) hours - 12 else hours
        println(String.format("%02d:%02d:%02d %s", displayHours, minutes, seconds, period))
    }
    fun addTime(addHours: Int, addMinutes: Int = 0, addSeconds: Int = 0) {
        require(addHours >= 0 && addMinutes >= 0 && addSeconds >= 0) {
            "Время не может быть отрицательным"
        }
        seconds += addSeconds
        minutes += addMinutes + seconds / 60
        seconds %= 60
        hours += addHours + minutes / 60
        minutes %= 60
        hours %= 24
    }
}

fun main() {
    val time1 = TimeMeasure(14, 30, 45)
    time1.print24Format()
    time1.print12Format()

    time1.addTime(2, 15, 20)
    println("После добавления времени:")
    time1.print24Format()
}
