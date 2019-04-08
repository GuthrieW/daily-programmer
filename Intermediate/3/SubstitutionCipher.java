import java.util.*;

public class SubstitutionCipher {
    public static void main(String[] args) {
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        Character[] alphabetInOrder = new Character[alphabet.length];
        for (int i = 0; i < alphabet.length; i++) {
            alphabetInOrder[i] = alphabet[i];
        }

        Character[] alphabetOutOfOrder = alphabetInOrder.clone();
        List<Character> alphabetList = Arrays.asList(alphabetOutOfOrder);
        Collections.shuffle(alphabetList);
        
        Map<Character, Character> substitutionMap = new HashMap<>();
        for (int i = 0; i < alphabetInOrder.length; i++) {
            substitutionMap.put(alphabetInOrder[i], alphabetList.get(i));
        }
        
        String plainText = "This is some plain text".toLowerCase();
        StringBuilder encryptedString = new StringBuilder();
        for (int i = 0; i < plainText.length(); i++) {
            if (substitutionMap.get(plainText.charAt(i)) != null) {
                encryptedString.append(substitutionMap.get(plainText.charAt(i)));
            } else {
                encryptedString.append(plainText.charAt(i));
            }
        }
        
        System.out.println(encryptedString);
    }
}