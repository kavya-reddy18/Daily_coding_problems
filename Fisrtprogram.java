import java.util.HashMap;
import java.util.Scanner;

public class Fisrtprogram {
	public static boolean solve(int[] a ,int n,int k) {
		HashMap<Integer,Integer> hm=new HashMap<Integer,Integer>();
		for(int i=0;i<n;i++) {
			int current = k-a[i];
			if(hm.containsKey(current)) {
				return true;
			}
			if(hm.containsKey(a[i])) {
				hm.put(a[i],hm.get(a[i])+1);
			}
			else {
				hm.put(a[i],1);
			}
		}
		return false;
		
	}
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int k=sc.nextInt();
		int[] a=new int[n];
		for(int i=0;i<n;i++) {
			a[i]=sc.nextInt();
		}
		System.out.println(solve(a,n,k));
	}

}
