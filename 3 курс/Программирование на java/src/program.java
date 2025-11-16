import src2.*;

class program {
  public static void main(String[] args) {

    Machine[] objs = new Machine[] {
        new Car("Lada"),
        new Bike("Yamaha"),
        new Bus("Liaz")
    };
    for (var obj : objs) {
      obj.printModel();
    }
  }
}
