import java.util.ArrayList;
import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {

        System.out.println(decimalToBinary(197));
        // Returns 11000101 as an array = [1, 1, 0, 0, 0, 1, 0, 1]
    }

    public static ArrayList<Integer> decimalToBinary(double num) {
        ArrayList<Integer> binaryList = new ArrayList<Integer>();

        do {
            if (Math.floor(num / 2) != num / 2) 
            {
                num = Math.floor(num / 2);
                binaryList.add(1);
            }
            else {
                num = Math.floor(num / 2);
                binaryList.add(0);
            }
        }
        while (num > 0); {
        }
        Collections.reverse(binaryList);
        return binaryList;
    }

}
