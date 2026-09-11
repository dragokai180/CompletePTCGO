from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="778951a6-f7ce-5d18-a075-e5a024c5963d",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaMawileex.Name",
    display_name="Mega Mawile ex",
    searchable_by=["Mega Mawile ex", "Basic", "MEGA", "ex", "SV_Mega", "MegaMawileex"],
    subtypes=["Basic", "MEGA", "ex", "SV_Mega"],
    collector_number=94,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=303,
    abilities=[
        Attack(
            title="Gobble Down",
            game_text="This attack does 80 damage for each Prize card you have taken.",
            cost={PokemonTypes.METAL: 2},
            damage=80,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Huge Bite",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack's base damage is 30.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=standard_attack,
        ),
    ],
)
