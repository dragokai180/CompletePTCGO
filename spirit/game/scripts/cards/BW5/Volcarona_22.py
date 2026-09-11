from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="0b1c021e-6322-5075-bb77-d208613b35a7",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona","Stage 1","Volcarona"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    abilities=[
        Ability(
            title="Scorching Scales",
            game_text="Put 4 damage counters instead of 2 on your opponent's Burned Pokémon between turns.",
            passive=bw_legacy_passive("Put 4 damage counters instead of 2 on your opponent's Burned Pokémon between turns."),
        ),
        Attack(
            title="Burning Wind",
            game_text="You may discard an Energy attached to this Pokémon. If you do, the Defending Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=bw_legacy_attack,
        ),
    ],
)
