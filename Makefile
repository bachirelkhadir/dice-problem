##
# Makefile
#
# @file
# @version 0.1



run:
	gnome-terminal -e "manimgl main.py" --title="gnome-terminal manim"


idice:
	gnome-terminal -e "manimgl dice.py" --title="gnome-terminal manim"

dice:
	manimgl dice.py

rec:
	manimgl recurrence.py

vrec:
	manimgl recurrence.py -ws
irec:
	gnome-terminal -e "manimgl recurrence.py" --title="gnome-terminal manim"

vtext:
	for i in $$(grep class make_text.py | cut -d' ' -f2 | cut -d'(' -f1); do manimgl make_text.py $$i -wt; done

text:
	manimgl make_text.py  Current

itext:
	manimgl make_text.py  Current -ws

game:
	manimgl dice.py GamesOfDice

vgame:
	manimgl dice.py GamesOfDice  -w

vaverage:
	manimgl average.py -wt

saverage:
	manimgl average.py -ws

average:
	manimgl average.py

thirdway:
	manimgl make_text.py ThirdWayQuestion -wt

islider:
	manimgl slider.py Slider -ws


slider:
	manimgl slider.py Slider

vslider:
	manimgl slider.py Slider -wt


solution1:
	manimgl solution1.py -n 12

isolution1:
	manimgl solution1.py -ws

vsolution1:
	manimgl solution1.py -wt


pngs:
	cd output/videos/ && bash mov_to_pngs.sh

stop:
	echo "Stopped"

# end
