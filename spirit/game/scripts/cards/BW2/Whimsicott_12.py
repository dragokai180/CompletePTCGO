from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="6b482de6-0d68-5459-9cf5-edeb768cdb0b",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott","Stage 1","Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    abilities=[
        Attack(
            title="Encore",
            game_text="Choose 1 of the Defending Pokémon's attacks. During your opponent's next turn, that Pokémon can only use that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="U-turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)
