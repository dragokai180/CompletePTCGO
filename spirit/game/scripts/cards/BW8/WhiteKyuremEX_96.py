from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.bw10 import giga_frost, outrage

card = PokemonCardDef(
    guid="1eaf880a-a000-5608-a069-4c4f2dc8e0f6",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyuremEX.Name",
    display_name="White Kyurem-EX",
    searchable_by=["White Kyurem-EX","Basic","EX","WhiteKyuremEX"],
    subtypes=["Basic","EX"],
    collector_number=96,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="White Inferno",
            game_text="Does 10 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=outrage,
        ),
    ],
)
