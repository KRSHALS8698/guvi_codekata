import java.util.*;
import java.io.*;
import java.lang.*;
public class MyClass {
    public static void main(String args[]) {
   int n,i;
   
   Scanner sc=new Scanner(System.in);
   n=sc.nextInt();
   int [] a=new int[n];
   for(i=0;i<n;i++)
   {
       a[i]=sc.nextInt();
   }
   int big=a[0];
   for(i=1;i<n;i++)
   {
       if(a[i]>big)
       {
           big=a[i];
       }
   }
   System.out.println(big);
    }
}
