import java.util.ArrayList;
import java.util.List;

public class Duplicates {

    public static <T extends Comparable<T>> List<T> removeDuplicates(List<T> inputList) {
        if (inputList == null || inputList.isEmpty()) {
            return new ArrayList<>();
        }

        List<T> resultList = new ArrayList<>();

        for (T item : inputList) {
            if (!resultList.contains(item)) {
                resultList.add(item);
            }
        }

        return resultList;
    }
    public static <T extends Comparable<T>> int findIndex(List<T> inputList, T elem){
        int cnt = 0;
        for(T elements : inputList) {
            if (elements == elem) {
                return cnt;
            }
            cnt++;
        }
        return -1;
    }

}