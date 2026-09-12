from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="10b93774-1edd-5d1e-8cd2-4b64c6523360",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo","Stage 1","Sharpedo","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=33,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon.",
            trigger="on_damaged_by_attack",
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Hard Bite",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
