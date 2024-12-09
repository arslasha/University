import java.util.InputMismatchException;
import java.util.Scanner;

public class prak_1 {
    public static void main(String[] args) {
        final double ROUBLES_PER_YUAN = 11.91;
        Scanner in = new Scanner(System.in);
        System.out.print("Введите количество юаней: ");
        double yuan;
        double digit;
        try {
            yuan = Double.parseDouble(in.next());

            if(yuan > 0){
                double roubles = ROUBLES_PER_YUAN * yuan;
                roubles = Math.ceil(roubles);
                System.out.print(yuan);
                digit = yuan % 10;

                if(digit == 1 && yuan % 100 != 11) System.out.print(" юань");
                else if(digit >=2 && digit <= 4 &&(yuan % 100 != 12 && yuan %100 != 13 && yuan %100 != 14)) System.out.print(" юаня");
                else{
                    System.out.print(" юаней");
                }
                System.out.printf(" равно %.2f рублей",roubles);
            }
            else if(yuan == 0){
                System.out.println("Вы ввели нулевое значение");
            }
            else{
                System.out.println("Вводите только положительные числа! ");
            }
        }
        catch(NumberFormatException ex){
            System.out.println("Вводите только положительные числа!");
        }
        in.close();
    }
}



