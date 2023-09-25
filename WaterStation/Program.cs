using System;
using static System.Console;
namespace WaterStation
{
class Program
{
static void Main (string[] args)
{
    double Place;
    Place = Double.Parse(Console.ReadLine());
    double diference = Place%10;
    if(diference>=3 && diference<=7){
        Console.WriteLine((Place-diference)+5);
    }else if(diference<5){
Console.WriteLine((Place-diference));
    }else{
Console.WriteLine((Place+(10-diference)));
    }
     
}
}
}