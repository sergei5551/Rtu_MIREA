package task
class Student {
    private var _firstName: String = ""
    private var _lastName: String = ""
    private var scores: IntArray = IntArray(10) { 0 }

    var firstName: String
        get() = _firstName.replaceFirstChar { it.uppercase() }
        set(value) {
            _firstName = value.trim()
        }

    var lastName: String
        get() = _lastName.replaceFirstChar { it.uppercase() }
        set(value) {
            _lastName = value.trim()
        }

    fun getScores(): IntArray = scores.copyOf()

    fun addScore(newScore: Int) {
        for (i in 0 until scores.size - 1) {
            scores[i] = scores[i + 1]
        }
        scores[scores.size - 1] = newScore
    }

    fun getAverageScore(): Double {
        return if (scores.isNotEmpty()) scores.average() else 0.0
    }
}
