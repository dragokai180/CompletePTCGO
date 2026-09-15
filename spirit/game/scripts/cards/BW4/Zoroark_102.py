from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ed987ee1-1c65-52de-ada4-8f26b9c512d2",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark","Stage 1","Zoroark"],
    subtypes=["Stage 1"],
    collector_number=102,
    set_code="BW4",
    rarity=Rarities.RareSecret,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=search_to_hand(
                None, count=1, reveal=False,
                prompt="Choose a card to put into your hand.",
            ),
        ),
        Attack(
            title="Foul Play",
            game_text="Choose 1 of the Defending Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=bw_legacy_attack,
        ),
    ],
)
