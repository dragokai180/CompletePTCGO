from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import psypower
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="da216ba6-34ab-58c4-b490-858c74ba2605",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja","Stage 1","Shedinja"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    abilities=[
        Ability(
            title="Empty Shell",
            game_text="If this Pokémon is Knocked Out, your opponent can't take any Prize cards for it.",
            passive=bw_legacy_passive("If this Pokémon is Knocked Out, your opponent can't take any Prize cards for it."),
        ),
        Attack(
            title="Cursed Drop",
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=psypower,
        ),
    ],
)
