import java.io.*;
import java.util.*;
public class MyClass {
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.print((n/60)+" "+(n%60));
    }
}
