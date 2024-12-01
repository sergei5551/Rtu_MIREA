public class IllegalTriangleException extends Exception {
    private final String massage;

    public IllegalTriangleException(String massage) {
        this.massage = massage;
    }

    public String getMassage() {
        return massage;
    }
}
