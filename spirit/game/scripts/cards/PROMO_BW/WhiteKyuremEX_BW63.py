from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="351931d6-2241-54b2-883d-fc9805e20570",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyuremEX.Name",
    display_name="White Kyurem-EX",
    searchable_by=["White Kyurem-EX","Basic","EX","WhiteKyuremEX"],
    subtypes=["Basic","EX"],
    collector_number=63,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Dragon Stream",
            game_text="Flip a coin. If heads, attach a basic Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Ice Burn",
            game_text="Discard 2 Fire Energy attached to this Pokémon. The Defending Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=bw_legacy_attack,
        ),
    ],
)
