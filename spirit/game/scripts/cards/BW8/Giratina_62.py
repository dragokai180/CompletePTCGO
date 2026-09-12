from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import knock_off, reinforced_lariat
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="0a313014-dafe-5886-b081-4b2306a48e06",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina","Basic","Giratina","Team Plasma"],
    subtypes=["Basic","Team Plasma"],
    collector_number=62,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    abilities=[
        Attack(
            title="Hex",
            game_text="If the Defending Pokémon is affected by a Special Condition, this attack does 50 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Shadow Claw",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=knock_off,
        ),
    ],
)
