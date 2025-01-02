from app.database.participants import KNIGHTS
from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion
from app.arena.fight import Fight


def battle(knights_config: dict) -> dict:
    participants = {
        name: Knight(knight["name"], knight["power"], knight["hp"])
        for name, knight in knights_config.items()
    }

    for name, knight in participants.items():
        participant = knights_config.get(name)

        if participant.get("armour") is not None:
            knight_armour = [
                Armour(armour["part"], armour["protection"])
                for armour in participant.get("armour")
            ]

            for armour in knight_armour:
                knight.apply_armour(armour)

        weapon = Weapon(
            participant.get("weapon")["name"],
            participant.get("weapon")["power"]
        )

        knight.apply_weapon(weapon)

        if participant.get("potion") is not None:
            potion = Potion(
                participant.get("potion")["name"],
                participant.get("potion")["effect"]
            )

            knight.apply_potion(potion)

    Fight.fight(participants.get("lancelot"), participants.get("mordred"))
    Fight.fight(participants.get("arthur"), participants.get("red_knight"))

    return {knight.name: knight.hp for knight in participants.values()}


print(battle(KNIGHTS))
