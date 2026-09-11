from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="45732293-ce7a-535d-8272-718247a77104",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureEX.Name",
    display_name="Chandelure-EX",
    searchable_by=["Chandelure-EX","Basic","EX","ChandelureEX"],
    subtypes=["Basic","EX"],
    collector_number=77,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Eerie Glow",
            game_text="The Defending Pokémon is now Burned and Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=bw_legacy_attack,
        ),
    ],
)
