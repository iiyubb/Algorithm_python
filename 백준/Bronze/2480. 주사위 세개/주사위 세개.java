import java.util.Scanner;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int num1 = input.nextInt();
		int num2 = input.nextInt();
		int num3 = input.nextInt();
		
		int price;
		
		if ((num1 == num2) & (num1 == num3) & (num2 == num3)) {
			price = 10000 + num1 * 1000;
		} else if (num1 == num2) {
			price = 1000 + num1 * 100;
		} else if (num1 == num3) {
			price = 1000 + num1 * 100;
		} else if (num2 == num3) {
			price = 1000 + num2 * 100;
		} else {
			int[] numArr = {num1, num2, num3};
			int max = Arrays.stream(numArr).max().getAsInt();
			price = max * 100;
		}
		
		System.out.println(price);
	}

}
