package src2;

abstract public class Machine {
  private String model;

  Machine(String model) {
    this.model = model;
  }

  public void printModel() {
    System.out.println("Модель " + typeMachine(this) + ": " + this.model);
  }

  static public Object typeMachine(Object obj) {
    return obj.getClass().getSimpleName();
  }
}
