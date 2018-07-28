import java.io.*;
import java.util.*;
public class MyClass {
    public static void main(String args[]) {
        
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int [] a=new int[n];
        int i;
        for(i=0;i<n;i++)
        {
            a[i]=sc.nextInt();
        }
       int small=a[0];
        for(i=1;i<n;i++)
        {
            if(a[i]<small)
            {
                small=a[i];
            }
        }
        System.out.println(small);
    }
}
