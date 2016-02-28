#Run length encoding

//Given an input string, write a function that returns the Run Length Encoded string for the input string. For example, 
//if the input string is “AABBBCCCC”, then the function should return “A2B3C4″

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

public class Magic2 {
 
    public static String encode(String source) {
        StringBuffer dest = new StringBuffer();
        for (int i = 0; i < source.length(); i++) {
            int runLength = 1;
             while (i + 1 < source.length()
                && source.charAt(i) == source.charAt(i + 1))
            
            {
                runLength++;
                i++;
            }
            
            dest.append(source.charAt(i));
            dest.append(runLength);
        }
        return dest.toString();
    }
 
     public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        System.out.println(encode(s));
     
    }
}
