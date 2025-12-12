import kotlin.random.Random

fun generatePlayers(count: Int): Sequence<Player> = sequence {
    val nicknames =
            listOf(
                            "ShadowHunter",
                            "IronWarrior",
                            "MagicMage",
                            "SwiftRogue",
                            "MightyTank",
                            "SniperWolf",
                            "FireDragon",
                            "IceQueen",
                            "StormRider",
                            "DarkKnight",
                            "LightBringer",
                            "CyberNinja",
                            "SpacePirate",
                            "TimeTraveler",
                            "NeoMatrix"
                    )
                    .shuffled()

    val achievementsList =
            listOf(
                    listOf("Новичок", "Победитель арены"),
                    listOf("Новичок", "Собиратель"),
                    listOf("Новичок", "Исследователь", "Мастер подземелий"),
                    listOf("Новичок", "Победитель арены", "Богач"),
                    listOf("Новичок", "Исследователь", "Легенда"),
                    listOf("Новичок", "Победитель босса"),
                    listOf("Новичок", "Собиратель", "Мастер крафта"),
                    listOf("Новичок", "Победитель арены", "Непобедимый"),
                    listOf("Новичок", "Исследователь", "Покоритель вершин"),
                    listOf("Новичок", "Легенда", "Ветеран"),
                    listOf("Новичок", "Богач", "Торговец"),
                    listOf("Новичок", "Победитель арены", "Дуэлянт"),
                    listOf("Новичок", "Собиратель", "Коллекционер"),
                    listOf("Новичок", "Легенда", "Мифический герой"),
                    listOf("Новичок", "Исследователь", "Первооткрыватель")
            )

    repeat(count) { index ->
        yield(
                Player(
                        nickname = nicknames[index % nicknames.size],
                        level = Random.nextInt(1, 30),
                        score = Random.nextInt(100, 10000),
                        achievements = achievementsList[index % achievementsList.size],
                        playTimeHours = Random.nextInt(10, 500)
                )
        )
    }
}

data class Player(
        val nickname: String,
        val level: Int,
        val score: Int,
        val achievements: List<String>,
        val playTimeHours: Int
)

fun main() {
    // 1. Создание последовательности из 12 игроков
    val playersSequence = generatePlayers(12)

    println("=== 1. Исходный список игроков ===")
    playersSequence.toList().forEach { println(it) }
    val players = generatePlayers(12)

    // 2. Фильтрация по уровню – выбрать игроков уровня > 10
    println("\n=== 2. Игроки с уровнем > 10 ===")
    val highLevelPlayers = players.filter { it.level > 10 }.toList()
    highLevelPlayers.forEach { println("${it.nickname} - уровень: ${it.level}") }

    // 3. Проверка наличия достижения «Легенда»
    println("\n=== 3. Проверка достижения 'Легенда' ===")
    val hasLegendAchievement = players.any { it.achievements.contains("Легенда") }
    println("Есть ли игрок с достижением 'Легенда': $hasLegendAchievement")

    if (hasLegendAchievement) {
        val legendPlayers = players.filter { it.achievements.contains("Легенда") }.toList()
        println("Игроки с достижением 'Легенда':")
        legendPlayers.forEach { println(it.nickname) }
    }

    // 4. Трансформация в статистику
    println("\n=== 4. Статистика игроков ===")
    val playerStats =
            players
                    .map { "Игрок: ${it.nickname}, Уровень: ${it.level}, Очки: ${it.score}" }
                    .toList()
    playerStats.forEach { println(it) }

    // 5. Группировка игроков по диапазонам времени
    println("\n=== 5. Группировка по времени игры ===")
    val groupedByPlayTime =
            players
                    .groupBy { player ->
                        when (player.playTimeHours) {
                            in 0..49 -> "Менее 50 часов"
                            in 50..200 -> "50-200 часов"
                            else -> "Более 200 часов"
                        }
                    }
                    .mapValues { (_, playersInGroup) -> playersInGroup.toList() }

    groupedByPlayTime.forEach { (groupName, playersInGroup) ->
        println("\n$groupName (${playersInGroup.size} игроков):")
        playersInGroup.forEach { println("  ${it.nickname} - ${it.playTimeHours} ч") }
    }

    // 6. Сортировка игроков по убыванию очков
    println("\n=== 6. Игроки, отсортированные по очкам (по убыванию) ===")
    val sortedByScore = players.sortedByDescending { it.score }.toList()
    sortedByScore.forEachIndexed { index, player ->
        println("${index + 1}. ${player.nickname} - ${player.score} очков")
    }

    // 7. Расчет среднего уровня игроков в каждой группе времени
    println("\n=== 7. Средний уровень по группам времени ===")
    groupedByPlayTime.forEach { (groupName, playersInGroup) ->
        val averageLevel = playersInGroup.map { it.level }.average()
        println("$groupName: средний уровень = ${"%.2f".format(averageLevel)}")
    }

    println("\n=== Дополнительная статистика ===")
    val statsSequence = generatePlayers(12)
    val totalPlayers = statsSequence.count()
    println("Всего игроков: $totalPlayers")
    val stats = generatePlayers(12).toList()
    println("Средний уровень всех игроков: ${"%.2f".format(stats.map { it.level }.average())}")
    println("Средние очки: ${"%.2f".format(stats.map { it.score }.average())}")
    println("Среднее время игры: ${"%.2f".format(stats.map { it.playTimeHours }.average())} часов")
}
