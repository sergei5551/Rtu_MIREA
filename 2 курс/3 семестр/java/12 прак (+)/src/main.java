import Delivery.*;

public class main {
    public static void main(String[] args){
        DeliverService d1_pizza = new PizzaDelivery();
        Product productA = d1_pizza.createOrder();
        productA.products();

        DeliverService d2_grocery = new GroceryDelivery();
        Product productB = d2_grocery.createOrder();
        productB.products();
    }
}
