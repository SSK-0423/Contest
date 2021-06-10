import java.util.Scanner;
public class C
{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a > b){
            System.out.println(a * b / Gcd(a,b));
        }else{
            System.out.println(a * b / Gcd(b,a));
        } 
    }
    // ユークリッドの互除法
    public static int Gcd(int n, int m){
        int temp;
        while(n % m != 0){
            temp = m; //割る数mを保存
            m = n % m;//n / mの余りをmに代入(次の割る数)
            n = temp; //次の割られる数
        }
        return m;
    }
}