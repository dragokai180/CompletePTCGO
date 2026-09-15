from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="971a7254-fbb8-5317-a3c7-0ba24364fe45",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaEX.Name",
    display_name="Lugia-EX",
    searchable_by=["Lugia-EX","Basic","EX","LugiaEX","Team Plasma"],
    subtypes=["Basic","EX","Team Plasma"],
    collector_number=102,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Ability(
            title="Overflow",
            game_text="If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card.",
            passive=bw_legacy_passive("If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card."),
        ),
        Attack(
            title="Plasma Gale",
            game_text="Discard a Plasma Energy attached to this Pokémon. If you can't discard a Plasma Energy, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=bw_legacy_attack,
        ),
    ],
)
