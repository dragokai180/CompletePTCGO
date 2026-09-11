from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import creepy_wind, wind_blast
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="d089aace-8b5a-55f0-b25b-7ea4f1c49b72",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent","Stage 1","Jellicent"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    abilities=[
        Ability(
            title="Stickiness",
            game_text="The Retreat Cost of each of your opponent's Pokémon in play is Colorless more.",
            passive=bw_legacy_passive("The Retreat Cost of each of your opponent's Pokémon in play is Colorless more."),
        ),
        Attack(
            title="Eerie Light",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=creepy_wind,
        ),
    ],
)
