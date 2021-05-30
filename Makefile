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
	manimgl recurrence.py -tw && cd output/videos/ && bash mov_to_pngs.sh RecurrenceScene.mov

irec:
	manimgl recurrence.py -ws -n 10,11

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
	manimgl solution1.py -n 40

esolution1:

	gnome-terminal -e "manimgl solution1.py -n 20" --title="gnome-terminal manim"

isolution1:
	manimgl solution1.py -ws

vsolution1:
	manimgl solution1.py -wt && cd output/videos/ && bash mov_to_pngs.sh SolutionOne.mov


solutionthree:
	manimgl solution_three.py -n 27

isolutionthree:
	manimgl solution_three.py -ws -n 4,5

vsolutionthree:
	manimgl solution_three.py -wt && cd output/videos/ && bash mov_to_pngs.sh SolutionThree.mov

cointoss:
	manimgl coin_toss.py CoinToss

icointoss:
	manimgl coin_toss.py  CoinToss -ws

vcointoss:
	manimgl coin_toss.py  CoinToss -wt  && cd output/videos/ && bash mov_to_pngs.sh CoinToss.mov


distr:
	manimgl distribution.py

idistr:
	manimgl distribution.py -ws

vdistr:
	manimgl distribution.py -wt  && cd output/videos/ && bash mov_to_pngs.sh Distribution.mov



q1:
	manimgl question_one.py

iq1:
	manimgl question_one.py -ws

vq1:
	manimgl question_one.py -wt && cd output/videos/ && bash mov_to_pngs.sh QuestionOne.mov

q1text:
	manimgl make_text.py TwoSixes

iq1text:
	manimgl make_text.py TwoSixes -ws

vq1text:
	manimgl make_text.py TwoSixes -wt && cd output/videos/ && bash mov_to_pngs.sh TwoSixes

q2:
	manimgl question_two.py

iq2:
	manimgl question_two.py -ws

vq2:
	manimgl question_two.py -wt && cd output/videos/ && bash mov_to_pngs.sh QuestionTwo.mov


q2text:
	manimgl make_text.py Conditional

iq2text:
	manimgl make_text.py Conditional -ws

vq2text:
	manimgl make_text.py Conditional -wt && cd output/videos/ && bash mov_to_pngs.sh Conditional

pngs:
	cd output/videos/ && bash mov_to_pngs.sh


remote:
	bash remote_compile.sh

stop:
	echo "Stopped"

# end
