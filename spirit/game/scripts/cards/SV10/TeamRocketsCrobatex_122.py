from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="62196e0f-d111-543b-b346-73abeb73bb03",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsCrobatex.Name",
    display_name="Team Rocket's Crobat ex",
    searchable_by=["Team Rocket's Crobat ex", "Stage 2", "ex", "TeamRocketsCrobatex"],
    subtypes=["Stage 2", "ex"],
    collector_number=122,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGolbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Biting Spree",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may choose 2 of your opponent's Pokémon and put 2 damage counters on each of them.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Assassin's Return",
            game_text="You may put this Pokémon into your hand. (Discard all cards attached to this Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
