from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import fury_swipes
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="05856e61-af17-522d-bc84-f208c4ac8a11",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast","Basic","Karrablast"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Mysterious Evolution",
            game_text="If Shelmet is in play, search your deck for a card that evolves from this Pokémon and put it onto this Pokémon. (This counts as evolving this Pokémon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
            condition=lambda board, player_id, pokemon: any(
                getattr(def_for(card.archetype_id), "display_name", "") == "Shelmet"
                for card in board.pokemon_in_play(player_id)
            ),
        ),
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=fury_swipes,
        ),
    ],
)
