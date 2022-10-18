import java.io.*;
import java.util.*;
import java.math.BigInteger;
public class JavaBigInteger 
{
public static void main(String[] args)
{   
    Scanner sc = new Scanner(System.in);

    BigInteger A = sc.nextBigInteger();
    BigInteger B = sc.nextBigInteger();

    if(((int) Math.log10(A.intValue())+1)<200 && ((int) Math.log10(B.intValue())+1)<200){       
        System.out.println(A.add(B));
        System.out.println(A.multiply(B));
    }
}
}