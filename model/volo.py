from dataclasses import dataclass


@dataclass
class Volo:
    ID: int
    AIRLINE_ID: int
    FLIGHT_NUMBER: int
    ORIGIN_AIRPORT:int
    DESTINATION_AIRPORT:int
    DISTANCE:int

    def __hash__(self):
        return hash((self.ID,self.AIRLINE_ID, self.ORIGIN_AIRPORT, self.DESTINATION_AIRPORT))

    def __eq__(self, other):
        return self.ID == other.ID and self.AIRLINE_ID==other.AIRLINE_ID and self.ORIGIN_AIRPORT==other.ORIGIN_AIRPORT and self.DESTINATION_AIRPORT==other.DESTINATION_AIRPORT
