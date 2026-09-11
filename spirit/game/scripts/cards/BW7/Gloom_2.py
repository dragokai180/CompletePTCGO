from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import bang_heads
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="3074097f-e79b-59c1-b65f-a8e8d573089d",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom","Stage 1","Gloom"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    abilities=[
        Attack(
            title="Foul Odor",
            game_text="Both this Pokémon and the Defending Pokémon are now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=bang_heads,
        ),
        Attack(
            title="Poison Powder",
            game_text="The Defending Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=bw_legacy_attack,
        ),
    ],
)
