import java.util.*; 
import java.util.Scanner;  

class p1 { 
      
    public static void main(String[] args)  
    { 
        Scanner in = new Scanner(System.in);
        float[] arr = new float[25];
        int u = 0, a = 0;

        do
        {
            System.out.print("Introduceti un numar:");
            a = in.nextInt();
            if (a != -1)
                arr[++u] = a;
        } while (a != -1 && u != 25);

        for (int i = 0; i < arr.length; i++)
            System.out.println(arr[i]);



    } 
} 
      
