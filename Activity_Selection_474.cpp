#include<bits/stdc++.h>
using namespace std;

bool comp(pair<int,int>i,pair<int,int>j){
    return i.second<j.second;
}

int main()
{
     
      int s[11]={0,1,2,3,3,5,5,6,8,8,12};           // Start time
      int f[11]={6,4,14,5,9,7,9,10,11,12,16};       // Finish time
      vector<pair<int,int>>vec(11);
      cout<<"Start time of activities: "<<endl;
      for(int i=0;i<11;i++){
          vec[i].first=s[i];
          cout<<vec[i].first<<" ";
      }
      cout<<"\nEnd time of activities: "<<endl;
      for(int i=0;i<11;i++){
          vec[i].second=f[i];
          cout<<vec[i].second<<" ";
      }
  
      sort(vec.begin(),vec.end(),comp);		// Sorting activities based on Finish time in increasing order
      vector<pair<int,int>>v;
      v.push_back(vec[0]);
      pair<int,int>current=vec[0];
      for(int j=1;j<11;j++){
          if(vec[j].first > current.second){
              v.push_back(vec[j]);
              current=vec[j];
          }
      }
      vector<pair<int,int>>::iterator i;
      cout<<"\nFollowing activities are selected- "<<endl;
      for(i=v.begin();i!=v.end();i++){
          cout<<"("<<(*i).first<<","<<(*i).second<<"), ";
      }
      cout<<endl;
  return 0;
}
