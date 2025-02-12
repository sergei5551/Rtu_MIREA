public class OffDevice implements Command{
    private RemoteControl r;
    OffDevice(RemoteControl r){
        this.r = r;
    }
    public void execute(){
        r.TurnOffCommand();
    };
}
