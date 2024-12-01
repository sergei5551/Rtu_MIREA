package Delivery;


public class PizzaDelivery extends DeliverService {
    @Override
    public Product createOrder(){
        return new ProductPizza();
    }
}