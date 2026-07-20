# Development Roadmap

The current client reaches the menus.

The next objective is to emulate the Home Server rather than simply ignoring requests.

---

# Phase 1

Intercept SendOperation()

Instead of only logging

[STUB]

switch(opCode)

and generate OperationResponses.

Example:

EquipWeapon

↓

update profile

↓

return Success

↓

fire ProfileChange event

The UI will immediately update.

---

# Phase 2

Build an in-memory Profile object.

The server owns:

PlayerProfile

Inventory

Currencies

Statistics

Equipment

XP

Level

All operations modify this object.

---

# Phase 3

Implement OperationResponse generation.

Examples:

UpdateAccountName

PurchaseItem

EquipWeapon

EquipHat

EquipSkin

SpendCurrency

GrantLoot

GetProfile

Each returns exactly what the original server returned.

---

# Phase 4

Implement Event generation.

Examples:

ProfileChange

FullProfile

PurchaseItemReceived

LootNotification

ChatMessage

These events update the client exactly as the original server did.

---

# Phase 5

Persistence

Save Profile

Load Profile

JSON initially.

Possible future SQLite backend.

---

# Phase 6

Progression

XP

Levels

Currencies

Loot

Unlocks

Statistics

Achievements

Weapon ownership

---

# Phase 7

AI Improvements

Current issue:

prefabs.Count = 0

Bots are not spawning.

Investigate:

AiSceneManager

BotBundle

BotDatabase

Prefab loading

Likely unrelated to the Home Server.

---

# Phase 8

Dedicated Emulator

Instead of stubs inside the client:

Client

↓

HomeServer Emulator

↓

Save Database

This restores the original architecture and makes future multiplayer possible.

---

# Immediate Next Task

Replace:

SendOperation()

↓

switch(opCode)

↓

fake OperationResponse

↓

fake EventData

↓

Client_OperationResponseReceived()

↓

Client_EventReceived()

Once this works, nearly every menu feature (shop, inventory, equipment, progression) should begin functioning without further client modifications.