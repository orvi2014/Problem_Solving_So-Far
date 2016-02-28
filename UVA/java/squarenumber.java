import java.util.Scanner;
public class squarenumber{
  public static void main(String[]args){
  Scanner k=new Scanner(System.in);
  
 
  for(int i=0;i<=201; i++){
  int a=k.nextInt();
  int b=k.nextInt();
  if(a==0 && b==0){
  break;}
  int count=0;
  if(a>0 && a<=b && b<=100000)
                {
                    for(int j=a; j<=b; j++)
                    {
                        int st=(int)Math.sqrt(j);
                        if(st*st==j)
                        {
                            count++;
                        }
                    }
                }
                System.out.println(count);
  
  }
  
  
  }
}