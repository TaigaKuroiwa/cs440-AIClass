#include <stdio.h>
#include <stdlib.h>
#define LIMIT_CONT 49
#define true 1
#define false 0
#define COLOR_LIMIT 4

typedef int bool;
unsigned char countrymap[LIMIT_CONT];



unsigned char countrylist[49][8] = {
	"WA", "OR", "ID", "CA", "NV", "MT", "UT", "ND", "WY", "AZ", "SD", "CO", "NB", "NM", "MN",
	"KS", "IA", "OK", "WS", "MO", "TX", "IL", "AR", "MI", "KY", "LA", "IN", "TN", "OH", "MS", "WV",
	"VA", "MD", "NC", "PA", "DE", "SC", "NY", "NJ", "GA", "CT", "AL", "RI", "FL", 
	"MA", "VT", "NH", "ME", "nocount" };

unsigned char areapattern[][9][251] ={
	{"OR", "ID", "nocount"},//WA
	{"WA", "ID", "CA", "NV", "nocount"},//OR
	{"WA", "OR", "NV", "UT", "WY", "MT", "nocount"},//ID
	{"OR", "AZ", "NV", "nocount"},//CA
	{"OR", "ID", "CA", "UT", "AZ", "nocount"},//NV
	{"ID", "ND", "WY", "SD", "nocount"},//MT
	{"ID", "NV", "AZ", "WY", "CO", "nocount"},//UT
	{"MT", "SD", "MN", "nocount"},//ND
	{"ID", "MT", "UT", "SD", "CO", "nocount"},//WY
	{"UT", "NV", "CA", "nocount"},//AZ
	{"ND", "MT", "WY", "NB", "MN", "IA", "nocount"},//SD
	{"WY", "UT", "NB", "KS", "OK", "NM", "nocount"},//CO
	{"SD", "WY", "CO", "MN", "IA", "KS", "nocount"},//NB
	{"CO", "AZ", "OK", "TX", "nocount"},//NM
	{"ND", "SD", "WS", "IA", "nocount"},//   MN
	{"NB", "CO", "MO", "OK", "nocount"},//KS
	{"MN", "NB", "WS", "MO", "SD", "IL", "nocount"},//IA
	{"KS", "CO", "NM", "MO", "AR", "TX", "nocount"},//OK
	{"MN", "IA", "MI", "IL", "nocount"},//WS
	{"IA", "KS", "OK", "IL", "KY", "TN", "AR", "nocount"},//MO
	{"OK", "NM", "AR", "LA", "nocount"},//TX
	{"WS", "IA", "MO", "IN", "KY", "nocount"},//IL
	{"MO", "OK", "TX", "TN", "MS", "LA", "nocount"},//AR
	{"WS", "IN", "OH", "nocount"},//MI
	{"IL", "IN", "MO", "TN", "OH", "WV", "VA", "nocount"},//KY
	{"AR", "TX", "MS", "nocount"},//LA
	{"MI", "IL", "KY", "OH", "nocount"},//IN
	{"KY", "MO", "AR", "MS", "VA", "NC", "GA", "AL", "nocount"},//TN
	{"MI", "IN", "KY", "PA", "WV", "nocount"},//OH
	{"TN", "AR", "LA", "AL", "nocount"},//MS
	{"OH", "KY", "PA", "MD", "VA", "nocount"},//WV
	{"WV", "KY", "TN", "MD", "NC", "nocount"},//VA
	{"WV", "VA", "PA", "DE", "nocount"},//MD
	{"VA", "TN", "SC", "nocount"},//NC
	{"OH", "WV", "MD", "NY", "NJ", "nocount"},//PA
	{"PA", "MD", "NJ", "nocount"},//DE
	{"NC", "GA", "nocount"},//SC
	{"PA", "CT", "MA", "VT", "nocount"},//NY
	{"PA", "DE", "nocount"},//NJ
	{"SC", "FL", "AL", "TN", "nocount"},//GA
	{"NY", "RI", "MA", "nocount"},//CT
	{"GA", "FL", "TN", "MS", "nocount"},//AL
	{"CT", "MA", "nocount"},//RI
	{"GA", "AL", "nocount"},//FL
	{"RI", "CT", "NY", "VT", "NH", "nocount"},//MA
	{"MA", "NY", "NH", "nocount"},//VT
	{"MA", "VT", "ME", "nocount"},//NH
	{"NH", "nocount"}//ME
};

bool isusedcolor(unsigned char country, unsigned char color)
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

bool colorsearch(unsigned char country, unsigned char color)
{
	int ready = 0;//ここから擬似boolとして扱う?
	if(isusedcolor(country,color)){
		return false;
	}
	countrymap[country]=color;
	country++;
	if (country >= LIMIT_CONT)
		return true;
	for (color = 1; color < COLOR_LIMIT; color++)
	{
		if (colorsearch(country, color))
			break;
	}
	if (color == COLOR_LIMIT)
		return false;
	return true;
}

int main(){
	int i = 0;
	int n = 0;
	int j = 0;
	unsigned char colors[4][5] = {"white", "red", "blue", "green"};
		
	colorsearch(areapattern[i], colors[j]);
	for(n=0; n<48; ++n){
	printf("%s%s,", countrylist[n], countrymap[n]);
	}
	return 0;
}