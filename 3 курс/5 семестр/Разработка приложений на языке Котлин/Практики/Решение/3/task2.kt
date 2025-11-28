fun convert_morze(s: String): String {
    val morze =
            arrayOf(
                    ".-",
                    "-...",
                    ".--",
                    "--.",
                    "-..",
                    ".",
                    "...-",
                    "--..",
                    "..",
                    ".---",
                    "-.-",
                    ".-..",
                    "--",
                    "-.",
                    "---",
                    ".--.",
                    ".-.",
                    "...",
                    "-",
                    "..-",
                    "..-.",
                    "....",
                    "-.-.",
                    "---.",
                    "----",
                    "--.-",
                    "--.--",
                    "-.--",
                    "-..-",
                    "..-..",
                    "..--",
                    ".-.-"
            )
    var summary_line: String = ""
    for (element in s) {
        summary_line += morze[element.code - 1040] + " "
    }
    return summary_line
}

fun main() {
    println(convert_morze("АЗБУКА"))
} 
