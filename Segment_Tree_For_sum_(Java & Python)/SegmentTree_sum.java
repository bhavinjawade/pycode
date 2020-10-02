class SegmentTree{
    int st[];
    
    SegmentTree(int a[], int n){
      int x = (int) (Math.ceil(Math.log(n) / Math.log(2)));
      int stsize = 2 * (int)Math.pow(2,x) - 1;
      st = new int[stsize];
      constructst(a,0,n-1,0);//array,start,end,position
    }
    
    int constructst(int a[], int s, int e , int pos){
      if(s == e)
        {
          //System.out.println(pos + " " + s);
          st[pos] = a[s]; return a[s];
        }
      int mid = (s + e)/2;
      //System.out.println(mid + " " + s + " " + e);
      st[pos] = constructst(a,s,mid,2*pos+1) + constructst(a,mid+1,e,2*pos+2);
      return st[pos];
    }
    
    int getresult(int low,int high, int s, int e, int pos){
      if(low <= s && e <= high)
        return st[pos];
      if(high < s || low > e)
        return 0;
      int mid = (e + s) / 2;
      return getresult(low,high,s,mid,2*pos+1) + getresult(low,high,mid+1,e,2*pos+2); 
    }
    
    void update(int s, int e, int index , int diff, int pos){
      if(index < s || index > e)
        return;
        
      st[pos] = st[pos] + diff;
      if (s != e) {
              int mid = (e + s) / 2;
              update(s, mid, index, diff, 2 * pos + 1);
              update(mid + 1, e, index, diff, 2 * pos + 2);
          }
    }
  }
  class Main{
   public static void main(String args[]){
      int arr[] = {1, 3, 5, 7, 9, 11};
          int n = arr.length;
          SegmentTree  tree = new SegmentTree(arr, n);
          System.out.println("Sum of values in given range = " + tree.getresult(1, 3,0,n-1,0));
          tree.update(0, n-1 , 1, 7 ,0); 
          // start,end,indextochange, diffbywhichtoadd,pos
          System.out.println("Sum of values in given range = " + tree.getresult(1, 3,0,n-1,0));
     
   }
  }