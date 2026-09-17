from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.bw10 import giga_frost, outrage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="51ce1f22-1e65-5092-8b63-a36d057b676b",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name",
    display_name="Reshiram",
    searchable_by=["Reshiram","Basic","Reshiram"],
    subtypes=["Basic"],
    # Original client slots 116..140 hold Radiant Collection RC1..RC25.
    collector_number=137,
    attributes={AttrID.CARD_NUMBER_TEXT.value: {"type": "string", "value": "RC22"}},
    set_code="BW11",
    rarity=Rarities.RareUltra,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Outrage",
            game_text="Does 10 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=outrage,
        ),
        Attack(
            title="Blue Flare",
            game_text="Discard 2 Fire Energy attached to this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=bw_legacy_attack,
        ),
    ],
)
