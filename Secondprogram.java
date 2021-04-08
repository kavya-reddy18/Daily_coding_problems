import java.util.*;
public class Secondprogram {
	public static ArrayList<Integer> solve(int[] a,int n){
		ArrayList<Integer> pre=new ArrayList<>();
		int temp=1;
		if (n!=1) {
		for(int i=0;i<n;i++) {
			pre.add(temp);
			temp*=a[i];
		}
		temp=1;
		for(int i=n-1;i>=0;i--) {
			pre.set(i,pre.get(i)*temp);
			temp*=a[i];
		}
		}
		return pre;	
	}
	public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int[] a=new int[n];
		for(int i=0;i<n;i++) {
			a[i]=sc.nextInt();
		}
		System.out.println(solve(a,n));
	}
}
