import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class PlayerGame(Base):
    __tablename__='PlayerGame'

    StatID = Column(Integer)
    TeamID = Column(Integer)
    PlayerID = Column(Integer)
    SeasonType = Column(Integer)
    Season = Column(Integer)
    Name = Column(String(50))
    Team = Column(String(10))
    Position = Column(String(10))
    PositionCategory = Column(String(10))
    Started = Column(Integer)
    BattingOrder = Column(Integer)
    FanDuelSalary = Column(Integer)
    DraftKingsSalary = Column(Integer)
    FantasyDataSalary = Column(Integer)
    YahooSalary = Column(Integer)
    InjuryStatus = Column(String(50))
    InjuryBodyPart = Column(String(50))
    InjuryStartDate = Column(DATETIME)
    InjuryNotes = Column(String(250))
    FanDuelPosition = Column(String(10))
    DraftKingsPosition = Column(String(10))
    YahooPosition = Column(String(10))
    OpponentRank = Column(Integer)
    OpponentPositionrank = Column(Integer)
    GlobalTeamID = Column(Integer)
    FantasyDraftSalary = Column(Integer)
    FantasyDraftPosition = Column(String(10))
    GameID = Column(Integer)
    OpponentID = Column(Integer)
    Opponent = Column(String(10))
    Day = Column(DATETIME)
    DateTime = Column(DATETIME)
    HomeOrAway = Column(String(4))
    IsGameOver = Column(Boolean)
    GlobalGameID = Column(Integer)
    GlobalOponentID = Column(Integer)
    Updated = Column(DATETIME)
    Games = Column(Integer)
    FantasyPoints = Column(DECIMAL(11,8))
    AtBats = Column(DECIMAL(11,8))
    Runs = Column(DECIMAL(11,8))
    Hits = Column(DECIMAL(11,8))
    Singles = Column(DECIMAL(11,8))
    Doubles = Column(DECIMAL(11,8))
    triples = Column(DECIMAL(11,8))
    HomeRuns = Column(DECIMAL(11,8))
    RunsBattedIn = Column(DECIMAL(11,8))
    BattingAverage = Column(DECIMAL(11,8))
    Outs = Column(DECIMAL(11,8))
    Strikeouts = Column(DECIMAL(11,8))
    Walks = Column(DECIMAL(11,8))
    HitByPitch = Column(DECIMAL(11,8))
    Sacrifices = Column(DECIMAL(11,8))
    SacrificeFlies = Column(DECIMAL(11,8))
    GroundIntoDoublePlay = Column(DECIMAL(11,8))
    StolenBases = Column(DECIMAL(11,8))
    CaughtStealing = Column(DECIMAL(11,8))
    PitchesSeen = Column(DECIMAL(11,8))
    OnBasePercentage = Column(DECIMAL(11,8))
    SluggingPercentage = Column(DECIMAL(11,8))
    OnBasePlusSlugging = Column(DECIMAL(11,8))
    Errors = Column(DECIMAL(11,8))
    Wins = Column(DECIMAL(11,8))
    Losses = Column(DECIMAL(11,8))
    Saves = Column(DECIMAL(11,8))
    InningsPitchedDecimal = Column(DECIMAL(11,8))
    TotalOutsPitched = Column(DECIMAL(11,8))
    InningsPitchedFull = Column(DECIMAL(11,8))
    InningsPitchedOuts = Column(DECIMAL(11,8))
    EarnedRunAverage = Column(DECIMAL(11,8))
    PitchingHits = Column(DECIMAL(11,8))
    PitchingRuns = Column(DECIMAL(11,8))
    PitchingEarnedRuns = Column(DECIMAL(11,8))
    PitchingWalks = Column(DECIMAL(11,8))
    PitchingStrikeouts = Column(DECIMAL(11,8))
    PitchingHomeRuns = Column(DECIMAL(11,8))
    PitchesThrown = Column(DECIMAL(11,8))
    PitchesThrownStrikes = Column(DECIMAL(11,8))
    WalksHitsPerInningsPitched = Column(DECIMAL(11,8))
    PitchingBattingAverageAgainst = Column(DECIMAL(11,8))
    GrandSlams = Column(DECIMAL(11,8))
    FantasyPointsFanDuel = Column(DECIMAL(11,8))
    FantasyPointsDraftKings = Column(DECIMAL(11,8))
    FantasyPointsYahoo = Column(DECIMAL(11,8))
    PlateAppearances = Column(DECIMAL(11,8))
    TotalBases = Column(DECIMAL(11,8))
    FlyOuts = Column(DECIMAL(11,8))
    GroundOuts = Column(DECIMAL(11,8))
    LineOuts = Column(DECIMAL(11,8))
    PopOuts = Column(DECIMAL(11,8))
    IntentionalWalks = Column(DECIMAL(11,8))
    ReachedOnError = Column(DECIMAL(11,8))
    BallsInPlay = Column(DECIMAL(11,8))
    BattingAverageOnBallsInPlay = Column(DECIMAL(11,8))
    WeightedOnBasePercentage = Column(DECIMAL(11,8))
    PitchingSingles = Column(DECIMAL(11,8))
    PitchingDoubles = Column(DECIMAL(11,8))
    PitchingTriples = Column(DECIMAL(11,8))
    PitchingGrandSlams = Column(DECIMAL(11,8))
    PitchingHitByPitch = Column(DECIMAL(11,8))
    PitchingSacrifices = Column(DECIMAL(11,8))
    PitchingSacrificeFlies = Column(DECIMAL(11,8))
    PitchingGroundIntoDoublePlay = Column(DECIMAL(11,8))
    PitchingCompleteGames = Column(DECIMAL(11,8))
    PitchingShutOuts = Column(DECIMAL(11,8))
    PitchingNoHitters = Column(DECIMAL(11,8))
    PitchingPerfectGames = Column(DECIMAL(11,8))
    PitchingPlateAppearances = Column(DECIMAL(11,8))
    PitchingTotalBases = Column(DECIMAL(11,8))
    PitchingFlyOuts = Column(DECIMAL(11,8))
    PitchingGroundOuts = Column(DECIMAL(11,8))
    PitchingLineOuts = Column(DECIMAL(11,8))
    PitchingPopOuts = Column(DECIMAL(11,8))
    PitchingIntentionalWalks = Column(DECIMAL(11,8))
    PitchingReachedOnError = Column(DECIMAL(11,8))
    PitchingCatchersInterference = Column(DECIMAL(11,8))
    PitchingBallsInPlay = Column(DECIMAL(11,8))
    PitchingOnBasePercentage = Column(DECIMAL(11,8))
    PitchingSluggingPercentage = Column(DECIMAL(11,8))
    PitchingOnBasePlusSlugging = Column(DECIMAL(11,8))
    PitchingStrikeoutsPerNineInnings = Column(DECIMAL(11,8))
    PitchingWalksPerNineInnings = Column(DECIMAL(11,8))
    PitchingBattingAverageOnBallsInPlay = Column(DECIMAL(11,8))
    PitchingWalksPerNineInnings = Column(DECIMAL(11,8))
    PitchingWeightedOnBasePercentage = Column(DECIMAL(11,8))
    DoublePlays = Column(DECIMAL(11,8))
    PitchingDoublePlays = Column(DECIMAL(11,8))
    BattingOrderConfirmed = Column(Boolean)
    IsolatedPower = Column(DECIMAL(11,8))
    FieldingIndependentPitching = Column(DECIMAL(11,8))
    PitchingQualityStarts = Column(DECIMAL(11,8))
    PitchingInningStarted = Column(DECIMAL(11,8))

    def __repr__(self):
        return '<Player: {0} r>'.format(self.Name)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



