#include <iostream>

using namespace std;
int x, y;
string week[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> x >> y;
    if(x==1 || x==10){//1월1일 월요일 10월 1일 월요일
        cout << week[y%7];
    }
    if(x==2 || x==3 || x==11){//2월1일 목요일,3월1일 목요일 11월 1일 목요일
        cout << week[(y+3)%7];
    }
    if(x==4 || x==7){//4월 1일 일요일 7월1일 일요일
        cout << week[(y+6)%7];
    }
    if(x==5){//5월 1일 화요일
        cout << week[(y+1)%7];
    }
    if(x==6){//6월 1일 금요일
        cout << week[(y+4)%7];
    }
    if(x==8){//8월 1일 수요일
        cout << week[(y+2)%7];
    }
    if(x==9 || x==12){//9월 1일 토요일 12월 1일 토요일
        cout << week[(y+5)%7];
    }
    return 0;
}