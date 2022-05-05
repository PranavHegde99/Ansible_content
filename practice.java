import java.util.Scanner;

public class practice{
    public static void main(String[] args) {
        int a,b,c;
        float area,r1,r2;

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the 3 sides of triangle");
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();   
        area = (float) Math.sqrt((b*b-4*a*c)); 
            r1 = (-b+area)/(2*a);
            r2 = (-b-area)/(2*a);
    //    area = (a+b+c)/2f ;
    //    System.out.println(Math.sqrt(area*(area-a)*(area-b)*(area-c)));
       System.out.println(r1);
       System.out.println(r2);
    }
}