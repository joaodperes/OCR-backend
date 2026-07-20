# Offensive Combat Redux - Offline Restoration Project

## Goal

Restore the Steam release of Offensive Combat Redux into a completely playable standalone game without requiring the original backend services.

The original game depended on several online services

- REST API
- Home Server
- Photon networking
- Accountprofile service
- Inventory service
- Matchmaking
- Progression
- Friends
- Chat
- Party system
- Shop

All of those services are now offline.

The objective is to recreate enough of the backend so the original client can run unchanged (or with only minimal patches) while believing it is communicating with the original infrastructure.

---

# Long Term Goals

The finished project should support

- Offline play
- AI matches
- Local progression
- Inventory
- Unlocks
- Currency
- Weapon customization
- Statistics
- Save games
- Optional LAN support
- Optional dedicated server
- Mod support

Eventually the project could support

- Community master server
- Online multiplayer
- Community accounts
- Cloud saves

---

# Design Philosophy

Whenever possible

- emulate the original server
- avoid modifying game code
- preserve original protocols
- preserve original gameplay

The client should continue using

REST
↓

HomeServer
↓

Photon

exactly as before.

The difference is that every server is now implemented locally.

---

# Architecture

Original

Game
    ↓
REST
    ↓
Home Server
    ↓
Photon Server
    ↓
Database

New

Game
    ↓
REST Emulator
    ↓
HomeServer Emulator
    ↓
Local Save Database (JSONSQLite)

Eventually

Game
    ↓
REST Emulator
    ↓
HomeServer Emulator
    ↓
Dedicated Game Server
    ↓
SQLite

---

# Current Status

REST
Working

Authentication
Working (development token)

Connection
Stubbed

Menus
Working

Gameplay
Offline AI launches

Progression
Not implemented

Inventory
Not implemented

Shop
Not implemented

Profile synchronization
Not implemented

---

# Backend Strategy

The backend will be implemented in stages.

Stage 1
- login
- profile loading
- basic menus

Stage 2
- profile persistence
- inventory
- currencies

Stage 3
- progression
- XP
- unlocks

Stage 4
- AI
- local multiplayer

Stage 5
- optional online multiplayer

---

# Save Format

Initially

JSON

Later optional

SQLite

This allows easy editing while developing and easy migration later.

---

# Guiding Rule

Whenever the client sends an operation

SendOperation()

the emulator should return the exact OperationResponse or EventData that the original server would have produced.

The goal is for the original client to never know the real servers disappeared.