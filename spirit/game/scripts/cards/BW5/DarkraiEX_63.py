from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="76fb1281-09a0-54fc-a2ae-539e8002d0c7",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiEX.Name",
    display_name="Darkrai-EX",
    searchable_by=["Darkrai-EX","Basic","EX","DarkraiEX"],
    subtypes=["Basic","EX"],
    collector_number=63,
    set_code="BW5",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    abilities=[
        Ability(
            title="Dark Cloak",
            game_text="Each of your Pokémon that has any Darkness Energy attached to it has no Retreat Cost.",
            passive=bw_legacy_passive("Each of your Pokémon that has any Darkness Energy attached to it has no Retreat Cost."),
        ),
        Attack(
            title="Night Spear",
            game_text="Does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=bw_legacy_attack,
        ),
    ],
)
