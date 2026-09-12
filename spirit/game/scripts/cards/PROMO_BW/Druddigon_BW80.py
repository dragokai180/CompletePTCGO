from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="86d1814e-6ee5-59c4-83ae-ebede51795c4",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon","Basic","Druddigon","Team Plasma"],
    subtypes=["Basic","Team Plasma"],
    collector_number=80,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Taunt",
            game_text="Switch 1 of your opponent's Benched Pokémon with the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Boost Claw",
            game_text="During your next turn, each of this Pokémon's attacks does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=bw_legacy_attack,
        ),
    ],
)
