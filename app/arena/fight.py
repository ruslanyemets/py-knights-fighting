from app.knights.knight import Knight


class Fight:
    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection
        knight1.hp = Fight.check_hp(knight1.hp)
        knight2.hp = Fight.check_hp(knight2.hp)

    @staticmethod
    def check_hp(hp: int) -> int:
        if hp < 0:
            return 0
        return hp
