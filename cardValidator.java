import java.util.Scanner;

public class CardValidator {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter your Credit Card Number: ");
        String cardNumber = input.nextLine();

        int[] cardNumberArray = new int[cardNumber.length()];

        for (int index = 0; index < cardNumber.length(); index++) {
            cardNumberArray[index] = cardNumber.charAt(index) - '0';
        }

        System.out.println("Credit Card Type: " + creditCardType(cardNumberArray));
        System.out.println("Credit Card Number: " + cardNumber);
        System.out.println("Credit Card Length: " + cardNumber.length());
        System.out.println("Card validity: " + (isValid(cardNumberArray) ? "Valid" : "Invalid"));
    
    }

    public static int digitDoubling(int[] cardNumberArray) {
        int sum = 0;

        for (int index = cardNumberArray.length - 2; index >= 0; index -= 2) {
            int number = cardNumberArray[index] * 2;
            if (number > 9) {
                number -= 9;
            }
            sum += number;
        }

        return sum;
    }

    public static int oddNumberSum(int[] cardNumberArray) {
        int sum = 0;
        for (int index = cardNumberArray.length - 1; index >= 0; index -= 2) {
            sum += cardNumberArray[index];
        }
        return sum;
    }

    public static boolean isValid(int[] cardNumberArray) {
        int total = oddNumberSum(cardNumberArray) + digitDoubling(cardNumberArray);
        return total % 10 == 0;
    }

    public static String creditCardType(int[] cardNumberArray) {
        if (cardNumberArray[0] == 4) return "Visa Card";
        if (cardNumberArray[0] == 5) return "Master Card";
        if (cardNumberArray[0] == 3 && cardNumberArray[1] == 7) return "American Express Card";
        if (cardNumberArray[0] == 6) return "Discover Card";

        return "Type not found";
    }
}

