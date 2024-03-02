package Other;

public class Order {
    private int id = 0, price = 0, quantity = 0;

    public Order(int id, int price, int quantity) {
        this.id = id;
        this.price = price;
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return Integer.toString(id) + " " + Integer.toString(price) + " " + Integer.toString(quantity);
    }
}
