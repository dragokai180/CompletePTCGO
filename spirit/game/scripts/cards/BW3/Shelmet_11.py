from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="489f3fbd-b612-5b4a-9a1b-2d90187bd979",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    display_name="Shelmet",
    searchable_by=["Shelmet","Basic","Shelmet"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Mysterious Evolution",
            game_text="If Karrablast is in play, search your deck for a card that evolves from this Pokémon and put it onto this Pokémon. (This counts as evolving this Pokémon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
            condition=lambda board, player_id, pokemon: any(
                getattr(def_for(card.archetype_id), "display_name", "") == "Karrablast"
                for card in board.pokemon_in_play(player_id)
            ),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
