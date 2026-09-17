from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="2bda0c14-c242-5123-a3e6-7d71092ec9c2",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewEX.Name",
    display_name="Mew-EX",
    searchable_by=["Mew-EX","Basic","EX","MewEX"],
    subtypes=["Basic","EX"],
    # Original client slots 116..140 hold Radiant Collection RC1..RC25.
    collector_number=139,
    attributes={AttrID.CARD_NUMBER_TEXT.value: {"type": "string", "value": "RC24"}},
    set_code="BW11",
    rarity=Rarities.RareUltra,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Ability(
            title="Versatile",
            game_text="This Pokémon can use the attacks of any Pokémon in play (both yours and your opponent's). (You still need the necessary Energy to use each attack.)",
            passive=bw_legacy_passive("This Pokémon can use the attacks of any Pokémon in play (both yours and your opponent's). (You still need the necessary Energy to use each attack.)"),
        ),
        Attack(
            title="Replace",
            game_text="Move as many Energy attached to your Pokémon to your other Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=bw_legacy_attack,
        ),
    ],
)
