from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="76dd469a-0d3c-58b4-877b-73952a8c947f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume","Stage 2","Vileplume"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    abilities=[
        Ability(
            title="Allergy Panic",
            game_text="Apply Weakness for each Pokémon (both yours and your opponent's) as ×4 instead.",
            passive=bw_legacy_passive("Apply Weakness for each Pokémon (both yours and your opponent's) as ×4 instead."),
        ),
        Attack(
            title="Pollen Spray",
            game_text="The Defending Pokémon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=bw_legacy_attack,
        ),
    ],
)
