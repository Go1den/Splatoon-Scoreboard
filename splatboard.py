from graphics import *
from splatboxscorewindowcoords import *
from splatfieldlabels import *
from splatscoreboardwindowcoords import *
from splatsettings import *
from splatsettingswindowcoords import *

class Splatoon(object):

    def __init__(self):
        self.settings_win = GraphWin(SETTINGS_WINDOW_TITLE, SETTINGS_WINDOW_WIDTH, SETTINGS_WINDOW_HEIGHT)
        self.boxscore_win = GraphWin(BOXSCORE_WINDOW_TITLE, BOXSCORE_WINDOW_WIDTH, BOXSCORE_WINDOW_HEIGHT)
        self.ScoreHistory = []
        self.currentMap = ""
        self.currentGametype = ""
        self.inputName1 = Entry(Point(XCOORD_INPUTNAME1, YCOORD_INPUTNAME1), MAX_TEAMNAME_LENGTH)
        self.inputName2 = Entry(Point(XCOORD_INPUTNAME2, YCOORD_INPUTNAME2), MAX_TEAMNAME_LENGTH)
        self.inputName1Text = Text(Point(XCOORD_INPUTNAME1TEXT, YCOORD_INPUTNAME1TEXT), TEAM1)
        self.inputName2Text = Text(Point(XCOORD_INPUTNAME2TEXT, YCOORD_INPUTNAME2TEXT), TEAM2)
        self.controlsTeam1 = Text(Point(XCOORD_CONTROLSTEAM1, YCOORD_CONTROLSTEAM1), TEAM1CONTROLS)
        self.controlsTeam2 = Text(Point(XCOORD_CONTROLSTEAM2, YCOORD_CONTROLSTEAM2), TEAM2CONTROLS)
        self.updateTeamNamesText = Text(Point(XCOORD_UPDATETEAMNAMESTEXT, YCOORD_UPDATETEAMNAMESTEXT), UPDATETEAMS)
        self.swapTeamsText = Text(Point(XCOORD_SWAPTEAMSTEXT, YCOORD_SWAPTEAMSTEXT), SWAPCOLORS)
        self.updateTeamNames = Rectangle(Point(XCOORD_UPDATETEAMS_TL, YCOORD_UPDATETEAMS_TL), Point(XCOORD_UPDATETEAMS_BR, YCOORD_UPDATETEAMS_BR))
        self.swapTeams = Rectangle(Point(XCOORD_SWAPTEAMS_TL, YCOORD_SWAPTEAMS_TL), Point(XCOORD_SWAPTEAMS_BR, YCOORD_SWAPTEAMS_BR))
        self.minus1Team1 = Rectangle(Point(XCOORD_MINUS1TEAM1_TL, YCOORD_MINUS1TEAM1_TL), Point(XCOORD_MINUS1TEAM1_BR, YCOORD_MINUS1TEAM1_BR))
        self.minus1Team2 = Rectangle(Point(XCOORD_MINUS1TEAM2_TL, YCOORD_MINUS1TEAM2_TL), Point(XCOORD_MINUS1TEAM2_BR, YCOORD_MINUS1TEAM2_BR))
        self.plus1Team1 = Rectangle(Point(XCOORD_PLUS1TEAM1_TL, YCOORD_PLUS1TEAM1_TL), Point(XCOORD_PLUS1TEAM1_BR, YCOORD_PLUS1TEAM1_BR))
        self.plus1Team2 = Rectangle(Point(XCOORD_PLUS1TEAM2_TL, YCOORD_PLUS1TEAM2_TL), Point(XCOORD_PLUS1TEAM2_BR, YCOORD_PLUS1TEAM2_BR))
        self.minus1Team1Text = Text(Point(XCOORD_MINUS1TEAM1TEXT, YCOORD_MINUS1TEAM1TEXT), MINUS1)
        self.minus1Team2Text = Text(Point(XCOORD_PLUS1TEAM1TEXT, YCOORD_PLUS1TEAM1TEXT), PLUS1)
        self.plus1Team1Text = Text(Point(XCOORD_MINUS1TEAM2TEXT, YCOORD_MINUS1TEAM2TEXT), MINUS1)
        self.plus1Team2Text = Text(Point(XCOORD_PLUS1TEAM2TEXT, YCOORD_PLUS1TEAM2TEXT), PLUS1)
        self.bgStrawberryP1 = getImage(SAMPLE_STRAWBERRY, XCOORD_BG_STRAWBERRY_P1, YCOORD_BG_STRAWBERRY_P1)
        self.bgOrangeP1 = getImage(SAMPLE_ORANGE, XCOORD_BG_ORANGE_P1, YCOORD_BG_ORANGE_P1)
        self.bgButterscotchP1 = getImage(SAMPLE_BUTTERSCOTCH, XCOORD_BG_BUTTERSCOTCH_P1, YCOORD_BG_BUTTERSCOTCH_P1)
        self.bgBananaP1 = getImage(SAMPLE_BANANA, XCOORD_BG_BANANA_P1, YCOORD_BG_BANANA_P1)
        self.bgYellowP1 = getImage(SAMPLE_YELLOW, XCOORD_BG_YELLOW_P1, YCOORD_BG_YELLOW_P1)
        self.bgPastelGreenP1 = getImage(SAMPLE_PASTELGREEN, XCOORD_BG_PASTELGREEN_P1, YCOORD_BG_PASTELGREEN_P1)
        self.bgSlimeGreenP1 = getImage(SAMPLE_SLIMEGREEN, XCOORD_BG_SLIMEGREEN_P1, YCOORD_BG_SLIMEGREEN_P1)
        self.bgSkyBlueP1 = getImage(SAMPLE_SKYBLUE, XCOORD_BG_SKYBLUE_P1, YCOORD_BG_SKYBLUE_P1)
        self.bgBlueP1 = getImage(SAMPLE_BLUE, XCOORD_BG_BLUE_P1, YCOORD_BG_BLUE_P1)
        self.bgBluePurpleP1 = getImage(SAMPLE_BLUEPURPLE, XCOORD_BG_BLUEPURPLE_P1, YCOORD_BG_BLUEPURPLE_P1)
        self.bgPurpleP1 = getImage(SAMPLE_PURPLE, XCOORD_BG_PURPLE_P1, YCOORD_BG_PURPLE_P1)
        self.bgMagentaP1 = getImage(SAMPLE_MAGENTA, XCOORD_BG_MAGENTA_P1, YCOORD_BG_MAGENTA_P1)
        self.bgStrawberryP2 = getImage(SAMPLE_STRAWBERRY, XCOORD_BG_STRAWBERRY_P2, YCOORD_BG_STRAWBERRY_P2)
        self.bgOrangeP2 = getImage(SAMPLE_ORANGE, XCOORD_BG_ORANGE_P2, YCOORD_BG_ORANGE_P2)
        self.bgButterscotchP2 = getImage(SAMPLE_BUTTERSCOTCH, XCOORD_BG_BUTTERSCOTCH_P2, YCOORD_BG_BUTTERSCOTCH_P2)
        self.bgBananaP2 = getImage(SAMPLE_BANANA, XCOORD_BG_BANANA_P2, YCOORD_BG_BANANA_P2)
        self.bgYellowP2 = getImage(SAMPLE_YELLOW, XCOORD_BG_YELLOW_P2, YCOORD_BG_YELLOW_P2)
        self.bgPastelGreenP2 = getImage(SAMPLE_PASTELGREEN, XCOORD_BG_PASTELGREEN_P2, YCOORD_BG_PASTELGREEN_P2)
        self.bgSlimeGreenP2 = getImage(SAMPLE_SLIMEGREEN, XCOORD_BG_SLIMEGREEN_P2, YCOORD_BG_SLIMEGREEN_P2)
        self.bgSkyBlueP2 = getImage(SAMPLE_SKYBLUE, XCOORD_BG_SKYBLUE_P2, YCOORD_BG_SKYBLUE_P2)
        self.bgBlueP2 = getImage(SAMPLE_BLUE, XCOORD_BG_BLUE_P2, YCOORD_BG_BLUE_P2)
        self.bgBluePurpleP2 = getImage(SAMPLE_BLUEPURPLE, XCOORD_BG_BLUEPURPLE_P2, YCOORD_BG_BLUEPURPLE_P2)
        self.bgPurpleP2 = getImage(SAMPLE_PURPLE, XCOORD_BG_PURPLE_P2, YCOORD_BG_PURPLE_P2)
        self.bgMagentaP2 = getImage(SAMPLE_MAGENTA, XCOORD_BG_MAGENTA_P2, YCOORD_BG_MAGENTA_P2)
        self.clearScores = Rectangle(Point(XCOORD_CLEARSCORES_TL, YCOORD_CLEARSCORES_TL), Point(XCOORD_CLEARSCORES_BR, YCOORD_CLEARSCORES_BR))
        self.clearScoresText = Text(Point(XCOORD_CLEARSCORESTEXT, YCOORD_CLEARSCORESTEXT), CLEARBOTHSCORES)
        self.quit = Rectangle(Point(XCOORD_QUIT_TL, YCOORD_QUIT_TL), Point(XCOORD_QUIT_BR, YCOORD_QUIT_BR))
        self.quitText = Text(Point(XCOORD_QUITTEXT, YCOORD_QUITTEXT), QUIT)
        self.currentMapText = Text(Point(XCOORD_CURRENTMAPTEXT, YCOORD_CURRENTMAPTEXT), CURRENTMAP)
        self.mapHumpback = Rectangle(Point(XCOORD_COLUMN1_TOPLEFT, YCOORD_MAP_HUMPBACK_TL), Point(XCOORD_COLUMN1_BOTTOMRIGHT, YCOORD_MAP_HUMPBACK_BR))
        self.mapInkblot = Rectangle(Point(XCOORD_COLUMN2_TOPLEFT, YCOORD_MAP_INKBLOT_TL), Point(XCOORD_COLUMN2_BOTTOMRIGHT, YCOORD_MAP_INKBLOT_BR))
        self.mapMoray = Rectangle(Point(XCOORD_COLUMN1_TOPLEFT, YCOORD_MAP_MORAY_TL), Point(XCOORD_COLUMN1_BOTTOMRIGHT, YCOORD_MAP_MORAY_BR))
        self.mapMusselforge = Rectangle(Point(XCOORD_COLUMN2_TOPLEFT, YCOORD_MAP_MUSSELFORGE_TL), Point(XCOORD_COLUMN2_BOTTOMRIGHT, YCOORD_MAP_MUSSELFORGE_BR))
        self.mapPort = Rectangle(Point(XCOORD_COLUMN1_TOPLEFT, YCOORD_MAP_PORT_TL), Point(XCOORD_COLUMN1_BOTTOMRIGHT, YCOORD_MAP_PORT_BR))
        self.mapReef = Rectangle(Point(XCOORD_COLUMN2_TOPLEFT, YCOORD_MAP_REEF_TL), Point(XCOORD_COLUMN2_BOTTOMRIGHT, YCOORD_MAP_REEF_BR))
        self.mapShifty = Rectangle(Point(XCOORD_COLUMN1_TOPLEFT, YCOORD_MAP_SHIFTY_TL), Point(XCOORD_COLUMN1_BOTTOMRIGHT, YCOORD_MAP_SHIFTY_BR))
        self.mapStarfish = Rectangle(Point(XCOORD_COLUMN2_TOPLEFT, YCOORD_MAP_STARFISH_TL), Point(XCOORD_COLUMN2_BOTTOMRIGHT, YCOORD_MAP_STARFISH_BR))
        self.mapSturgeon = Rectangle(Point(XCOORD_COLUMN1_TOPLEFT, YCOORD_MAP_STURGEON_TL), Point(XCOORD_COLUMN1_BOTTOMRIGHT, YCOORD_MAP_STURGEON_BR))
        self.mapAnchov = Rectangle(Point(XCOORD_COLUMN2_TOPLEFT, YCOORD_MAP_ANCHOV_TL), Point(XCOORD_COLUMN2_BOTTOMRIGHT, YCOORD_MAP_ANCHOV_BR))
        self.gametypeRM = Rectangle(Point(XCOORD_COLUMN1_TOPLEFT, YCOORD_GAMETYPE_RM_TL), Point(XCOORD_COLUMN1_BOTTOMRIGHT, YCOORD_GAMETYPE_RM_BR))
        self.gametypeSZ = Rectangle(Point(XCOORD_COLUMN2_TOPLEFT, YCOORD_GAMETYPE_SZ_TL), Point(XCOORD_COLUMN2_BOTTOMRIGHT, YCOORD_GAMETYPE_SZ_BR))
        self.gametypeTC = Rectangle(Point(XCOORD_COLUMN1_TOPLEFT, YCOORD_GAMETYPE_TC_TL), Point(XCOORD_COLUMN1_BOTTOMRIGHT, YCOORD_GAMETYPE_TC_BR))
        self.gametypeTW = Rectangle(Point(XCOORD_COLUMN2_TOPLEFT, YCOORD_GAMETYPE_TW_TL), Point(XCOORD_COLUMN2_BOTTOMRIGHT, YCOORD_GAMETYPE_TW_BR))
        self.bestOf3 = Rectangle(Point(XCOORD_BESTOF3_TL, YCOORD_BESTOF3_TL), Point(XCOORD_BESTOF3_BR, YCOORD_BESTOF3_BR))
        self.bestOf5 = Rectangle(Point(XCOORD_BESTOF5_TL, YCOORD_BESTOF5_TL), Point(XCOORD_BESTOF5_BR, YCOORD_BESTOF5_BR))
        self.bestOf7 = Rectangle(Point(XCOORD_BESTOF7_TL, YCOORD_BESTOF7_TL), Point(XCOORD_BESTOF7_BR, YCOORD_BESTOF5_BR))
        self.bestOfText = Text(Point(XCOORD_BESTOFTEXT, YCOORD_BESTOFTEXT), BESTOFTEXT)
        self.bestOf3Text = Text(Point(XCOORD_BESTOF3TEXT, YCOORD_BESTOF3TEXT), "3")
        self.bestOf5Text = Text(Point(XCOORD_BESTOF5TEXT, YCOORD_BESTOF5TEXT), "5")
        self.bestOf7Text = Text(Point(XCOORD_BESTOF7TEXT, YCOORD_BESTOF7TEXT), "7")
        self.mapHumpbackText = Text(Point(XCOORD_COLUMN1_TEXT, YCOORD_MAP_HUMPBACK_TEXT), MAP_HUMPBACK)
        self.mapInkblotText = Text(Point(XCOORD_COLUMN2_TEXT, YCOORD_MAP_INKBLOT_TEXT), MAP_INKBLOT)
        self.mapMorayText = Text(Point(XCOORD_COLUMN1_TEXT, YCOORD_MAP_MORAY_TEXT), MAP_MORAY)
        self.mapMusselforgeText = Text(Point(XCOORD_COLUMN2_TEXT, YCOORD_MAP_MUSSELFORGE_TEXT), MAP_MUSSELFORGE)
        self.mapPortText = Text(Point(XCOORD_COLUMN1_TEXT, YCOORD_MAP_PORT_TEXT), MAP_PORT)
        self.mapReefText = Text(Point(XCOORD_COLUMN2_TEXT, YCOORD_MAP_REEF_TEXT), MAP_REEF)
        self.mapShiftyText = Text(Point(XCOORD_COLUMN1_TEXT, YCOORD_MAP_SHIFTY_TEXT), MAP_SHIFTY)
        self.mapStarfishText = Text(Point(XCOORD_COLUMN2_TEXT, YCOORD_MAP_STARFISH_TEXT), MAP_STARFISH)
        self.mapSturgeonText = Text(Point(XCOORD_COLUMN1_TEXT, YCOORD_MAP_STURGEON_TEXT), MAP_STURGEON)
        self.mapAnchovText = Text(Point(XCOORD_COLUMN2_TEXT, YCOORD_MAP_ANCHOV_TEXT), MAP_ANCHOV)
        self.currentGametypeText = Text(Point(XCOORD_CURRENTGAMETYPETEXT, YCOORD_CURRENTGAMETYPETEXT), CURRENTGAMETYPE)
        self.gametypeRMText = Text(Point(XCOORD_COLUMN1_TEXT, YCOORD_GAMETYPE_RM_TEXT), GAMETYPE_RM)
        self.gametypeSZText = Text(Point(XCOORD_COLUMN2_TEXT, YCOORD_GAMETYPE_SZ_TEXT), GAMETYPE_SZ)
        self.gametypeTCText = Text(Point(XCOORD_COLUMN1_TEXT, YCOORD_GAMETYPE_TC_TEXT), GAMETYPE_TC)
        self.gametypeTWText = Text(Point(XCOORD_COLUMN2_TEXT, YCOORD_GAMETYPE_TW_TEXT), GAMETYPE_TW)
        self.gameScoreText = Text(Point(XCOORD_GAMESCORETEXT, YCOORD_GAMESCORETEXT), ENTERCURRENTGAMEFINALSCOREHERE)
        self.gameScore1Text = Text(Point(XCOORD_INPUTGAMESCORE1TEXT, YCOORD_INPUTGAMESCORE1TEXT), TEAM1)
        self.gameScore2Text = Text(Point(XCOORD_INPUTGAMESCORE2TEXT, YCOORD_INPUTGAMESCORE2TEXT), TEAM2)
        self.inputGameScore1 = Entry(Point(XCOORD_INPUTGAMESCORE1, YCOORD_INPUTGAMESCORE1), MAX_SCORE_LENGTH)
        self.inputGameScore2 = Entry(Point(XCOORD_INPUTGAMESCORE2, YCOORD_INPUTGAMESCORE2), MAX_SCORE_LENGTH)
        self.alertRecordedText = Text(Point(XCOORD_ALERT, YCOORD_ALERT), GAMERECORDED)
        self.alertRemovedText = Text(Point(XCOORD_ALERT, YCOORD_ALERT), GAMEDELETED)
        self.bsName1 = TEAM1
        self.bsName2 = TEAM2
        self.bsScore1 = 0
        self.bsScore2 = 0
        self.bsbackgroundImage1 = BG_ORDER
        self.bsbackgroundImage2 = BG_CHAOS
        self.bsText1 = Text(Point(BS_XCOORD_NAME1, BS_YCOORD_NAME1), self.bsName1)
        self.bsText2 = Text(Point(BS_XCOORD_NAME2, BS_YCOORD_NAME2), self.bsName2)
        self.bsImage1 = getImage(self.bsName1, BS_XCOORD_IMAGE1, BS_YCOORD_IMAGE1)
        self.bsImage2 = getImage(self.bsName2, BS_XCOORD_IMAGE2, BS_YCOORD_IMAGE2)
        self.bsbackgroundTeam1 = getImage(self.bsbackgroundImage1, BS_XCOORD_BACKGROUNDTEAM1, BS_YCOORD_BACKGROUNDTEAM1)
        self.bsbackgroundTeam2 = getImage(self.bsbackgroundImage2, BS_XCOORD_BACKGROUNDTEAM2, BS_YCOORD_BACKGROUNDTEAM2)
        self.bsBackgroundImageTeam1 = BS_BLUE
        self.bsBackgroundImageTeam2 = BS_SLIMEGREEN
        self.bsGame1Team1 = getImage(self.bsBackgroundImageTeam1, BS_XCOORD_GAME1TEAM1, BS_YCOORD_GAME1TEAM1)
        self.bsGame1Team2 = getImage(self.bsBackgroundImageTeam2, BS_XCOORD_GAME1TEAM2, BS_YCOORD_GAME1TEAM2)
        self.bsGame2Team1 = getImage(self.bsBackgroundImageTeam1, BS_XCOORD_GAME2TEAM1, BS_YCOORD_GAME2TEAM1)
        self.bsGame2Team2 = getImage(self.bsBackgroundImageTeam2, BS_XCOORD_GAME2TEAM2, BS_YCOORD_GAME2TEAM2)
        self.bsGame3Team1 = getImage(self.bsBackgroundImageTeam1, BS_XCOORD_GAME3TEAM1, BS_YCOORD_GAME3TEAM1)
        self.bsGame3Team2 = getImage(self.bsBackgroundImageTeam2, BS_XCOORD_GAME3TEAM2, BS_YCOORD_GAME3TEAM2)
        self.bsGame4Team1 = getImage(self.bsBackgroundImageTeam1, BS_XCOORD_GAME4TEAM1, BS_YCOORD_GAME4TEAM1)
        self.bsGame4Team2 = getImage(self.bsBackgroundImageTeam2, BS_XCOORD_GAME4TEAM2, BS_YCOORD_GAME4TEAM2)
        self.bsGame5Team1 = getImage(self.bsBackgroundImageTeam1, BS_XCOORD_GAME5TEAM1, BS_YCOORD_GAME5TEAM1)
        self.bsGame5Team2 = getImage(self.bsBackgroundImageTeam2, BS_XCOORD_GAME5TEAM2, BS_YCOORD_GAME5TEAM2)
        self.bsGame6Team1 = getImage(self.bsBackgroundImageTeam1, BS_XCOORD_GAME6TEAM1, BS_YCOORD_GAME6TEAM1)
        self.bsGame6Team2 = getImage(self.bsBackgroundImageTeam2, BS_XCOORD_GAME6TEAM2, BS_YCOORD_GAME6TEAM2)
        self.bsGame7Team1 = getImage(self.bsBackgroundImageTeam1, BS_XCOORD_GAME7TEAM1, BS_YCOORD_GAME7TEAM1)
        self.bsGame7Team2 = getImage(self.bsBackgroundImageTeam2, BS_XCOORD_GAME7TEAM2, BS_YCOORD_GAME7TEAM2)
        self.bsGame1Team1Text = Text(Point(BS_XCOORD_GAME1TEAM1, BS_YCOORD_GAME1TEAM1 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame1Team2Text = Text(Point(BS_XCOORD_GAME1TEAM2, BS_YCOORD_GAME1TEAM2 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame2Team1Text = Text(Point(BS_XCOORD_GAME2TEAM1, BS_YCOORD_GAME2TEAM1 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame2Team2Text = Text(Point(BS_XCOORD_GAME2TEAM2, BS_YCOORD_GAME2TEAM2 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame3Team1Text = Text(Point(BS_XCOORD_GAME3TEAM1, BS_YCOORD_GAME3TEAM1 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame3Team2Text = Text(Point(BS_XCOORD_GAME3TEAM2, BS_YCOORD_GAME3TEAM2 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame4Team1Text = Text(Point(BS_XCOORD_GAME4TEAM1, BS_YCOORD_GAME4TEAM1 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame4Team2Text = Text(Point(BS_XCOORD_GAME4TEAM2, BS_YCOORD_GAME4TEAM2 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame5Team1Text = Text(Point(BS_XCOORD_GAME5TEAM1, BS_YCOORD_GAME5TEAM1 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame5Team2Text = Text(Point(BS_XCOORD_GAME5TEAM2, BS_YCOORD_GAME5TEAM2 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame6Team1Text = Text(Point(BS_XCOORD_GAME6TEAM1, BS_YCOORD_GAME6TEAM1 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame6Team2Text = Text(Point(BS_XCOORD_GAME6TEAM2, BS_YCOORD_GAME6TEAM2 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame7Team1Text = Text(Point(BS_XCOORD_GAME7TEAM1, BS_YCOORD_GAME7TEAM1 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsGame7Team2Text = Text(Point(BS_XCOORD_GAME7TEAM2, BS_YCOORD_GAME7TEAM2 + BS_GAMETEAM_TEXT_OFFSET), "")
        self.bsScoreText1 = Text(Point(BS_XCOORD_SCORE1, BS_YCOORD_SCORE1), str(self.bsScore1))
        self.bsScoreText2 = Text(Point(BS_XCOORD_SCORE2, BS_YCOORD_SCORE2), str(self.bsScore2))
        self.bsGame1Header = getImage(BS_GAMEHEADER, BS_XCOORD_GAME1HEADER, BS_YCOORD_GAME1HEADER)
        self.bsGame2Header = getImage(BS_GAMEHEADER, BS_XCOORD_GAME2HEADER, BS_YCOORD_GAME2HEADER)
        self.bsGame3Header = getImage(BS_GAMEHEADER, BS_XCOORD_GAME3HEADER, BS_YCOORD_GAME3HEADER)
        self.bsGame4Header = getImage(BS_GAMEHEADER, BS_XCOORD_GAME4HEADER, BS_YCOORD_GAME4HEADER)
        self.bsGame5Header = getImage(BS_GAMEHEADER, BS_XCOORD_GAME5HEADER, BS_YCOORD_GAME5HEADER)
        self.bsGame6Header = getImage(BS_GAMEHEADER, BS_XCOORD_GAME6HEADER, BS_YCOORD_GAME6HEADER)
        self.bsGame7Header = getImage(BS_GAMEHEADER, BS_XCOORD_GAME7HEADER, BS_YCOORD_GAME7HEADER)
        self.bsGame1HeaderText = Text(Point(BS_XCOORD_GAME1HEADER, BS_YCOORD_GAME1HEADER + BS_GAMEHEADER_TEXT_OFFSET), "1")
        self.bsGame2HeaderText = Text(Point(BS_XCOORD_GAME2HEADER, BS_YCOORD_GAME2HEADER + BS_GAMEHEADER_TEXT_OFFSET), "2")
        self.bsGame3HeaderText = Text(Point(BS_XCOORD_GAME3HEADER, BS_YCOORD_GAME3HEADER + BS_GAMEHEADER_TEXT_OFFSET), "3")
        self.bsGame4HeaderText = Text(Point(BS_XCOORD_GAME4HEADER, BS_YCOORD_GAME4HEADER + BS_GAMEHEADER_TEXT_OFFSET), "4")
        self.bsGame5HeaderText = Text(Point(BS_XCOORD_GAME5HEADER, BS_YCOORD_GAME5HEADER + BS_GAMEHEADER_TEXT_OFFSET), "5")
        self.bsGame6HeaderText = Text(Point(BS_XCOORD_GAME6HEADER, BS_YCOORD_GAME6HEADER + BS_GAMEHEADER_TEXT_OFFSET), "6")
        self.bsGame7HeaderText = Text(Point(BS_XCOORD_GAME7HEADER, BS_YCOORD_GAME7HEADER + BS_GAMEHEADER_TEXT_OFFSET), "7")
        self.bestOfHowMany = 7

    def getAllMapText(self):
        return [self.mapHumpbackText, self.mapInkblotText, self.mapMorayText, self.mapMusselforgeText, self.mapPortText, self.mapReefText, self.mapShiftyText, self.mapStarfishText,
                self.mapSturgeonText, self.mapAnchovText]

    def getAllGametypeText(self):
        return [self.gametypeRMText, self.gametypeSZText, self.gametypeTCText, self.gametypeTWText]

    def getAllBoxscoreBackgrounds(self):
        return [self.bsGame1Team1, self.bsGame1Team2, self.bsGame2Team1, self.bsGame2Team2, self.bsGame3Team1, self.bsGame3Team2, self.bsGame4Team1, self.bsGame4Team2,
                self.bsGame5Team1, self.bsGame5Team2, self.bsGame6Team1, self.bsGame6Team2, self.bsGame7Team1, self.bsGame7Team2]

    def getAllBoxscoreText(self):
        return [self.bsGame1Team1Text, self.bsGame1Team2Text, self.bsGame2Team1Text, self.bsGame2Team2Text, self.bsGame3Team1Text, self.bsGame3Team2Text, self.bsGame4Team1Text,
                self.bsGame4Team2Text, self.bsGame5Team1Text, self.bsGame5Team2Text, self.bsGame6Team1Text, self.bsGame6Team2Text, self.bsGame7Team1Text, self.bsGame7Team2Text]

    def getAllBestOfText(self):
        return [self.bestOf3Text, self.bestOf5Text, self.bestOf7Text]

def getImage(teamName, x, y):
    try:
        im = Image(Point(x, y), teamName + ".png")
    except:
        im = Image(Point(x, y), DEFAULT_IMAGE)
    return im

def setupAndDrawBoxscoreFields(s):
    print("setupAndDrawBoxscoreFields")
    s.bsbackgroundTeam1.draw(s.boxscore_win)
    s.bsbackgroundTeam2.draw(s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsText1, TEAMNAME_FONT, TEAMNAME_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsText2, TEAMNAME_FONT, TEAMNAME_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsScoreText1, SCORE_FONT, SCORE_FONT_SIZE, SCORE_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsScoreText2, SCORE_FONT, SCORE_FONT_SIZE, SCORE_COLOR, s.boxscore_win)
    s.bsImage1.draw(s.boxscore_win)
    s.bsImage2.draw(s.boxscore_win)
    s.bsGame1Team1.draw(s.boxscore_win)
    s.bsGame1Team2.draw(s.boxscore_win)
    s.bsGame2Team1.draw(s.boxscore_win)
    s.bsGame2Team2.draw(s.boxscore_win)
    s.bsGame3Team1.draw(s.boxscore_win)
    s.bsGame3Team2.draw(s.boxscore_win)
    s.bsGame1Header.draw(s.boxscore_win)
    s.bsGame2Header.draw(s.boxscore_win)
    s.bsGame3Header.draw(s.boxscore_win)
    drawBoxscoreText(s)

def clearScores(s):
    print("clearScores")
    s.bsScore1 = 0
    s.bsScore2 = 0
    s.ScoreHistory = []
    updateBoxScoreTexts(s)
    s.bsScoreText1.undraw()
    s.bsScoreText2.undraw()
    s.bsScoreText1.setText(str(s.bsScore1))
    s.bsScoreText2.setText(str(s.bsScore2))
    setFaceSizeColorAndDraw(s.bsScoreText1, SCORE_FONT, SCORE_FONT_SIZE, SCORE_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsScoreText2, SCORE_FONT, SCORE_FONT_SIZE, SCORE_COLOR, s.boxscore_win)

def alterScore(s, team, delta):
    scoreChangeWasMade = False
    if team == 1:
        s.bsScore1 += delta
        if s.bsScore1 < 0:
            s.bsScore1 = 0
        else:
            scoreChangeWasMade = True
        s.bsScoreText1.undraw()
        s.bsScoreText1.setText(str(s.bsScore1))
        setFaceSizeColorAndDraw(s.bsScoreText1, SCORE_FONT, SCORE_FONT_SIZE, SCORE_COLOR, s.boxscore_win)
    else:
        s.bsScore2 += delta
        if s.bsScore2 < 0:
            s.bsScore2 = 0
        else:
            scoreChangeWasMade = True
        s.bsScoreText2.undraw()
        s.bsScoreText2.setText(str(s.bsScore2))
        setFaceSizeColorAndDraw(s.bsScoreText2, SCORE_FONT, SCORE_FONT_SIZE, SCORE_COLOR, s.boxscore_win)
    if scoreChangeWasMade:
        recordGameInformation(s, team, delta)

def updateBoxScoreTexts(s):
    idx = 0
    for game in s.ScoreHistory:
        if idx > 12:
            break
        s.getAllBoxscoreText()[idx].setText(game[0])
        s.getAllBoxscoreText()[idx + 1].setText(game[1])
        idx += 2
    while idx < 14:
        s.getAllBoxscoreText()[idx].setText("")
        s.getAllBoxscoreText()[idx + 1].setText("")
        idx += 2
    undrawBoxscoreGameFields(s)
    drawBoxscoreGameFields(s)

def recordGameInformation(s, team, delta):
    print([s.inputGameScore1.getText(), s.inputGameScore2.getText(), s.currentMap, s.currentGametype])
    if s.inputGameScore1.getText() == "0" and s.inputGameScore2.getText() == "0":
        if team == 1:
            s.inputGameScore1.setText(1)
        else:
            s.inputGameScore2.setText(1)
    if delta == 1:
        s.ScoreHistory.append([s.inputGameScore1.getText(), s.inputGameScore2.getText(), s.currentMap, s.currentGametype])
    else:
        idx = 0
        for x in s.ScoreHistory:
            if team == 1 and x[0] > x[1]:
                lastWin = idx
            if team == 2 and x[1] > x[0]:
                lastWin = idx
            idx += 1
        del s.ScoreHistory[lastWin]
    print(s.ScoreHistory)
    updateBoxScoreTexts(s)
    s.currentGametype = ""
    s.currentMap = ""
    selectMap(s, "")
    selectGametype(s, "")
    s.inputGameScore1.setText(0)
    s.inputGameScore2.setText(0)
    if delta == 1:
        setFaceSizeColorAndDraw(s.alertRecordedText, TEAMNAME_FONT, ENTRY_FONT_SIZE, ALERT_COLOR, s.settings_win)
    else:
        setFaceSizeColorAndDraw(s.alertRemovedText, TEAMNAME_FONT, ENTRY_FONT_SIZE, ALERT_COLOR, s.settings_win)
    time.sleep(1.5)
    if delta == 1:
        s.alertRecordedText.undraw()
    else:
        s.alertRemovedText.undraw()

def setFaceSizeColorAndDraw(obj, font, size, color, win):
    obj.setFace(font)
    obj.setSize(size)
    obj.setTextColor(color)
    obj.draw(win)

def setButtonUp(rect, win):
    rect.setFill('grey')
    rect.draw(win)

def undrawBoxscoreElements(s):
    print("undrawBoxscoreElements")
    s.bsbackgroundTeam1.undraw()
    s.bsbackgroundTeam2.undraw()
    s.bsText1.undraw()
    s.bsText2.undraw()
    s.bsImage1.undraw()
    s.bsImage2.undraw()
    s.bsGame1Team1Text.undraw()
    s.bsGame1Team2Text.undraw()
    s.bsGame2Team1Text.undraw()
    s.bsGame2Team2Text.undraw()
    s.bsGame3Team1Text.undraw()
    s.bsGame3Team2Text.undraw()
    s.bsScoreText1.undraw()
    s.bsScoreText2.undraw()
    s.bsGame1Team1.undraw()
    s.bsGame1Team2.undraw()
    s.bsGame2Team1.undraw()
    s.bsGame2Team2.undraw()
    s.bsGame3Team1.undraw()
    s.bsGame3Team2.undraw()
    s.bsGame1Header.undraw()
    s.bsGame2Header.undraw()
    s.bsGame3Header.undraw()
    s.bsGame1HeaderText.undraw()
    s.bsGame2HeaderText.undraw()
    s.bsGame3HeaderText.undraw()
    undrawBoxscoreGameFields(s)

def updateTeams(s):
    print("updateTeams")
    undrawBoxscoreElements(s)
    s.Name1 = s.inputName1.getText()
    s.Name2 = s.inputName2.getText()
    s.Text1 = Text(Point(XCOORD_NAME1, YCOORD_NAME1), s.Name1)
    s.Text2 = Text(Point(XCOORD_NAME2, YCOORD_NAME2), s.Name2)
    s.Image1 = getImage(TEAMLOGOS_FOLDER + s.Name1, XCOORD_IMAGE1, YCOORD_IMAGE1)
    s.Image2 = getImage(TEAMLOGOS_FOLDER + s.Name2, XCOORD_IMAGE2, YCOORD_IMAGE2)
    s.bsName1 = s.inputName1.getText()
    s.bsName2 = s.inputName2.getText()
    s.bsText1 = Text(Point(BS_XCOORD_NAME1, BS_YCOORD_NAME1), s.bsName1)
    s.bsText2 = Text(Point(BS_XCOORD_NAME2, BS_YCOORD_NAME2), s.bsName2)
    s.bsImage1 = getImage(TEAMLOGOS_FOLDER + s.bsName1, BS_XCOORD_IMAGE1, BS_YCOORD_IMAGE1)
    s.bsImage2 = getImage(TEAMLOGOS_FOLDER + s.bsName2, BS_XCOORD_IMAGE2, BS_YCOORD_IMAGE2)
    setupAndDrawBoxscoreFields(s)

def updateBackgroundColor(s, backgroundColor, boxscoreBackgroundColor, player):
    print("updateBackgroundColor")
    if player == 1:
        s.bsbackgroundImage1 = backgroundColor
        s.bsBackgroundImageTeam1 = boxscoreBackgroundColor
    else:
        s.bsbackgroundImage2 = backgroundColor
        s.bsBackgroundImageTeam2 = boxscoreBackgroundColor
    undrawBoxscoreElements(s)
    redrawBoxscoreFields(s)
    setupAndDrawBoxscoreFields(s)

def swapColors(s):
    print("swapColors")
    bstmpImage = s.bsbackgroundImage1
    s.bsbackgroundImage1 = s.bsbackgroundImage2
    s.bsbackgroundImage2 = bstmpImage
    bstmpTeamImage = s.bsBackgroundImageTeam1
    s.bsBackgroundImageTeam1 = s.bsBackgroundImageTeam2
    s.bsBackgroundImageTeam2 = bstmpTeamImage
    undrawBoxscoreElements(s)
    redrawBoxscoreFields(s)
    setupAndDrawBoxscoreFields(s)

def redrawBoxscoreFields(s):
    print("redrawBoxscoreFields")
    s.bsbackgroundTeam1 = getImage(s.bsbackgroundImage1, BS_XCOORD_BACKGROUNDTEAM1, BS_YCOORD_BACKGROUNDTEAM1)
    s.bsbackgroundTeam2 = getImage(s.bsbackgroundImage2, BS_XCOORD_BACKGROUNDTEAM2, BS_YCOORD_BACKGROUNDTEAM2)
    s.bsGame1Team1 = getImage(s.bsBackgroundImageTeam1, BS_XCOORD_GAME1TEAM1, BS_YCOORD_GAME1TEAM1)
    s.bsGame1Team2 = getImage(s.bsBackgroundImageTeam2, BS_XCOORD_GAME1TEAM2, BS_YCOORD_GAME1TEAM2)
    s.bsGame2Team1 = getImage(s.bsBackgroundImageTeam1, BS_XCOORD_GAME2TEAM1, BS_YCOORD_GAME2TEAM1)
    s.bsGame2Team2 = getImage(s.bsBackgroundImageTeam2, BS_XCOORD_GAME2TEAM2, BS_YCOORD_GAME2TEAM2)
    s.bsGame3Team1 = getImage(s.bsBackgroundImageTeam1, BS_XCOORD_GAME3TEAM1, BS_YCOORD_GAME3TEAM1)
    s.bsGame3Team2 = getImage(s.bsBackgroundImageTeam2, BS_XCOORD_GAME3TEAM2, BS_YCOORD_GAME3TEAM2)

def drawToSettingsWindow(s):
    print("drawToSettingsWindow")
    s.inputName1.setText(s.bsName1)
    s.inputName2.setText(s.bsName2)
    s.inputGameScore1.setText(0)
    s.inputGameScore2.setText(0)
    drawSettingsButtons(s)
    drawSettingsText(s)
    drawSettingsLines(s)
    drawSettingsBackgroundColorSamples(s)

def drawSettingsText(s):
    print("drawSettingsText")
    setFaceSizeColorAndDraw(s.inputName1, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.inputName2, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.inputName1Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.inputName2Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.controlsTeam1, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.controlsTeam2, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.updateTeamNamesText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.swapTeamsText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.minus1Team1Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.plus1Team1Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.minus1Team2Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.plus1Team2Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.clearScoresText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.quitText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.currentMapText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapHumpbackText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapInkblotText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapMorayText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapMusselforgeText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapPortText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapReefText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapShiftyText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapStarfishText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapSturgeonText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.mapAnchovText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.currentGametypeText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.gametypeRMText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.gametypeSZText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.gametypeTCText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.gametypeTWText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.gameScoreText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.gameScore1Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.gameScore2Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.inputGameScore1, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.inputGameScore2, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.bestOfText, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.bestOf3Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.bestOf5Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)
    setFaceSizeColorAndDraw(s.bestOf7Text, TEAMNAME_FONT, ENTRY_FONT_SIZE, TEAMNAME_COLOR, s.settings_win)

def drawBoxscoreText(s):
    print("drawBoxscoreText")
    setFaceSizeColorAndDraw(s.bsGame1Team1Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsGame1Team2Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsGame2Team1Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsGame2Team2Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsGame3Team1Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsGame3Team2Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsGame1HeaderText, TEAMNAME_FONT, HEADER_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsGame2HeaderText, TEAMNAME_FONT, HEADER_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    setFaceSizeColorAndDraw(s.bsGame3HeaderText, TEAMNAME_FONT, HEADER_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    drawBoxscoreGameFields(s)

def drawBoxscoreGameFields(s):
    print("drawBoxscoreGameFields")
    if s.bestOfHowMany > 3:
        s.bsGame4Header.draw(s.boxscore_win)
        s.bsGame5Header.draw(s.boxscore_win)
        s.bsGame4Team1 = getImage(s.bsBackgroundImageTeam1, BS_XCOORD_GAME4TEAM1, BS_YCOORD_GAME4TEAM1)
        s.bsGame4Team2 = getImage(s.bsBackgroundImageTeam2, BS_XCOORD_GAME4TEAM2, BS_YCOORD_GAME4TEAM2)
        s.bsGame5Team1 = getImage(s.bsBackgroundImageTeam1, BS_XCOORD_GAME5TEAM1, BS_YCOORD_GAME5TEAM1)
        s.bsGame5Team2 = getImage(s.bsBackgroundImageTeam2, BS_XCOORD_GAME5TEAM2, BS_YCOORD_GAME5TEAM2)
        s.bsGame4Team1.draw(s.boxscore_win)
        s.bsGame4Team2.draw(s.boxscore_win)
        s.bsGame5Team1.draw(s.boxscore_win)
        s.bsGame5Team2.draw(s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame4HeaderText, TEAMNAME_FONT, HEADER_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame5HeaderText, TEAMNAME_FONT, HEADER_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame4Team1Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame4Team2Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame5Team1Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame5Team2Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
    if s.bestOfHowMany > 5:
        s.bsGame6Header.draw(s.boxscore_win)
        s.bsGame7Header.draw(s.boxscore_win)
        s.bsGame6Team1 = getImage(s.bsBackgroundImageTeam1, BS_XCOORD_GAME6TEAM1, BS_YCOORD_GAME6TEAM1)
        s.bsGame6Team2 = getImage(s.bsBackgroundImageTeam2, BS_XCOORD_GAME6TEAM2, BS_YCOORD_GAME6TEAM2)
        s.bsGame7Team1 = getImage(s.bsBackgroundImageTeam1, BS_XCOORD_GAME7TEAM1, BS_YCOORD_GAME7TEAM1)
        s.bsGame7Team2 = getImage(s.bsBackgroundImageTeam2, BS_XCOORD_GAME7TEAM2, BS_YCOORD_GAME7TEAM2)
        s.bsGame6Team1.draw(s.boxscore_win)
        s.bsGame6Team2.draw(s.boxscore_win)
        s.bsGame7Team1.draw(s.boxscore_win)
        s.bsGame7Team2.draw(s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame6HeaderText, TEAMNAME_FONT, HEADER_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame7HeaderText, TEAMNAME_FONT, HEADER_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame6Team1Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame6Team2Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame7Team1Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)
        setFaceSizeColorAndDraw(s.bsGame7Team2Text, TEAMNAME_FONT, BOXSCORE_FONT_SIZE, TEAMNAME_COLOR, s.boxscore_win)

def undrawBoxscoreGameFields(s):
    print("undrawBoxscoreGameFields")
    s.bsGame6Header.undraw()
    s.bsGame7Header.undraw()
    s.bsGame6HeaderText.undraw()
    s.bsGame7HeaderText.undraw()
    s.bsGame6Team1Text.undraw()
    s.bsGame6Team2Text.undraw()
    s.bsGame7Team1Text.undraw()
    s.bsGame7Team2Text.undraw()
    s.bsGame6Team1.undraw()
    s.bsGame6Team2.undraw()
    s.bsGame7Team1.undraw()
    s.bsGame7Team2.undraw()
    s.bsGame4Header.undraw()
    s.bsGame5Header.undraw()
    s.bsGame4HeaderText.undraw()
    s.bsGame5HeaderText.undraw()
    s.bsGame4Team1Text.undraw()
    s.bsGame4Team2Text.undraw()
    s.bsGame5Team1Text.undraw()
    s.bsGame5Team2Text.undraw()
    s.bsGame4Team1.undraw()
    s.bsGame4Team2.undraw()
    s.bsGame5Team1.undraw()
    s.bsGame5Team2.undraw()

def drawSettingsLines(s):
    print("drawSettingsLines")
    line1 = Line(Point(10, 292), Point(330, 292))
    line1.setFill('white')
    line1.draw(s.settings_win)
    line2 = Line(Point(10, 650), Point(330, 650))
    line2.setFill('white')
    line2.draw(s.settings_win)

def drawSettingsButtons(s):
    print("drawSettingsButtons")
    setButtonUp(s.updateTeamNames, s.settings_win)
    setButtonUp(s.swapTeams, s.settings_win)
    setButtonUp(s.minus1Team1, s.settings_win)
    setButtonUp(s.plus1Team1, s.settings_win)
    setButtonUp(s.minus1Team2, s.settings_win)
    setButtonUp(s.plus1Team2, s.settings_win)
    setButtonUp(s.clearScores, s.settings_win)
    setButtonUp(s.quit, s.settings_win)
    setButtonUp(s.mapHumpback, s.settings_win)
    setButtonUp(s.mapInkblot, s.settings_win)
    setButtonUp(s.mapMoray, s.settings_win)
    setButtonUp(s.mapMusselforge, s.settings_win)
    setButtonUp(s.mapPort, s.settings_win)
    setButtonUp(s.mapReef, s.settings_win)
    setButtonUp(s.mapShifty, s.settings_win)
    setButtonUp(s.mapStarfish, s.settings_win)
    setButtonUp(s.mapSturgeon, s.settings_win)
    setButtonUp(s.mapAnchov, s.settings_win)
    setButtonUp(s.gametypeRM, s.settings_win)
    setButtonUp(s.gametypeSZ, s.settings_win)
    setButtonUp(s.gametypeTC, s.settings_win)
    setButtonUp(s.gametypeTW, s.settings_win)
    setButtonUp(s.bestOf3, s.settings_win)
    setButtonUp(s.bestOf5, s.settings_win)
    setButtonUp(s.bestOf7, s.settings_win)

def drawSettingsBackgroundColorSamples(s):
    print("drawSettingsBackgroundColorSamples")
    s.bgStrawberryP1.draw(s.settings_win)
    s.bgOrangeP1.draw(s.settings_win)
    s.bgButterscotchP1.draw(s.settings_win)
    s.bgBananaP1.draw(s.settings_win)
    s.bgYellowP1.draw(s.settings_win)
    s.bgPastelGreenP1.draw(s.settings_win)
    s.bgSlimeGreenP1.draw(s.settings_win)
    s.bgSkyBlueP1.draw(s.settings_win)
    s.bgBlueP1.draw(s.settings_win)
    s.bgBluePurpleP1.draw(s.settings_win)
    s.bgPurpleP1.draw(s.settings_win)
    s.bgMagentaP1.draw(s.settings_win)
    s.bgStrawberryP2.draw(s.settings_win)
    s.bgOrangeP2.draw(s.settings_win)
    s.bgButterscotchP2.draw(s.settings_win)
    s.bgBananaP2.draw(s.settings_win)
    s.bgYellowP2.draw(s.settings_win)
    s.bgPastelGreenP2.draw(s.settings_win)
    s.bgSlimeGreenP2.draw(s.settings_win)
    s.bgSkyBlueP2.draw(s.settings_win)
    s.bgBlueP2.draw(s.settings_win)
    s.bgBluePurpleP2.draw(s.settings_win)
    s.bgPurpleP2.draw(s.settings_win)
    s.bgMagentaP2.draw(s.settings_win)

def selectMap(s, mapText):
    for x in s.getAllMapText():
        x.undraw()
        if x is mapText:
            mapText.setTextColor("yellow")
        else:
            x.setTextColor("white")
        x.draw(s.settings_win)
    try:
        s.currentMap = mapText.getText()
    except:
        s.currentMap = ""

def selectGametype(s, gametypeText):
    for x in s.getAllGametypeText():
        x.undraw()
        if x is gametypeText:
            gametypeText.setTextColor("yellow")
        else:
            x.setTextColor("white")
        x.draw(s.settings_win)
    try:
        s.currentGametype = gametypeText.getText()
    except:
        s.currentGametype = ""

def wasClicked(lowerX, upperX, middleX, lowerY, upperY, middleY):
    return lowerX <= middleX and middleX <= upperX and lowerY <= middleY and middleY <= upperY

def updateBestOf(s, num, bestOfText):
    s.bestOfHowMany = num
    for x in s.getAllBestOfText():
        x.undraw()
        if x is bestOfText:
            bestOfText.setTextColor("yellow")
        else:
            x.setTextColor("white")
        x.draw(s.settings_win)
    undrawBoxscoreGameFields(s)
    drawBoxscoreGameFields(s)

def processMouseClick(s, clickLocation):
    clickX = clickLocation.getX()
    clickY = clickLocation.getY()

    # UPDATETEAMS
    if wasClicked(XCOORD_UPDATETEAMS_TL, XCOORD_UPDATETEAMS_BR, clickX, YCOORD_UPDATETEAMS_TL, YCOORD_UPDATETEAMS_BR, clickY):
        updateTeams(s)

    # SWAPCOLORS
    elif wasClicked(XCOORD_SWAPTEAMS_TL, XCOORD_SWAPTEAMS_BR, clickX, YCOORD_SWAPTEAMS_TL, YCOORD_SWAPTEAMS_BR, clickY):
        swapColors(s)

    # -1 TEAM1
    elif wasClicked(XCOORD_MINUS1TEAM1_TL, XCOORD_MINUS1TEAM1_BR, clickX, YCOORD_MINUS1TEAM1_TL, YCOORD_MINUS1TEAM1_BR, clickY):
        alterScore(s, 1, -1)

    # +1 TEAM1
    elif wasClicked(XCOORD_PLUS1TEAM1_TL, XCOORD_PLUS1TEAM1_BR, clickX, YCOORD_PLUS1TEAM1_TL, YCOORD_PLUS1TEAM1_BR, clickY):
        alterScore(s, 1, 1)

    # -1 TEAM2
    elif wasClicked(XCOORD_MINUS1TEAM2_TL, XCOORD_MINUS1TEAM2_BR, clickX, YCOORD_MINUS1TEAM2_TL, YCOORD_MINUS1TEAM2_BR, clickY):
        alterScore(s, 2, -1)

    # +1 TEAM2
    elif wasClicked(XCOORD_PLUS1TEAM2_TL, XCOORD_PLUS1TEAM2_BR, clickX, YCOORD_PLUS1TEAM2_TL, YCOORD_PLUS1TEAM2_BR, clickY):
        alterScore(s, 2, 1)

    # CLEARBOTH
    elif wasClicked(XCOORD_CLEARSCORES_TL, XCOORD_CLEARSCORES_BR, clickX, YCOORD_CLEARSCORES_TL, YCOORD_CLEARSCORES_BR, clickY):
        clearScores(s)

    # BACKGROUNDS P1
    elif wasClicked(XCOORD_BG_STRAWBERRY_P1 - 12, XCOORD_BG_STRAWBERRY_P1 + 12, clickX, YCOORD_BG_STRAWBERRY_P1 - 12, YCOORD_BG_STRAWBERRY_P1 + 12, clickY):
        updateBackgroundColor(s, BG_STRAWBERRY, BS_STRAWBERRY, 1)
    elif wasClicked(XCOORD_BG_ORANGE_P1 - 12, XCOORD_BG_ORANGE_P1 + 12, clickX, YCOORD_BG_ORANGE_P1 - 12, YCOORD_BG_ORANGE_P1 + 12, clickY):
        updateBackgroundColor(s, BG_ORANGE, BS_ORANGE, 1)
    elif wasClicked(XCOORD_BG_BUTTERSCOTCH_P1 - 12, XCOORD_BG_BUTTERSCOTCH_P1 + 12, clickX, YCOORD_BG_BUTTERSCOTCH_P1 - 12, YCOORD_BG_BUTTERSCOTCH_P1 + 12, clickY):
        updateBackgroundColor(s, BG_BUTTERSCOTCH, BS_BUTTERSCOTCH, 1)
    elif wasClicked(XCOORD_BG_BANANA_P1 - 12, XCOORD_BG_BANANA_P1 + 12, clickX, YCOORD_BG_BANANA_P1 - 12, YCOORD_BG_BANANA_P1 + 12, clickY):
        updateBackgroundColor(s, BG_BANANA, BS_BANANA, 1)
    elif wasClicked(XCOORD_BG_YELLOW_P1 - 12, XCOORD_BG_YELLOW_P1 + 12, clickX, YCOORD_BG_YELLOW_P1 - 12, YCOORD_BG_YELLOW_P1 + 12, clickY):
        updateBackgroundColor(s, BG_YELLOW, BS_YELLOW, 1)
    elif wasClicked(XCOORD_BG_PASTELGREEN_P1 - 12, XCOORD_BG_PASTELGREEN_P1 + 12, clickX, YCOORD_BG_PASTELGREEN_P1 - 12, YCOORD_BG_PASTELGREEN_P1 + 12, clickY):
        updateBackgroundColor(s, BG_PASTELGREEN, BS_PASTELGREEN, 1)
    elif wasClicked(XCOORD_BG_SLIMEGREEN_P1 - 12, XCOORD_BG_SLIMEGREEN_P1 + 12, clickX, YCOORD_BG_SLIMEGREEN_P1 - 12, YCOORD_BG_SLIMEGREEN_P1 + 12, clickY):
        updateBackgroundColor(s, BG_SLIMEGREEN, BS_SLIMEGREEN, 1)
    elif wasClicked(XCOORD_BG_SKYBLUE_P1 - 12, XCOORD_BG_SKYBLUE_P1 + 12, clickX, YCOORD_BG_SKYBLUE_P1 - 12, YCOORD_BG_SKYBLUE_P1 + 12, clickY):
        updateBackgroundColor(s, BG_SKYBLUE, BS_SKYBLUE, 1)
    elif wasClicked(XCOORD_BG_BLUE_P1 - 12, XCOORD_BG_BLUE_P1 + 12, clickX, YCOORD_BG_BLUE_P1 - 12, YCOORD_BG_BLUE_P1 + 12, clickY):
        updateBackgroundColor(s, BG_BLUE, BS_BLUE, 1)
    elif wasClicked(XCOORD_BG_BLUEPURPLE_P1 - 12, XCOORD_BG_BLUEPURPLE_P1 + 12, clickX, YCOORD_BG_BLUEPURPLE_P1 - 12, YCOORD_BG_BLUEPURPLE_P1 + 12, clickY):
        updateBackgroundColor(s, BG_BLUEPURPLE, BS_BLUEPURPLE, 1)
    elif wasClicked(XCOORD_BG_PURPLE_P1 - 12, XCOORD_BG_PURPLE_P1 + 12, clickX, YCOORD_BG_PURPLE_P1 - 12, YCOORD_BG_PURPLE_P1 + 12, clickY):
        updateBackgroundColor(s, BG_PURPLE, BS_PURPLE, 1)
    elif wasClicked(XCOORD_BG_MAGENTA_P1 - 12, XCOORD_BG_MAGENTA_P1 + 12, clickX, YCOORD_BG_MAGENTA_P1 - 12, YCOORD_BG_MAGENTA_P1 + 12, clickY):
        updateBackgroundColor(s, BG_MAGENTA, BS_MAGENTA, 1)

    # BACKGROUNDS P2
    elif wasClicked(XCOORD_BG_STRAWBERRY_P2 - 12, XCOORD_BG_STRAWBERRY_P2 + 12, clickX, YCOORD_BG_STRAWBERRY_P2 - 12, YCOORD_BG_STRAWBERRY_P2 + 12, clickY):
        updateBackgroundColor(s, BG_STRAWBERRY, BS_STRAWBERRY, 2)
    elif wasClicked(XCOORD_BG_ORANGE_P2 - 12, XCOORD_BG_ORANGE_P2 + 12, clickX, YCOORD_BG_ORANGE_P2 - 12, YCOORD_BG_ORANGE_P2 + 12, clickY):
        updateBackgroundColor(s, BG_ORANGE, BS_ORANGE, 2)
    elif wasClicked(XCOORD_BG_BUTTERSCOTCH_P2 - 12, XCOORD_BG_BUTTERSCOTCH_P2 + 12, clickX, YCOORD_BG_BUTTERSCOTCH_P2 - 12, YCOORD_BG_BUTTERSCOTCH_P2 + 12, clickY):
        updateBackgroundColor(s, BG_BUTTERSCOTCH, BS_BUTTERSCOTCH, 2)
    elif wasClicked(XCOORD_BG_BANANA_P2 - 12, XCOORD_BG_BANANA_P2 + 12, clickX, YCOORD_BG_BANANA_P2 - 12, YCOORD_BG_BANANA_P2 + 12, clickY):
        updateBackgroundColor(s, BG_BANANA, BS_BANANA, 2)
    elif wasClicked(XCOORD_BG_YELLOW_P2 - 12, XCOORD_BG_YELLOW_P2 + 12, clickX, YCOORD_BG_YELLOW_P2 - 12, YCOORD_BG_YELLOW_P2 + 12, clickY):
        updateBackgroundColor(s, BG_YELLOW, BS_YELLOW, 2)
    elif wasClicked(XCOORD_BG_PASTELGREEN_P2 - 12, XCOORD_BG_PASTELGREEN_P2 + 12, clickX, YCOORD_BG_PASTELGREEN_P2 - 12, YCOORD_BG_PASTELGREEN_P2 + 12, clickY):
        updateBackgroundColor(s, BG_PASTELGREEN, BS_PASTELGREEN, 2)
    elif wasClicked(XCOORD_BG_SLIMEGREEN_P2 - 12, XCOORD_BG_SLIMEGREEN_P2 + 12, clickX, YCOORD_BG_SLIMEGREEN_P2 - 12, YCOORD_BG_SLIMEGREEN_P2 + 12, clickY):
        updateBackgroundColor(s, BG_SLIMEGREEN, BS_SLIMEGREEN, 2)
    elif wasClicked(XCOORD_BG_SKYBLUE_P2 - 12, XCOORD_BG_SKYBLUE_P2 + 12, clickX, YCOORD_BG_SKYBLUE_P2 - 12, YCOORD_BG_SKYBLUE_P2 + 12, clickY):
        updateBackgroundColor(s, BG_SKYBLUE, BS_SKYBLUE, 2)
    elif wasClicked(XCOORD_BG_BLUE_P2 - 12, XCOORD_BG_BLUE_P2 + 12, clickX, YCOORD_BG_BLUE_P2 - 12, YCOORD_BG_BLUE_P2 + 12, clickY):
        updateBackgroundColor(s, BG_BLUE, BS_BLUE, 2)
    elif wasClicked(XCOORD_BG_BLUEPURPLE_P2 - 12, XCOORD_BG_BLUEPURPLE_P2 + 12, clickX, YCOORD_BG_BLUEPURPLE_P2 - 12, YCOORD_BG_BLUEPURPLE_P2 + 12, clickY):
        updateBackgroundColor(s, BG_BLUEPURPLE, BS_BLUEPURPLE, 2)
    elif wasClicked(XCOORD_BG_PURPLE_P2 - 12, XCOORD_BG_PURPLE_P2 + 12, clickX, YCOORD_BG_PURPLE_P2 - 12, YCOORD_BG_PURPLE_P2 + 12, clickY):
        updateBackgroundColor(s, BG_PURPLE, BS_PURPLE, 2)
    elif wasClicked(XCOORD_BG_MAGENTA_P2 - 12, XCOORD_BG_MAGENTA_P2 + 12, clickX, YCOORD_BG_MAGENTA_P2 - 12, YCOORD_BG_MAGENTA_P2 + 12, clickY):
        updateBackgroundColor(s, BG_MAGENTA, BS_MAGENTA, 2)
    elif wasClicked(XCOORD_QUIT_TL, XCOORD_QUIT_BR, clickX, YCOORD_QUIT_TL, YCOORD_QUIT_BR, clickY):
        exit(1)
    elif wasClicked(XCOORD_COLUMN1_TOPLEFT, XCOORD_COLUMN1_BOTTOMRIGHT, clickX, YCOORD_MAP_HUMPBACK_TL, YCOORD_MAP_HUMPBACK_BR, clickY):
        selectMap(s, s.mapHumpbackText)
    elif wasClicked(XCOORD_COLUMN2_TOPLEFT, XCOORD_COLUMN2_BOTTOMRIGHT, clickX, YCOORD_MAP_INKBLOT_TL, YCOORD_MAP_INKBLOT_BR, clickY):
        selectMap(s, s.mapInkblotText)
    elif wasClicked(XCOORD_COLUMN1_TOPLEFT, XCOORD_COLUMN1_BOTTOMRIGHT, clickX, YCOORD_MAP_MORAY_TL, YCOORD_MAP_MORAY_BR, clickY):
        selectMap(s, s.mapMorayText)
    elif wasClicked(XCOORD_COLUMN2_TOPLEFT, XCOORD_COLUMN2_BOTTOMRIGHT, clickX, YCOORD_MAP_MUSSELFORGE_TL, YCOORD_MAP_MUSSELFORGE_BR, clickY):
        selectMap(s, s.mapMusselforgeText)
    elif wasClicked(XCOORD_COLUMN1_TOPLEFT, XCOORD_COLUMN1_BOTTOMRIGHT, clickX, YCOORD_MAP_PORT_TL, YCOORD_MAP_PORT_BR, clickY):
        selectMap(s, s.mapPortText)
    elif wasClicked(XCOORD_COLUMN2_TOPLEFT, XCOORD_COLUMN2_BOTTOMRIGHT, clickX, YCOORD_MAP_REEF_TL, YCOORD_MAP_REEF_BR, clickY):
        selectMap(s, s.mapReefText)
    elif wasClicked(XCOORD_COLUMN1_TOPLEFT, XCOORD_COLUMN1_BOTTOMRIGHT, clickX, YCOORD_MAP_SHIFTY_TL, YCOORD_MAP_SHIFTY_BR, clickY):
        selectMap(s, s.mapShiftyText)
    elif wasClicked(XCOORD_COLUMN2_TOPLEFT, XCOORD_COLUMN2_BOTTOMRIGHT, clickX, YCOORD_MAP_STARFISH_TL, YCOORD_MAP_STARFISH_BR, clickY):
        selectMap(s, s.mapStarfishText)
    elif wasClicked(XCOORD_COLUMN1_TOPLEFT, XCOORD_COLUMN1_BOTTOMRIGHT, clickX, YCOORD_MAP_STURGEON_TL, YCOORD_MAP_STURGEON_BR, clickY):
        selectMap(s, s.mapSturgeonText)
    elif wasClicked(XCOORD_COLUMN2_TOPLEFT, XCOORD_COLUMN2_BOTTOMRIGHT, clickX, YCOORD_MAP_ANCHOV_TL, YCOORD_MAP_ANCHOV_BR, clickY):
        selectMap(s, s.mapAnchovText)
    elif wasClicked(XCOORD_COLUMN1_TOPLEFT, XCOORD_COLUMN1_BOTTOMRIGHT, clickX, YCOORD_GAMETYPE_RM_TL, YCOORD_GAMETYPE_RM_BR, clickY):
        selectGametype(s, s.gametypeRMText)
    elif wasClicked(XCOORD_COLUMN2_TOPLEFT, XCOORD_COLUMN2_BOTTOMRIGHT, clickX, YCOORD_GAMETYPE_SZ_TL, YCOORD_GAMETYPE_SZ_BR, clickY):
        selectGametype(s, s.gametypeSZText)
    elif wasClicked(XCOORD_COLUMN1_TOPLEFT, XCOORD_COLUMN1_BOTTOMRIGHT, clickX, YCOORD_GAMETYPE_TC_TL, YCOORD_GAMETYPE_TC_BR, clickY):
        selectGametype(s, s.gametypeTCText)
    elif wasClicked(XCOORD_COLUMN2_TOPLEFT, XCOORD_COLUMN2_BOTTOMRIGHT, clickX, YCOORD_GAMETYPE_TW_TL, YCOORD_GAMETYPE_TW_BR, clickY):
        selectGametype(s, s.gametypeTWText)

    # BEST OF BUTTONS
    elif wasClicked(XCOORD_BESTOF3_TL, XCOORD_BESTOF3_BR, clickX, YCOORD_BESTOF3_TL, YCOORD_BESTOF3_BR, clickY):
        updateBestOf(s, 3, s.bestOf3Text)
    elif wasClicked(XCOORD_BESTOF5_TL, XCOORD_BESTOF5_BR, clickX, YCOORD_BESTOF5_TL, YCOORD_BESTOF5_BR, clickY):
        updateBestOf(s, 5, s.bestOf5Text)
    elif wasClicked(XCOORD_BESTOF7_TL, XCOORD_BESTOF7_BR, clickX, YCOORD_BESTOF7_TL, YCOORD_BESTOF7_BR, clickY):
        updateBestOf(s, 7, s.bestOf7Text)

def main(s):
    s.settings_win.setBackground("black")
    s.boxscore_win.setBackground("black")
    setupAndDrawBoxscoreFields(s)
    drawToSettingsWindow(s)
    while 1:
        clickLocation = s.settings_win.getMouse()
        processMouseClick(s, clickLocation)

s = Splatoon()
main(s)
