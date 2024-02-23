#aibanez1:2/16/2024:Ex4-guess-music.bash

guess=$@
music1=country
music2=metal

if [ $guess = $music1 ]
then
  echo You got my favorite music genre
elif [ $guess = $music2 ]
then
  echo You got my not favorite music genre
else
  echo Sorry, you did not pick my music genres.
  echo Run the script again and enter a different music genre.
fi

#. Ex4-guess-music.bash country
