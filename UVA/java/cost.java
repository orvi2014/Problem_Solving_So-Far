// Uva 11727 - Cost Cutting
// Author= Robat Das Orvi

import java.util.Scanner;
public class cost {  
      static int testCases;  
      static int a;  
      static int b;  
      static int c;  
      public static void main(String[] args) {  
           Scanner k = new Scanner(System.in);  
           testCases = k.nextInt();  
           for(int i = 1; i < testCases+1; i++) {  
                a = k.nextInt();  
                b = k.nextInt();  
                c = k.nextInt();  
                System.out.print("Case " + i + ": ");  
                if (a > b) {  
                     if (b > c) {  
                          System.out.println(b);  
                          continue;  
                     }  
                     if (a > c) {  
                          System.out.println(c);  
                          continue;  
                     }  
                     System.out.println(a);  
                     continue;  
                }  
                if (a > c) {  
                     System.out.println(a);  
                     continue;  
                }  
                if (b > c) {  
                     System.out.println(c);  
                     continue;  
                }  
                System.out.println(b);  
                continue;  
           }  
      }  
 }  