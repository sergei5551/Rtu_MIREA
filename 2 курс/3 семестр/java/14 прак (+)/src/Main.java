//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //создание объекта ж
        RemoteControl device = new RemoteControl();

        OnDevice funk1 = new OnDevice(device); // Функция включения через отдельный объект
        OffDevice funk2 = new OffDevice(device); // Функция выключения через отдельный объект

        funk1.execute(); // Включение device
        funk2.execute(); // Выключение device

    }
}