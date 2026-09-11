from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import creepy_wind, wind_blast
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="6fff0b86-4073-5055-b04b-c5cd23e14baa",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye","Basic","Sableye"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=creepy_wind,
        ),
        Attack(
            title="Junk Hunt",
            game_text="Put 2 Item cards from your discard pile into your hand.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=bw_legacy_attack,
        ),
    ],
)
