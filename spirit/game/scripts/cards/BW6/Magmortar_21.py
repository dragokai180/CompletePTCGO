from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import discard_own_energy
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="fe26e6b9-3200-5062-b4b9-a9a976ea7222",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmortar.Name",
    display_name="Magmortar",
    searchable_by=["Magmortar","Stage 1","Magmortar"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    abilities=[
        Attack(
            title="Flame Screen",
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy attached to this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=discard_own_energy,
        ),
    ],
)
