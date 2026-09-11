from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="f3e6c08c-70e9-5fa6-afbd-2fc8891daa6d",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    display_name="Glaceon",
    searchable_by=["Glaceon","Stage 1","Glaceon"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    abilities=[
        Ability(
            title="Freeze Zone",
            game_text="The Retreat Cost of each of your Team Plasma Pokémon in play is ColorlessColorless less.",
            passive=bw_legacy_passive("The Retreat Cost of each of your Team Plasma Pokémon in play is ColorlessColorless less."),
        ),
        Attack(
            title="Icy Wind",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=powder_snow,
        ),
    ],
)
