from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="eb34c9f5-938a-5ca7-87d6-416e8b969318",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew","Basic","Axew"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="DV",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Flip a coin. If heads, search your deck for Fraxure, reveal it, and put it into your hand, Shuffle your deck afterward.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)
