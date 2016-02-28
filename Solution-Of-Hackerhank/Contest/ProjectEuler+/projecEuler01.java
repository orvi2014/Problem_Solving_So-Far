import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner k=new Scanner(System.in);
        int input=k.nextInt();
        for(int i=0;i<input;i++){
            int n=k.nextInt();
            long sum=0;
            for ( long j = 3 ; j <n ; j+=3 ){
                    sum+=j;
                   }
             for ( long j = 5 ; j <n ; j+=5 ){
                  sum+=j;
                   }
            for(long j=15; j<n; j+=15){
                sum-=j;
            }
           System.out.println(sum);
        } 
     
    }
}