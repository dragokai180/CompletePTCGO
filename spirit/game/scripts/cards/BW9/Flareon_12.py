from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="31474d37-cd9f-57ba-82bb-bae2f077ad52",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon","Stage 1","Flareon","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=12,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    abilities=[
        Attack(
            title="Vengeance",
            game_text="Does 10 more damage for each Pokémon in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pokémon does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=recoil_attack(10),
        ),
    ],
)
