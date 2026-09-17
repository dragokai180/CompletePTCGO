from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="f2a4375e-32ee-5f50-8341-1cdc3077d062",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe","Basic","Growlithe"],
    subtypes=["Basic"],
    # Original client slots 116..140 hold Radiant Collection RC1..RC25.
    collector_number=119,
    attributes={AttrID.CARD_NUMBER_TEXT.value: {"type": "string", "value": "RC4"}},
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Rest",
            game_text="Heal all damage from this Pokémon. This Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)
