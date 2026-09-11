from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_metal_energy_card
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="28260b7b-9560-58ee-8ec6-bd61479ddd03",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp","Stage 1","Bisharp"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="BW3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    abilities=[
        Attack(
            title="Energy Stream",
            game_text="Attach a Metal Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=attach_from_discard(predicate=is_metal_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Metal Scissors",
            game_text="Does 20 more damage for each Metal Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
