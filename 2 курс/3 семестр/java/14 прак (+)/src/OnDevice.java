public class OnDevice implements Command{
    private RemoteControl r;

    OnDevice(RemoteControl r){
        this.r = r;
    }
    public void execute(){
        r.TurnOnCommand();
    };
}

