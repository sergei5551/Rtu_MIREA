enum class DrinkType(
  val name_dr: String,
  val v: Int,
  val temp: Int
){
  Coca_Cola("Газировка", 500, 38),
  Tea("Чай", 250, 65),
  Coffe("Кофе", 350, 70),
  ColdTea("Чай", 300, 0);

  fun nameDrink() = this.name_dr.replaceFirstChar {it.uppercase()}
  fun get_v(): Int = this.v
  fun isHot(): Boolean = temp > 60
}



fun main(){
  for (dr in DrinkType.entries){
    println("Название: ${dr.nameDrink()}")
    println("Объем: ${dr.get_v()}")
    if (dr.isHot())
      println("Напиток горячий, ${dr.temp}C")
    else
      println("Напиток не горячий, ${dr.temp}C")
    println() 
  }
}
