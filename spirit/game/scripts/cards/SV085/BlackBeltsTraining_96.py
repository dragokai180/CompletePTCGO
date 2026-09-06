from spirit.game.data_utils import SupporterCardDef, is_pokemon_ex
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _BlackBeltsTrainingPassive(Passive):
    """Your attacks do +40 to the opponent's Active Pokémon ex this turn."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if calc.attacker is None:
            return
        if carrier_pokemon(carrier) is not calc.attacker:
            return
        if is_pokemon_ex(calc.target.archetype_id):
            calc.amount += 40


async def black_belts_training(ctx):
    for p in ctx.my_pokemon_in_play():
        ctx.add_temporary_passive(
            p,
            _BlackBeltsTrainingPassive(),
            expires_after_turn=ctx.session.turn_state.turn_number,
        )


card = SupporterCardDef(
    guid="ac4a6266-b84b-5f04-a876-c2685a7cad68",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackBeltsTraining.Name",
    display_name="Black Belt's Training",
    searchable_by=["Black Belt's Training", "Supporter", "BlackBeltsTraining"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=black_belts_training,
)
