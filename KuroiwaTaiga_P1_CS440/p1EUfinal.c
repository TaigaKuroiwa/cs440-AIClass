#include <stdio.h>
#include <stdlib.h>
#define LIMIT_CONT 250
#define true 1
#define false 0
typedef int bool;
unsigned char countrymap[LIMIT_CONT];


unsigned char countrylist[42][64] = {
	"Portugal", "France", "Italy", "Switzerland", "Spain", "Germany", 	
	"Andorra", "Luxenbourg", "Belgium", "Denmark", "Netherlands", "Liechtenstein",
	"Austria", "Slovenia", "Croatia", "Bosnia", "Montenegro", "Albania", "Kosovo", 
	"Macedonia", "Greece", "Bulgaria", "Turkey", "Armenia", "Azerbaijan", "Serbia", 
	"Romania", "Moldova", "Hungary", "Ukraine", "Slovakia", "Czech", "Poland", "Belarus", 
	"Lithuania", "Latvia", "Estonia", "Norway", "Sweden", "Finland", "Russia"
};

unsigned char areapattern[LIMIT_CONT][64][64] ={
	{"Spain", "nocount"},//Portugal, this nocount means function does not need to find further
	{"Spain", "Italy", "Switzerland", "Germany", "Belgium", "Andorra", "nocount"},//France
	{"Slovenia", "Austria", "France", "nocount"},//Italy
	{"Liechtenstein", "Austria", "France", "nocount"},//Switzerland
	{"Andorra", "Portugal", "France", "nocount"},//Spain
	{"Denmark", "France", "Luxenbourg", "Belgium", "Netherlands", "Austria", "Czech", "Poland", "nocount"},//Germany
	{"Spain", "France", "nocount"},//Andorra
	{"France", "Belgium", "nocount"},//Luxenbourg
	{"Germany", "Netherlands", "France", "Luxenbourg", "nocount"},//Belgium
	{"Germany", "nocount"},//Denmark
	{"Belgium", "Germany", "nocount"},//Netherlands
	{"Switzerland", "Austria", "nocount"},//Liechtenstein
	{"Italy", "Switzerland", "Germany", "Slovenia", "Hungary", "Slovakia", "Czech", "nocount"},//Austria
	{"Italy", "Austria", "Croatia", "Hungary", "nocount"},//Slovenia
	{"Bosnia", "Slovenia", "Serbia", "Hungary", "nocount"},//Croatia
	{"Montenegro", "Croatia", "Serbia", "nocount"},//Bosnia
	{"Bosnia", "Albania", "Kosovo", "Serbia", "nocount"},//Montenegro
	{"Kosovo", "Montenegro", "Macedonia", "Greece", "nocount"},//Albania
	{"Albania", "Montenegro", "Macedonia", "Serbia", "nocount"},//Kosovo
	{"Albania", "Kosovo", "Greece", "Bulgaria", "Serbia", "nocount"},//Macedonia
	{"Albania", "Macedonia", "Bulgaria", "Turkey", "nocount"},//Greece
	{"Macedonia", "Greece", "Turkey", "Serbia", "Romania", "nocount"},//Bulgaria
	{"Greece", "Bulgaria", "Armenia", "Georgia", "Azerbaijan", "nocount"},//Turkey
	{"Turkey", "Georgia", "Azerbaijan", "nocount"},//Armenia
	{"Armenia", "Georgia", "Russia", "nocount"},//Azerbaijan
	{"Romania", "Hungary", "Bulgaria", "Macedonia", "Kosovo", "Montenegro", "Bosnia", "Croatia", "nocount"},//Serbia
	{"Bulgaria", "Serbia", "Moldova", "Hungary", "Ukraine", "nocount"},//Romania
	{"Romania", "Ukraine", "nocount"},//Moldova
	{"Serbia", "Romania", "Slovakia", "Ukraine", "Croatia", "Slovenia", "Austria", "nocount"},//Hungary
	{"Moldova", "Romania", "Hungary", "Slovakia", "Poland", "Belarus", "Russia", "nocount"},//Ukraine
	{"Hungary", "Ukraine", "Czech", "Austria", "nocount"},//Slovakia
	{"Slovakia", "Poland", "Austria", "Germany", "nocount"},//Czech
	{"Ukraine", "Czech", "Belarus", "Russia", "Lithuania", "Germany", "nocount"},//Poland
	{"Latvia", "Lithuania", "Ukraine", "Poland", "Russia", "nocount"},//Belarus
	{"Poland", "Lithuania", "Latvia", "Russia", "nocount"},//Lithuania
	{"Belarus", "Lithuania", "Estonia", "Russia", "nocount"},//Latvia
	{"Latvia", "Russia", "nocount"},//Estonia
	{"Sweden", "Finland", "Russia", "nocount"},//Norway
	{"Norway", "Finland", "nocount"},//Sweden
	{"Sweden", "Norway", "Russia", "nocount"},//Finland
	{"Norway", "Finland", "Lithuania", "Estonia", "Latvia", "Belarus", "Poland", "Ukraine", "Azerbaijan", "Georgia", "nocount"}//Russia
	
};

bool isusedcolor(unsigned char country, int color)
{
	unsigned char c, checking;
	int i = 0;
	while (areapattern[country][i] != "nocount"){
		checking = areapattern[country][i];
		if (color == countrymap[checking])
			return true;
		i++;
	}
	return false;
}

bool colorsearch(unsigned char country, int color, int m)
{
	
	if(isusedcolor(country,color)){
		return false;
	}
	
	countrymap[m]=color;
	country++;
	++m;
	if (country >= LIMIT_CONT)
		return true;
	for (color = 1; color < 4; color++)
	{	
		if (colorsearch(country, color, m))
			break;
	}
	if (color == 4)
		return false;
	return true;
}

int main(){
	int i = 0;
	int n = 0;
	int j = 0;
	int m = 0;
	int colors[4]={1,2,3,4};
		
	colorsearch(areapattern[i], colors[j], m);
	for(n=0; n<48; ++n){
	printf("%s%s,", countrylist[n], countrymap[n]);
	}
	return 0;
}