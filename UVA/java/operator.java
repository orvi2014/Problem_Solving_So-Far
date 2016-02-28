// UVA:11172 - Relational Operator
// Author=Robat Das Orvi

import java.util.Scanner;
public class operator{
  public static void main(String[]args){
    Scanner k=new Scanner(System.in);
    int testcase=k.nextInt();
    for(int i=0;i<testcase;i++){
    int a=k.nextInt();
    int b=k.nextInt();
{
      if (a>b){
        System.out.println(">");
        
      }
      else if(a<b){
      System.out.println("<");}
      else
      {
      System.out.println("=");}
    }
    
    }
  }}