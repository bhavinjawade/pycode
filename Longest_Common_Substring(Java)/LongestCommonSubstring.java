import java.util.Scanner;
import java.util.Arrays;

class LongestCommonSubstring{
  public static void main(String args[]){
    int max = 0;
    Scanner sc = new Scanner(System.in);
    String s1 = sc.next();
    String s2 = sc.next();
    int dpmat[][] = new int[s1.length()+1][s2.length()+1];
    //System.out.println(s1 + " " + s2);
    for(int i = 0; i < s1.length(); i++)
      dpmat[i][0] = 0;
    for(int j = 0; j < s2.length(); j++)
      dpmat[0][j] = 0;
    for(int i = 1; i < s1.length()+1; i++){
      for(int j = 1; j < s2.length()+1;j++){
        if(s1.charAt(i-1) == s2.charAt(j-1)){
          dpmat[i][j] = dpmat[i-1][j-1]+1;
          if(dpmat[i][j] > max)
            max = dpmat[i][j];
        }
        else
          dpmat[i][j] = 0;      
      }
    }
  /*for(int i = 0; i < s1.length()+1;i++){
    for(int j = 0 ; j < s2.length()+1; j++)
    System.out.print(dpmat[i][j]);
  System.out.print("\n");
  }*/
  System.out.println(max);
  }
}