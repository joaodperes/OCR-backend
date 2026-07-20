from enum import IntEnum


class OpCode(IntEnum):

    SendCommand = 1
    SendChat = 2

    JoinSession = 3
    RequestSessionList = 4
    RequestSessionInfo = 5

    Authenticate = 7

    JoinLobby = 8
    ReserveSession = 9

    CreatePlayer = 40

    SendClientPlayerState = 42
    SendClientPlayerActions = 43
    SendClientPlayerFireWeapon = 44
    SendClientPlayerUseConsumable = 45

    StartMatch = 46
    RestartMatch = 47
    CancelMatch = 48
    EndMatch = 49