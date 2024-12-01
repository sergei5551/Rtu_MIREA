package Delivery;


public class GroceryDelivery extends DeliverService {
    @Override
    public Product createOrder(){
        return new ProductsGrocery();
    }
}

