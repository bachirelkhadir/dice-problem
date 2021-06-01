##
# Makefile
#
# @file
# @version 0.1



run:
	gnome-terminal -e "manimgl main.py" --title="gnome-terminal manim"


idice:
	gnome-terminal -e "manimgl dice.py" --title="gnome-terminal manim"


vrec:
	manimgl recurrence.py -tw && cd output/videos/ && bash mov_to_pngs.sh RecurrenceScene.mov


vtext:
	for i in $$(grep class make_text.py | cut -d' ' -f2 | cut -d'(' -f1); do manimgl make_text.py $$i -wt; done

vgame:
	manimgl dice.py GamesOfDice  -w

vaverage:
	manimgl average.py -wt


thirdway:
	manimgl make_text.py ThirdWayQuestion -wt


vslider:
	manimgl slider.py Slider -wt


vsolution1:
	manimgl solution1.py -wt && cd output/videos/ && bash mov_to_pngs.sh SolutionOne.mov

vsolutionthree:
	manimgl solution_three.py -wt && cd output/videos/ && bash mov_to_pngs.sh SolutionThree.mov


vcointoss:
	manimgl coin_toss.py  CoinToss -wt  && cd output/videos/ && bash mov_to_pngs.sh CoinToss.mov


vdistr:
	manimgl distribution.py -wt  && cd output/videos/ && bash mov_to_pngs.sh Distribution.mov

vq1:
	manimgl question_one.py -wt && cd output/videos/ && bash mov_to_pngs.sh QuestionOne.mov

vq1text:
	manimgl make_text.py TwoSixes -wt && cd output/videos/ && bash mov_to_pngs.sh TwoSixes


vq2:
	manimgl question_two.py -wt && cd output/videos/ && bash mov_to_pngs.sh QuestionTwo.mov

vq2text:
	manimgl make_text.py Conditional -wt && cd output/videos/ && bash mov_to_pngs.sh Conditional


vlln:
	manimgl law_of_large_numbers.py LawLargeNumbers -wt && cd output/videos/ && bash mov_to_pngs.sh LawLargeNumbers

vcoinlln:
	manimgl law_of_large_numbers.py LLNWithCoins -wt && cd output/videos/ && bash mov_to_pngs.sh LLNWithCoins

vexciting:
	manimgl make_text.py NotTheMostExciting -wt && cd output/videos/ && bash mov_to_pngs.sh NotTheMostExciting

vequallylikely:
	manimgl equally_likely.py  EquallyLikely -wt && cd output/videos/ && bash mov_to_pngs.sh  EquallyLikely

vcolorarea:
	manimgl color_area.py  ColorArea -wt && cd output/videos/ && bash mov_to_pngs.sh  ColorArea


vnot6then6:
	manimgl equally_likely.py  Not6Then6 -wt && cd output/videos/ && bash mov_to_pngs.sh  Not6Then6

vnot6not6then6:
	manimgl equally_likely.py  Not6Not6Then6 -wt && cd output/videos/ && bash mov_to_pngs.sh  Not6Not6Then6

vsumkxk:
	manimgl make_text.py   Sumkxk -wt && cd output/videos/ && bash mov_to_pngs.sh  Sumkxk

vcaptionlln:
	manimgl make_text.py   CaptionLLN -wt && cd output/videos/ && bash mov_to_pngs.sh CaptionLLN


vapproximationgetsbetter:
	manimgl law_of_large_numbers.py ApproximationGetsBetter -wt && cd output/videos/ && bash mov_to_pngs.sh ApproximationGetsBetter


vmedian:
	manimgl make_text.py WhatIsMedian -wt && cd output/videos/ && bash mov_to_pngs.sh WhatIsMedian

pngs:
	cd output/videos/ && bash mov_to_pngs.sh

captions:
	manimgl slider.py BouncingSolution1 BouncingSolution2 BouncingSolution3 BouncingQuestion1 BouncingQuestion2 BouncingQuestion3 -wt && cd output/videos/ && bash mov_to_pngs.sh  "BouncingSolution1 BouncingSolution2 BouncingSolution3 BouncingQuestion1 BouncingQuestion2 BouncingQuestion3"

unexpected:
	manimgl make_text.py UnexpectedConsequence -wt && cd output/videos/ && bash mov_to_pngs.sh UnexpectedConsequence
thanks:
	manimgl make_text.py Thankyou -wt && cd output/videos/ && bash mov_to_pngs.sh Thankyou

remote:
	bash remote_compile.sh

stop:
	echo "Stopped"

# end
