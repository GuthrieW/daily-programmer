public class CaesarCipher {
    public static void main(String[] args) {
        // getting program arguments
        int shiftAmount = Integer.parseInt(args[1]);
        char[] plainText = args[0].toLowerCase().toCharArray();

        // encryption
        System.out.println("Encrypting...");
        char[] encryptedMessage = new char[plainText.length];
        for (int i = 0; i < plainText.length; i++) {
            int tempIntegerValue = plainText[i] + shiftAmount;
            if (tempIntegerValue > 112)
                tempIntegerValue -= 26;
            char newCharacterValue = (char) tempIntegerValue;
            encryptedMessage[i] = newCharacterValue;
        }
        System.out.println(new String(encryptedMessage));

        // decryption
        System.out.println("Decrypting...");
        char[] decryptedMessage = new char[encryptedMessage.length];
        for (int i = 0; i < encryptedMessage.length; i++) {
            int tempIntegerValue = encryptedMessage[i] - shiftAmount;
            if (tempIntegerValue < 97)
                tempIntegerValue += 26;
            char newCharacterValue = (char) tempIntegerValue;
            decryptedMessage[i] = newCharacterValue;
        }
        System.out.println(new String(decryptedMessage));
    }
}